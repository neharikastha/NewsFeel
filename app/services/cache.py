import aioredis
import json

redis = aioredis.from_url("redis://redis:6379", decode_responses=True)

async def get_cached(topic: str):
    return await redis.get(topic)

async def set_cached(topic: str, data: list, ttl: int = 300):
    await redis.set(topic, json.dumps(data), ex=ttl)
