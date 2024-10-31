from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_ONE_URL: str = os.getenv("DATABASE_ONE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 2
    QUEST_PROC_SERVICE_URL: str = os.getenv("QUEST_PROC_SERVICE_URL")
    QUEST_CATA_SERVICE_URL: str = os.getenv("QUEST_CATA_SERVICE_URL")
    USER_AUTH_SERVICE_URL: str = os.getenv("USER_AUTH_SERVICE_URL")

    class Config:
        env_file = ".env"

settings = Settings()