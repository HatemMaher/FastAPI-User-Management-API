from fastapi import FastAPI

from routers.user_router import router as user_router
from routers.auth_router import router as auth_router

from database.database import engine
from database.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Welcome to Project 1"
    }


app.include_router(user_router)

app.include_router(auth_router)