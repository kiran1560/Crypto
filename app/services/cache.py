import asyncio
import time
from typing import Any, Optional

class SimpleCache:
    def __init__(self, ttl: int = 30):
        self.ttl = ttl
        self._cache = {}
        self._lock = asyncio.Lock()

    async def get(self, key: str) -> Optional[Any]:
        async with self._lock:
            entry = self._cache.get(key)
            if not entry:
                return None
            value, expires_at = entry
            if time.time() > expires_at:
                del self._cache[key]
                return None
            return value

    async def set(self, key: str, value: Any):
        async with self._lock:
            expires_at = time.time() + self.ttl
            self._cache[key] = (value, expires_at)

    async def clear(self):
        async with self._lock:
            self._cache.clear()
