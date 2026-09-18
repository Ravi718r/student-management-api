from datetime import datetime

from pydantic import BaseModel, ConfigDict


#Base Schema
class CourseBase(BaseModel):
    name: str
    code: str
    duration: int
    department_id: int

# Create Schema
class CourseCreate(CourseBase):
    pass 

# Update Schema
class CourseUpdate(CourseBase):
    pass 


# Response Schema
class CourseResponse(CourseBase):
    id: int 
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )