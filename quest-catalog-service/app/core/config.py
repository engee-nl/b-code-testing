from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_TWO_URL: str = os.getenv("DATABASE_TWO_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM: str = "HS256"
    QUEST_PROC_SERVICE_URL: str = os.getenv("QUEST_PROC_SERVICE_URL")
    QUEST_CATA_SERVICE_URL: str = os.getenv("QUEST_CATA_SERVICE_URL")
    USER_AUTH_SERVICE_URL: str = os.getenv("USER_AUTH_SERVICE_URL")
    GRPC_SERVER_URL: str = os.getenv("GRPC_SERVER_URL")

    class Config:
        env_file = ".env"

settings = Settings()