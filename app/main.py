# app/main.py
from fastapi import FastAPI
from app.api.routes import api_router
from app.core.db import get_database,test_db_connection
app = FastAPI()
@app.get("/")
async def read_root():
    if test_db_connection():
        return {"message": "Connected to MongoDB"}
    else:
        return{"message":"Not Connected with MongoDB"}
app.include_router(api_router)

