import os
from functools import wraps
from typing import Callable, Any, Optional
from redis.asyncio import Redis
from aiocache import cached as aiocache_cached
from loguru import logger
from dotenv import load_dotenv
import asyncio

load_dotenv()

REDIS_URL = os.getenv('REDIS_URL')


async def get_redis_client() -> Optional[Redis]:
    try:
        if REDIS_URL:
            return Redis.from_url(REDIS_URL, decode_responses=True)
        return None
    except Exception as e:
        logger.error(f"Failed to initialize Redis client: {e}")
        return None


def cached(ttl: int = 60 * 60):
    def decorator(func: Callable) -> Callable:
        cached_func = aiocache_cached(ttl=ttl)(func)

        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            try:
                redis_client = await get_redis_client()

                result = await cached_func(*args, **kwargs)
                if result is not None:
                    logger.info("Cache hit: memory cache")
                    return result

                if redis_client:
                    cache_key = f"redis:{args[0]}" if args else "redis:default"
                    try:
                        redis_result = await redis_client.get(cache_key)
                        if redis_result:
                            logger.info("Cache hit: Redis cache")
                            return redis_result
                    except Exception as e:
                        logger.error(f"Redis error: {e}")
                    finally:
                        await redis_client.close()

                result = await func(*args, **kwargs)

                if result:
                    await cached_func(*args, **kwargs)

                    if redis_client:
                        try:
                            await redis_client.setex(cache_key, ttl, result)
                            logger.info("Cached in both memory and redis")
                        except Exception as e:
                            logger.error(f"Redis caching error: {e}")
                            logger.info("Cached in memory only")

                return result
            except Exception as e:
                logger.error(f"Caching error: {e}")
                return await func(*args, **kwargs)

        return wrapper
    return decorator
