from pydantic import BaseModel
from bson import ObjectId

class User(BaseModel):
    username: str
    password: str  # Raw password for incoming requests

    class Config:
        # This will allow pydantic to serialize ObjectId into a string
        json_encoders = {
            ObjectId: str
        }

class UserInDB(User):
    hashed_password: str  # We will store the hashed password in the DB
