from sqlalchemy.orm import Session 
from app.crud.base import BaseCRUD
import app.models 
import app.schemas

department_crud = BaseCRUD(
    app.models.Department
)

#===========================
# Get All Department
#===========================
def get_departments(
        db: Session
) -> list[app.models.Department]:
    return department_crud.get_all(db)


#===========================
# Get Department By ID
#===========================
def get_department(
        db: Session,
        department_id: int
) -> app.models.Department | None:
    
    return department_crud.get(
        db,
        department_id
    )


#===========================
# Get Department By Code
#===========================
def get_department_by_code(
        db: Session,
        code: str
) -> app.models.Department | None:
    
    return (
        db.query(app.models.Department)
        .filter(
            app.models.Department.code == code
        ).first()
    )

#===========================
# Create Department
#===========================
def create_department(
        db: Session,
        department: app.schemas.DepartmentCreate
) -> app.models.Department:
    
    return department_crud.create(
        db, department
    )

#===========================
# Update Department
#===========================
def update_department(
        db: Session,
        department_id: int,
        updated_department: app.schemas.DepartmentCreate
) -> app.models.Department | None:
    
    department = get_department(
        db,
        department_id
    )

    return department_crud.update(
        db,
        department,
        updated_department
    )

#===========================
# Delete Department
#===========================
def delete_department(
        db: Session,
        department_id: int
) -> app.models.Department | None:
    
    department = get_department(
        db,
        department_id
    )

    return department_crud.delete(
        db,
        department
    )
