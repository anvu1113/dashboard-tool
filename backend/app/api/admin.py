from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.auth.deps import get_current_user
from app.models.user import User
from app.models.subscription import Plan, PlanFeature, Subscription

router = APIRouter()

# --- Plans ---
@router.get("/plans")
async def get_plans(session: AsyncSession = Depends(get_session), admin: User = Depends(get_current_user)):
    # Check admin role? For now skip
    query = select(Plan)
    result = await session.exec(query)
    plans = result.all()
    
    # Populate features manual
    final_plans = []
    for p in plans:
         # fetch features
         q_f = select(PlanFeature).where(PlanFeature.plan_id == p.id)
         res_f = await session.exec(q_f)
         p_features = res_f.all()
         
         # Convert to dict representation
         p_dict = p.dict()
         p_dict['features'] = p_features
         final_plans.append(p_dict)
         
    return final_plans

@router.post("/plans")
async def create_plan(plan_data: dict, session: AsyncSession = Depends(get_session), admin: User = Depends(get_current_user)):
    # Basic implementation
    new_plan = Plan(
        code=plan_data['code'],
        name=plan_data['name'],
        price=plan_data['price'],
        billing_cycle=plan_data['billing_cycle'],
        is_active=plan_data.get('is_active', True)
    )
    session.add(new_plan)
    await session.commit()
    await session.refresh(new_plan)

    features = plan_data.get('features', [])
    for f in features:
        new_f = PlanFeature(plan_id=new_plan.id, key=f['key'], value=f['value'])
        session.add(new_f)
    
    await session.commit()
    return new_plan

@router.delete("/plans/{plan_id}")
async def delete_plan(plan_id: int, session: AsyncSession = Depends(get_session), admin: User = Depends(get_current_user)):
    plan = await session.get(Plan, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    await session.delete(plan)
    await session.commit()
    return {"ok": True}

# --- Subscriptions ---
@router.get("/subscriptions")
async def get_subscriptions(session: AsyncSession = Depends(get_session), admin: User = Depends(get_current_user)):
    query = select(Subscription) # add join user/plan
    result = await session.exec(query)
    return result.all()
