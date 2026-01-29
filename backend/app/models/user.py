from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    name: Optional[str] = None
    role: str = Field(default="user")
    phone: Optional[str] = None

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
