from dotenv import load_dotenv
import os

load_dotenv()
def get_database_url():
    DATABASE_URL = os.getenv('DATABASE_URL')
    if DATABASE_URL is None:
        raise RuntimeError("DATABASE_URL environment variable is not set.")
    
    return DATABASE_URL
