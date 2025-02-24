import os
import asyncio
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Initialize FastAPI app
app = FastAPI()
load_dotenv()

# Fetch credentials securely from environment variables
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

# Ensure credentials are set
if not MONGO_USERNAME or not MONGO_PASSWORD:
    raise ValueError("MongoDB username or password is missing. Set them as environment variables.")

# Construct MongoDB connection string
MONGO_URL = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.5uyl0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Database name
DATABASE_NAME = "rewardconnect"

# Initialize MongoDB Client
client = AsyncIOMotorClient(MONGO_URL)
database = client[DATABASE_NAME]
users_collection = database["users"]

async def get_database():
    """Returns the database connection."""
    return database

async def test_db_connection():
    """Test MongoDB connection by listing collections."""
    try:
        collections = await database.list_collection_names()
        print("✅ MongoDB Connected Successfully!")
        print("📂 Collections in Database:", collections)
        return True  # Indicating success
    except Exception as e:
        print("❌ MongoDB Connection Error:", e)
        return False  # Indicating failure

@app.get("/")
async def read_root():
    """Checks MongoDB connection and returns a response."""
    is_connected = await test_db_connection()
    
    if is_connected:
        return {"status": "success", "message": "Connected to MongoDB"}
    else:
        return {"status": "error", "message": "Failed to connect to MongoDB"}

# Run the test function if executed directly
if __name__ == "__main__":
    asyncio.run(test_db_connection())
