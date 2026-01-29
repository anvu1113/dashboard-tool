from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class TranslationPhrase(SQLModel, table=True):
    __tablename__ = "translation_phrases"

    id: Optional[int] = Field(default=None, primary_key=True)
    source_lang: str = Field(index=True, max_length=10)
    target_lang: str = Field(index=True, max_length=10)
    source_text: str = Field(index=True, max_length=255)
    translated_text: str = Field(max_length=255)
    context: Optional[str] = Field(default=None, max_length=50) # 'ui', 'error', etc
    priority: int = Field(default=0)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
