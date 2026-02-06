"""
Cache Service - Centralized cache management for all API caches
"""
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

class CacheManager:
    """Singleton cache manager for all application caches"""
    
    _instance = None
    _caches: Dict[str, Dict[str, Any]] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CacheManager, cls).__new__(cls)
            cls._instance._caches = {}
        return cls._instance
    
    def register_cache(self, cache_name: str, duration: timedelta):
        """Register a new cache type"""
        if cache_name not in self._caches:
            self._caches[cache_name] = {
                "data": None,
                "expires_at": None,
                "duration": duration,
                "name": cache_name
            }
    
    def get(self, cache_name: str) -> Optional[Any]:
        """Get cached data if valid"""
        if cache_name not in self._caches:
            return None
        
        cache = self._caches[cache_name]
        now = datetime.utcnow()
        
        if cache["data"] and cache["expires_at"] and now < cache["expires_at"]:
            return cache["data"]
        
        return None
    
    def set(self, cache_name: str, data: Any):
        """Set cache data with expiry"""
        if cache_name not in self._caches:
            raise ValueError(f"Cache '{cache_name}' not registered")
        
        now = datetime.utcnow()
        self._caches[cache_name]["data"] = data
        self._caches[cache_name]["expires_at"] = now + self._caches[cache_name]["duration"]
    
    def clear(self, cache_name: str):
        """Clear specific cache"""
        if cache_name in self._caches:
            self._caches[cache_name]["data"] = None
            self._caches[cache_name]["expires_at"] = None
            return True
        return False
    
    def clear_all(self):
        """Clear all caches"""
        for cache_name in self._caches:
            self._caches[cache_name]["data"] = None
            self._caches[cache_name]["expires_at"] = None
    
    def get_status(self, cache_name: str) -> Optional[Dict[str, Any]]:
        """Get cache status"""
        if cache_name not in self._caches:
            return None
        
        cache = self._caches[cache_name]
        now = datetime.utcnow()
        
        is_active = bool(cache["data"] and cache["expires_at"] and now < cache["expires_at"])
        
        status = {
            "name": cache_name,
            "is_active": is_active,
            "expires_at": cache["expires_at"].isoformat() if cache["expires_at"] else None,
            "item_count": len(cache["data"]) if cache["data"] and isinstance(cache["data"], list) else None,
            "duration_seconds": int(cache["duration"].total_seconds())
        }
        
        return status
    
    def get_all_status(self) -> list[Dict[str, Any]]:
        """Get status of all caches"""
        return [self.get_status(name) for name in self._caches.keys()]


# Global instance
cache_manager = CacheManager()
