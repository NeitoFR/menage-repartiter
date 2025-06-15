from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    nom: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True 