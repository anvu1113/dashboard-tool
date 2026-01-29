from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from .user import User

# --- Plan ---
class PlanBase(SQLModel):
    code: str = Field(unique=True, index=True)
    name: str
    price: int
    billing_cycle: str # monthly, yearly
    is_active: bool = True

class Plan(PlanBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    features: List["PlanFeature"] = Relationship(back_populates="plan")

class PlanRead(PlanBase):
    id: int
    features: List["PlanFeatureRead"] = []

# --- Plan Feature ---
class PlanFeatureBase(SQLModel):
    key: str
    value: str

class PlanFeature(PlanFeatureBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    plan_id: int = Field(foreign_key="plan.id")
    plan: Optional[Plan] = Relationship(back_populates="features")

class PlanFeatureRead(PlanFeatureBase):
    id: int

# Update forward refs
PlanRead.update_forward_refs()

# --- Subscription ---
class SubscriptionBase(SQLModel):
    status: str = "active"
    starts_at: datetime = Field(default_factory=datetime.utcnow)
    ends_at: Optional[datetime] = None

class Subscription(SubscriptionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    plan_id: int = Field(foreign_key="plan.id")
    
    plan: Optional[Plan] = Relationship()
    user: Optional[User] = Relationship()

# --- Usage Log ---
class UsageLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    feature_key: str
    count: int = 0
    date: str # YYYY-MM-DD
