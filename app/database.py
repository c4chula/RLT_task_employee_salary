from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

from app.config import cfg

client = AsyncIOMotorClient(cfg.get_db_uri())

class MotorAsyncSessionfactory:

    async def get_client_session(self) -> AsyncIOMotorClientSession:
        async with await client.start_session() as session:
            return session
