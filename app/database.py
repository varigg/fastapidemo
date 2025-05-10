import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from the .env file
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("PROD_DB")  # Default production database

# Use in-memory database for testing
if os.getenv("TESTING"):
    SQLALCHEMY_DATABASE_URL = os.getenv("TEST_DB")

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # type: ignore
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
