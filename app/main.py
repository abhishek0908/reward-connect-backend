# app/main.py
from fastapi import FastAPI
from app.api.routes import api_router
from app.core.db import get_database,test_db_connection
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://reward-connect-fe.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Use only for development/testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    if test_db_connection():
        return {"message": "Connected to MongoDB"}
    else:
        return{"message":"Not Connected with MongoDB"}
app.include_router(api_router)

