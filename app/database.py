from motor.motor_asyncio import AsyncIOMotorClient

from app.config import cfg

client = AsyncIOMotorClient(cfg.get_db_uri())

