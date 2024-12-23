﻿from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    image_url: str | None = None
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    image_url: str | None
    is_active: bool

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    image_url: Optional[str] = None
    password: Optional[str] = None
