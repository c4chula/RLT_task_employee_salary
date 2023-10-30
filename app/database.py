from motor.motor_asyncio import AsyncIOMotorClient
from app.config import Settings

client = AsyncIOMotorClient(Settings().get_db_uri)

