# from sqlalchemy.orm import Session

from app.database import SessionLocal

#Database Dependecy 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  


