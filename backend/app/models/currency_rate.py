from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class CurrencyRateBase(SQLModel):
    currency_code: str = Field(max_length=10, unique=True, index=True)
    currency_name: str = Field(max_length=100)
    buy_rate: Optional[float] = Field(default=None)
    transfer_rate: Optional[float] = Field(default=None)
    sell_rate: Optional[float] = Field(default=None)


class CurrencyRate(CurrencyRateBase, table=True):
    __tablename__ = "currency_rates"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class CurrencyRateRead(CurrencyRateBase):
    id: int
    created_at: datetime
    updated_at: datetime


class CurrencyRateCreate(CurrencyRateBase):
    pass


class CurrencyRateUpdate(SQLModel):
    currency_name: Optional[str] = None
    buy_rate: Optional[float] = None
    transfer_rate: Optional[float] = None
    sell_rate: Optional[float] = None
