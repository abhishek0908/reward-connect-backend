from fastapi import APIRouter, HTTPException
from app.core.db import users_collection
from app.api.schemas.auth import LoginRequest, RegisterRequest
from app.core.security import hash_password, verify_password, create_jwt_token

router = APIRouter()

@router.get("/hello")
def hello_world():
    return {"message": "Hello, World!"}

@router.post("/register")
async def register_api(user: RegisterRequest):
    # Check if passwords match
    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    # Check if user already exists
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Hash password and store user
    hashed_password = hash_password(user.password)
    user_data = {"username": user.username, "email": user.email, "password": hashed_password}
    await users_collection.insert_one(user_data)

    return {"message": "User registered successfully"}

@router.post("/login")
async def login_api(user: LoginRequest):
    # Find user by username or email
    existing_user = await users_collection.find_one({
        "$or": [{"email": user.username_or_email}, {"username": user.username_or_email}]
    })
    
    if not existing_user or not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate JWT Token
    token = create_jwt_token({"username": existing_user["username"], "email": existing_user["email"]})
    
    return {"message": "Login successful", "token": token}
