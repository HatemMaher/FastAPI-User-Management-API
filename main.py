from fastapi import FastAPI

from routers.user_router import router as user_router

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Project 1"
    }


app.include_router(user_router)