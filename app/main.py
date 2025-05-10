from fastapi import FastAPI
from loguru import logger

from app import routes
from app.database import Base, engine

logger.debug("Starting the FastAPI application...")
app = FastAPI()

app.include_router(routes.router)

# Create database tables
logger.debug("Creating database tables...")
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo List API!"}
