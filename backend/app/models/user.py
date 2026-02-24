from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from typing import List, Optional
from app.models.user_role import UserRole
from app.models.role import RoleReadSimple # Safe import as role.py doesn't depend on User
if False:
    from app.models.role import Role, RoleReadSimple

class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    name: Optional[str] = None
    role: str = Field(default="user")
    phone: Optional[str] = None

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    is_super_admin: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    roles: List["Role"] = Relationship(back_populates="users", link_model=UserRole)

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    roles: List["RoleReadSimple"] = []

class UserUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    role: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None

