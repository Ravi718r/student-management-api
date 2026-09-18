import os
from dotenv import load_dotenv

# Load .env file
load_dotenv() 


# Read values from .env 
DATABASE_URL = os.getenv("DATABASE_URL") 

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in .env")

SECRET_KEY= os.getenv("SECRET_KEY")

ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)