from sqlalchemy.orm import Session

class BaseCRUD:

    def __init__(
            self,
            model
    ):
        self.model = model

    # ============================================
    # Get By ID
    # ============================================
    def get(
            self,
            db: Session,
            object_id: int
    ):
        return (
            db.query(self.model)
            .filter(self.model.id == object_id)
            .first()
        )
    

    # ============================================
    # Get All
    # ============================================
    def get_all(
        self,
        db: Session
    ):
        return (
            db.query(self.model)
            .all()
        )
    

    # ============================================
    # Create
    # ============================================
    def create(
        self,
        db: Session,
        obj
    ):
        db_obj = self.model(
            **obj.model_dump()
        )

        db.add(db_obj)

        db.commit()

        db.refresh(db_obj)

        return db_obj
    

    # ============================================
    # Update
    # ============================================
    def update(
        self,
        db: Session,
        db_obj,
        obj 
    ):
        for key, value in obj.model_dump().items():

            setattr(
                db_obj,
                key,
                value
            )

        db.commit()

        db.refresh(db_obj)

        return db_obj
    

    # ============================================
    # Delete
    # ============================================
    def delete(
        self,
        db: Session,
        db_obj
    ):
        db.delete(  db_obj)

        db.commit()

        return db_obj