# app/main.py
from fastapi import FastAPI
from app.api.routes import api_router
from app.core.db import get_database
app = FastAPI()
@app.get("/")
async def read_root():
    db = await get_database()
    return {"message": "Connected to MongoDB"}
app.include_router(api_router)

