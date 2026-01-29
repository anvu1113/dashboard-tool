from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.auth.deps import get_current_user
from app.models.user import User
from app.services.subscription import SubscriptionService

router = APIRouter()

@router.get("/me/subscription")
async def get_my_subscription(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    service = SubscriptionService(session)
    sub = await service.get_active_subscription(current_user)

    if not sub:
        return {
            "plan": "none",
            "expires_at": None,
            "features": {}
        }
    
    # Need to load plan and features
    await session.refresh(sub, ["plan"])
    # await session.refresh(sub.plan, ["features"]) 
    # SQLModel async relationship loading can be tricky, let's manual fetch if needed or trust lazy
    # But lazy doesn't work well in async without explicit await/refresh
    
    # Manual fetch features
    from sqlmodel import select
    from app.models.subscription import PlanFeature
    query = select(PlanFeature).where(PlanFeature.plan_id == sub.plan_id)
    features_Result = await session.exec(query)
    features = features_Result.all()

    feature_map = {f.key: f.value for f in features}

    return {
        "plan": sub.plan.code,
        "expires_at": sub.ends_at,
        "features": feature_map
    }
