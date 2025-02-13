from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_reward():
    return "Hello, to Reward!"
