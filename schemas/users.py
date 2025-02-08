from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):# Herança
    password: str
    role: Optional[str] = "user"
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr 
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
