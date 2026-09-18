from pydantic import BaseModel, ConfigDict, EmailStr, Field


#------------------------------
# User Schemas
#------------------------------
class UserBase(BaseModel):

    username: str = Field(
        min_length=3,
        max_length=30
    )

    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(
        min_length=6,
        max_length=100
    )

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    role: str
    model_config = ConfigDict(
        from_attributes=True
    )
    
   

