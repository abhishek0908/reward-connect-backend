from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = "mongodb://localhost:27017"  # MongoDB URI
    database_name: str = "test_db"  # Database name

settings = Settings()

# MongoDB client and database instance
client = AsyncIOMotorClient(settings.mongo_uri)
db = client[settings.database_name]
