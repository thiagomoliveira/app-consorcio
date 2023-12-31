from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Get database path from environment variable
DATABASE_PATH = os.getenv("DATABASE_PATH")
DEBUG_MODE = os.getenv("DEBUG", "False") == "True"

if not DATABASE_PATH:
    raise ValueError("The 'DATABASE_PATH' variable was not found in the .env file")

# Define the database path
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=DEBUG_MODE)

# Create a base session
Session = sessionmaker(bind=engine)

# Create a declarative base
Base = declarative_base()
