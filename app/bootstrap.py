from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User
from app.auth import hash_password

def create_default_admin():

    db: Session = SessionLocal()

    try:
        # Check if an admin already exists 
        admin = db.query(User).filter(
            User.role =="admin"
        ).first()

        if admin:
            print("Admin Already exists.")
            return
        
        default_admin = User(
            username="admin",
            email="admin@gmail.com",
            hashed_password=hash_password("123456"),
            role ="admin"
        )

        db.add(default_admin)
        db.commit()

        print("Default admin created Successfully!!")

    finally:
        db.close()