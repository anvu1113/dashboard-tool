from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class SupportedDomainBase(SQLModel):
    domain: str = Field(unique=True, index=True)
    is_active: bool = Field(default=True)
    source_language: Optional[str] = Field(default=None, max_length=10)
    target_language: Optional[str] = Field(default=None, max_length=10)

class SupportedDomain(SupportedDomainBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SupportedDomainCreate(SupportedDomainBase):
    pass

class SupportedDomainRead(SupportedDomainBase):
    id: int
    created_at: datetime

class SupportedDomainUpdate(SQLModel):
    domain: Optional[str] = None
    is_active: Optional[bool] = None
    source_language: Optional[str] = None
    target_language: Optional[str] = None
