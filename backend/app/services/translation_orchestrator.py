from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.models.phrase import TranslationPhrase
from app.models.translation_log import TranslationLog
from app.services.cache import get_cache_service
from app.services.translation import get_translation_service
from app.services.subscription import SubscriptionService
from app.models.user import User
import json
import time

class TranslationOrchestrator:
    def __init__(self, session: AsyncSession, user: User):
        self.session = session
        self.user = user
        self.cache = get_cache_service()
        self.sub_service = SubscriptionService(session)

    async def translate(self, text: str, source: str, target: str, engine_id: str = "argos", context: str = "general") -> dict:
        """
        Layer 1: Phrase DB
        Layer 2: Redis Cache
        Layer 3: Engine
        """
        start_time = time.time()
        text_normalized = text.strip()
        text_hash = self.cache.generate_hash(text_normalized, source, target, engine_id)
        
        result_data = None
        source_layer = "unknown"
        
        try:
            # --- Layer 1: Phrase DB ---
            # Only for short texts
            if len(text_normalized) < 100:
                query = select(TranslationPhrase).where(
                    TranslationPhrase.source_lang == source,
                    TranslationPhrase.target_lang == target,
                    TranslationPhrase.source_text == text_normalized
                )
                result = await self.session.exec(query)
                phrase = result.first()
                if phrase:
                    source_layer = "db"
                    result_data = {
                        "translated": phrase.translated_text,
                        "source": "db",
                        "engine": engine_id
                    }

            # --- Layer 2: Redis Cache ---
            if not result_data:
                cached_result = await self.cache.get(text_hash)
                
                if cached_result:
                    source_layer = "cache"
                    result_data = {
                        "translated": cached_result,
                        "source": "cache",
                        "engine": engine_id
                    }

            # --- Layer 3: Engine ---
            if not result_data:
                source_layer = engine_id # 'argos' or 'ai'
                
                # 3.1 Check Quota (Delegate to SubscriptionService)
                allowed = await self.sub_service.can_use_feature(self.user, "translate_requests")
                if not allowed:
                     raise Exception("Quota reached")

                # 3.2 Call Engine
                translator = get_translation_service(engine_id)
                try:
                    translated_text = translator.translate(text_normalized, source, target)
                except Exception as e:
                    # Fallback or re-raise
                    raise e

                # 3.3 Save to Cache (Write-back)
                # Determine TTL based on context (simplified logic)
                ttl = 86400 * 30 # 30 days default
                if context == 'description':
                    ttl = 86400 * 30
                elif context == 'ui':
                    ttl = 86400 * 90
                    
                await self.cache.set(text_hash, translated_text, ttl=ttl)

                # 3.4 Log Usage (Aggregate for Quota)
                await self.sub_service.increment_usage(self.user, "translate_requests")
                
                result_data = {
                    "translated": translated_text,
                    "source": "engine",
                    "engine": engine_id
                }

            return result_data

        finally:
            # Commit Transactional Log
            latency = int((time.time() - start_time) * 1000)
            await self._log_request(
                text_hash=text_hash,
                char_count=len(text_normalized),
                engine=source_layer,
                context=context,
                latency_ms=latency
            )

        # 3.4 Log Usage (Aggregate for Quota)
        await self.sub_service.increment_usage(self.user, "translate_requests")
        
        # 3.5 Log Detail (For Tracking/Billing - according to V2 Design)
        # We calculate latency strictly for engine call or end-to-end? 
        # Design says "latency_ms" for engine request. simpler to just log end-to-end for now or engine specific.
        # Let's log the Engine usage specifically.
        
        # NOTE: If we want to log CACHE hits too, we should move this logging out of the "Layer 3" block
        # and into a `finally` or common return path. 
        # But V2 Design says "Save Cache + Log Usage" at Step 5.
        
        return {
            "translated": translated_text,
            "source": "engine",
            "engine": engine_id
        }

    async def _log_request(self, text_hash: str, char_count: int, engine: str, context: str, latency_ms: int):
        log = TranslationLog(
            user_id=self.user.id if self.user else None,
            action="translate_text",
            engine=engine,
            text_hash=text_hash,
            char_count=char_count,
            context=context,
            latency_ms=latency_ms
        )
        self.session.add(log)
        await self.session.commit()
