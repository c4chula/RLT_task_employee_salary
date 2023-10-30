from pydantic_settings import BaseSettings


class MongoDBSettings(BaseSettings):


    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    def get_db_uri(self) -> str:
        return f"mongodb://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

class AiogramBotSettings(BaseSettings):

    BOT_TOKEN: str

class Settings(MongoDBSettings, AiogramBotSettings):

    class Config:
        env_file=".env"

cfg = Settings()
