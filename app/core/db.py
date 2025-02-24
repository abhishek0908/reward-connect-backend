from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "mydatabase"

client = AsyncIOMotorClient(MONGO_URL)
database = client[DATABASE_NAME]
users_collection = database["users"]

async def get_database():
    return database
