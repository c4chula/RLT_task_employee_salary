from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession

from app.config import cfg

client = AsyncIOMotorClient(
    host=cfg.DB_HOST,
    username=cfg.DB_USERNAME,
    password=cfg.DB_PASSWORD,
)


class MotorAsyncSessionfactory:
    async def get_client_session(self) -> AsyncIOMotorClientSession:
        async with await client.start_session() as session:
            return session
