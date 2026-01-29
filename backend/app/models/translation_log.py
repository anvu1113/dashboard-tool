from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class TranslationLog(SQLModel, table=True):
    __tablename__ = "translation_logs_detail" # Avoid conflict with existing usage_logs table if name collision

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="user.id")
    
    action: str = Field(max_length=50) # 'translate_text'
    engine: str = Field(max_length=20) # 'argos', 'cache', 'db'
    text_hash: str = Field(index=True, max_length=64)
    char_count: int
    context: Optional[str] = Field(default=None, max_length=50)
    latency_ms: Optional[int] = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
