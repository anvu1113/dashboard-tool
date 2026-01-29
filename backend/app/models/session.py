from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from .user import User

class UserSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    token_jti: str = Field(index=True, unique=True) # JWT ID
    
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_active_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[User] = Relationship()
