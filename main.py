from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

# Reference the environment configuration 
config = dotenv_values(".env")


@asynccontextmanager
async def lifespan(app:FastAPI):
    app.mongodb_client = MongoClient(config["DB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
    yield
    app.mongodb_client.close()


app = FastAPI(lifespan=lifespan, title="Librongo Home Digital Library")


app.include_router(book_router, tags=["books"], prefix="/book")

# @app.get("/")
# async def root():
#     return {"message": "Welcome to Librongo - Home Library"}