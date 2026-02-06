from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, String, Text

class TranslationPhrase(SQLModel, table=True):
    __tablename__ = "translation_phrases"

    id: Optional[int] = Field(default=None, primary_key=True)
    
    src_lang: str = Field(index=True, max_length=10)
    tgt_lang: str = Field(index=True, max_length=10)
    
    src_text_hash: str = Field(index=True, max_length=64)
    src_text: str = Field(sa_column=Column(Text))
    
    translated_text: str = Field(sa_column=Column(Text))
    
    engine: str = Field(default="argos") # 'google', 'argos', 'manual'
    confidence_score: float = Field(default=1.0)
    
    usage_count: int = Field(default=0)
    last_used_at: datetime = Field(default_factory=datetime.utcnow)
    
    updated_by: Optional[int] = Field(default=None) # user_id of admin
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
