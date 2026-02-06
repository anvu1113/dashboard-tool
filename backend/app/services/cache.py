import redis.asyncio as redis
import os
import json
import hashlib

class CacheService:
    def __init__(self):
        self.redis_url = os.environ.get("REDIS_URL", "redis://redis:6379")
        self.client = redis.from_url(self.redis_url, decode_responses=True)

    async def get(self, key: str):
        return await self.client.get(key)
    
    async def set(self, key: str, value: str, ttl: int = 86400):
        await self.client.set(key, value, ex=ttl)

    @staticmethod
    def generate_hash(text: str, source: str, target: str, engine: str) -> str:
        # hash = sha256(normalized_text + source + target + engine)
        raw = f"{text.strip()}|{source}|{target}|{engine}"
        return hashlib.sha256(raw.encode()).hexdigest()

# Global instance
_cache_service = None

def get_cache_service() -> CacheService:
    global _cache_service
    if not _cache_service:
        _cache_service = CacheService()
    return _cache_service
