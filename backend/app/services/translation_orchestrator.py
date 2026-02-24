from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.models.phrase import TranslationPhrase
from app.models.translation_log import TranslationLog
from app.services.cache import get_cache_service
from app.services.translation import get_translation_service
from app.services.translation.argos import ArgosService
from app.services.translation.google import GoogleService
from app.services.subscription import SubscriptionService
from app.models.user import User
import json
import time
from datetime import datetime
from app.core.logger import engine_logger, error_logger

class TranslationOrchestrator:
    def __init__(self, session: AsyncSession, user: User):
        self.session = session
        self.user = user
        self.cache = get_cache_service()
        self.sub_service = SubscriptionService(session)
        
        # Initialize Engines
        self.argos_engine = ArgosService()
        self.google_engine = GoogleService()

    async def translate(self, text: str, source: str, target: str, engine_id: str = "auto", context: str = "general") -> dict:
        print(f"DEBUG_REQUEST: translate('{text}', {source}->{target}, engine_id='{engine_id}')", flush=True)
        """
        Orchestration Flow:
        1. Redis Cache
        2. DB (Translation Memory)
        3. Engine Strategy (Google/Argos)
        """
        start_time = time.time()
        text_normalized = text.strip()
        
        # Normalize Language Codes (Global)
        if source.lower() in ['zh', 'zh-cn']:
            source = 'zh-CN'
        if target.lower() in ['zh', 'zh-cn']:
            target = 'zh-CN'
            
        # Hash based on content + lang pair (use 'hybrid_v2' to distinguish from legacy argos hashes)
        text_hash = self.cache.generate_hash(text_normalized, source, target, "hybrid_v2") 
        
        result_data = None
        source_layer = "unknown"
        used_engine = "none"
        confidence = 0.0

        try:
            # --- Layer 1: Redis Cache ---
            cached_result = await self.cache.get(text_hash)
            if cached_result:
                used_engine = "cache" # For logging
                return {
                    "translated": cached_result,
                    "source": "cache",
                    "engine": "cache"
                }

            # --- Layer 2: Phrase DB (Translation Memory) ---
            from app.models.phrase import TranslationPhrase
            # query source_lang -> src_lang
            query = select(TranslationPhrase).where(
                TranslationPhrase.src_lang == source,
                TranslationPhrase.tgt_lang == target,
                TranslationPhrase.src_text_hash == text_hash
            )
            result = await self.session.exec(query)
            phrase = result.first()
            
            if phrase:
                # HIT DB
                source_layer = "db"
                used_engine = phrase.engine
                translated_text = phrase.translated_text
                
                # Write-back to Redis
                await self.cache.set(text_hash, translated_text, ttl=86400 * 30)
                
                return {
                    "translated": translated_text,
                    "source": "db",
                    "engine": phrase.engine
                }

            # --- Layer 3: External Engine ---
            
            # 3.1 Check User Quota
            if self.user:
                allowed = await self.sub_service.can_use_feature(self.user, "translate_requests")
                if not allowed:
                     raise Exception("Quota reached")

            # 3.2 Strategy Selection
            primary, backup = self._select_strategy(source, target, engine_id)
            # print(f"DEBUG_STRATEGY: Primary={primary.__class__.__name__}, Backup={backup.__class__.__name__ if backup else 'None'}")
            
            translated_text = None
            
            # Try Primary
            try:
                translated_text = primary.translate(text_normalized, source, target)
                used_engine = "google" if isinstance(primary, GoogleService) else "argos"
                confidence = 1.0 if used_engine == "google" else 0.7
                # print(f"DEBUG_ENGINE: Success {used_engine} -> {translated_text}")
            except Exception as e:
                error_logger.error(f"Primary Engine ({primary}) failed: {e}")
                print(f"CRITICAL_DEBUG: Primary Engine failed for '{text_normalized}' ({source}->{target}) | Error: {e}", flush=True)
                # Try Backup
                if backup:
                    try:
                        translated_text = backup.translate(text_normalized, source, target)
                        used_engine = "google" if isinstance(backup, GoogleService) else "argos"
                        confidence = 1.0 if used_engine == "google" else 0.7
                        # print(f"DEBUG_ENGINE: Backup success {used_engine} -> {translated_text}")
                    except Exception as e2:
                        error_logger.error(f"Backup Engine ({backup}) failed: {e2}")
                        # print(f"DEBUG_ENGINE: Backup failed -> {e2}")
                        raise e2
                else:
                    raise e
            
            source_layer = "engine"
            
            # 3.3 Save to DB (Translation Memory)
            # Reverted 'skip save' logic as requested by user to debug
            await self._save_phrase(
                text=text_normalized,
                translated=translated_text,
                source=source,
                target=target,
                text_hash=text_hash,
                engine=used_engine,
                confidence=confidence
            )
            
            # 3.4 Save to Redis
            await self.cache.set(text_hash, translated_text, ttl=86400 * 30)
            
            # 3.5 Increment Quota
            if self.user:
                await self.sub_service.increment_usage(self.user, "translate_requests")

            return {
                "translated": translated_text,
                "source": "engine",
                "engine": used_engine
            }

        finally:
            # Commit Transactional Log
            latency = int((time.time() - start_time) * 1000)
            await self._log_request(
                text_hash=text_hash,
                char_count=len(text_normalized),
                engine=used_engine,
                context=context,
                latency_ms=latency,
                source=source,
                target=target,
                cost=0.0
            )

    def _select_strategy(self, source: str, target: str, requested_engine: str):
        # Force specific
        if requested_engine == "google":
            return self.google_engine, None
        if requested_engine == "argos":
            return self.argos_engine, None

        # Rule 1: Vietnamese -> Google Priority
        if source == 'vi' or target == 'vi':
            return self.google_engine, self.argos_engine
        
        # Rule 2: English <-> Chinese/Spanish -> using Argos Priority (Good enough)
        return self.argos_engine, self.google_engine

    async def _save_phrase(self, text, translated, source, target, text_hash, engine, confidence):
        try:
            from app.models.phrase import TranslationPhrase
            phrase = TranslationPhrase(
                src_lang=source,
                tgt_lang=target,
                src_text=text,
                src_text_hash=text_hash,
                translated_text=translated,
                engine=engine,
                confidence_score=confidence,
                usage_count=1
            )
            self.session.add(phrase)
            await self.session.commit()
            # print("DEBUG_DB: Saved phrase successfully")
        except Exception as e:
            # print(f"DEBUG_DB: Failed to save phrase: {e}")
            error_logger.error(f"Failed to save translation phrase: {e}")
            # Do not re-raise to avoid failing the user request, just log error

    async def _log_request(self, text_hash: str, char_count: int, engine: str, context: str, latency_ms: int, source: str, target: str, cost: float):
        log = TranslationLog(
            user_id=self.user.id if self.user else None,
            action="translate_text",
            engine=engine,
            source_lang=source,
            target_lang=target,
            text_hash=text_hash,
            char_count=char_count,
            context=context,
            cost_estimate=cost,
            latency_ms=latency_ms
        )
        self.session.add(log)
        await self.session.commit()
