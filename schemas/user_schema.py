from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    is_active: bool

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    is_active: bool
    