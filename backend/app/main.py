from fastapi import Depends,HTTPException,FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.db.database import get_db

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "backend": "working"
    }

@app.get("/health/db")
def database_health(db: Session=Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )