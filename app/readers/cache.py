import os
from functools import wraps
from typing import Callable, Any, Optional
from redis.asyncio import Redis
from aiocache import cached as aiocache_cached
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv('REDIS_URL')
redis_client: Optional[Redis] = Redis.from_url(
    REDIS_URL) if REDIS_URL else None
CACHE_TTL = 60 * 60


def cached(ttl: int = CACHE_TTL):
    def decorator(func: Callable) -> Callable:
        def _cache_key(*args, **kwargs):
            return f"mem:{args[0]}" if args else "mem:default"

        memory_cached = aiocache_cached(ttl=ttl, key_builder=_cache_key)
        cached_func = memory_cached(func)

        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            try:
                result = await cached_func(*args, **kwargs)
                result = None
                if result is not None:
                    logger.info("cache hit: memory cache")
                    return result

                if redis_client:
                    cache_key = f"redis:{args[0]}" if args else "redis:default"
                    try:
                        redis_result = await redis_client.get(cache_key)
                        if redis_result:
                            result = redis_result.decode()
                            logger.info("cache hit: Redis cache")
                            return result
                    except Exception as e:
                        logger.error(f"redis error: {e}")

                result = await func(*args, **kwargs)

                if result:
                    await memory_cached(func)(*args, **kwargs)

                    if redis_client:
                        try:
                            await redis_client.setex(cache_key, ttl, result)
                            logger.info("cached in both memory and redis")
                        except Exception as e:
                            logger.error(f"redis caching error: {e}")
                            logger.info("cached in memory only")

                return result
            except Exception as e:
                logger.error(f"caching error: {e}")
                return await func(*args, **kwargs)

        return wrapper
    return decorator
