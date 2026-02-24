from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from app.models.user_role import UserRole

# Link table for Role <-> Permission
class RolePermission(SQLModel, table=True):
    role_id: int = Field(foreign_key="role.id", primary_key=True)
    permission_id: int = Field(foreign_key="permission.id", primary_key=True)

class Permission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(unique=True, index=True) # e.g. "users.view"
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    roles: List["Role"] = Relationship(back_populates="permissions", link_model=RolePermission)

class Role(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(unique=True, index=True) # e.g. "admin", "staff"
    name: str 
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    users: List["User"] = Relationship(back_populates="roles", link_model=UserRole)
    permissions: List["Permission"] = Relationship(back_populates="roles", link_model=RolePermission)

# Read Schema to avoid infinite recursion
class PermissionRead(SQLModel):
    id: int
    code: str
    description: Optional[str] = None
    created_at: datetime

class RoleReadSimple(SQLModel):
    id: int
    code: str
    name: str

class RoleRead(SQLModel):
    id: int
    code: str
    name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    permissions: List[PermissionRead] = []
