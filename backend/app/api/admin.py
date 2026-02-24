from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.auth.deps import get_current_user
from app.models.user import User, UserCreate, UserRead, UserUpdate
from app.models.subscription import Plan, PlanFeature, Subscription
from app.auth.permission import RequirePermission
from app.models.role import Role
from app.models.user_role import UserRole
from app.auth.security import get_password_hash
from typing import List
from sqlalchemy.orm import selectinload

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

# --- Users ---

@router.get("/users", response_model=List[UserRead], dependencies=[Depends(RequirePermission("users.view"))])
async def get_users(
    skip: int = 0,
    limit: int = 20,
    search: str = None,
    role: str = None,
    session: AsyncSession = Depends(get_session),
    admin: User = Depends(get_current_user)
):
    query = select(User).options(selectinload(User.roles))
    if search:
        query = query.where(User.email.contains(search) | User.name.contains(search))
    if role:
        # Filter by role... complicated with many-to-many?
        # Or filter by legacy role string?
        # Assuming legacy string for now or join?
        # If legacy 'role' column is still used for basic filter, keep it.
        # But if checking permissions, we should check UserRole.
        # Let's keep existing logic: User.role == role if "role" param is passed
        query = query.where(User.role == role)
    
    query = query.offset(skip).limit(limit)
    result = await session.exec(query)
    return result.all()

@router.post("/users", response_model=UserRead, dependencies=[Depends(RequirePermission("users.create"))])
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_session),
    admin: User = Depends(get_current_user)
):
    # Check if user exists
    q = select(User).where(User.email == user_in.email)
    res = await session.exec(q)
    if res.first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = get_password_hash(user_in.password)
    user_data = user_in.dict()
    del user_data['password']
    user_data['hashed_password'] = hashed_pw
    
    # Handle Role Assignment: use 'role' field to find Role and assign
    role_code = user_data.get('role')
    role_obj = None
    if role_code:
        role_res = await session.exec(select(Role).where(Role.code == role_code))
        role_obj = role_res.first()
        if not role_obj:
            # Fallback or error? defaulting to user role if not found?
            # Or assume valid code.
            pass

    db_user = User(**user_data) # use unpack to avoid validation issues? or model_validate
    # db_user = User.model_validate(user_data) # model_validate expects fields matching model
    
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    
    if role_obj:
        # Create UserRole
        user_role = UserRole(user_id=db_user.id, role_id=role_obj.id)
        session.add(user_role)
        await session.commit()

    return db_user

@router.put("/users/{user_id}", response_model=UserRead, dependencies=[Depends(RequirePermission("users.edit"))])
async def update_user(
    user_id: int,
    user_in: UserUpdate,
    session: AsyncSession = Depends(get_session),
    admin: User = Depends(get_current_user)
):
    from sqlalchemy.orm import selectinload
    # Load user with roles to update them
    # db_user = await session.get(User, user_id) 
    # Need to load relationship if we want to update it properly?
    # For now, just deleting existing user_role and adding new one is simplest for 1-1 mapping simulation
    
    db_user = await session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_data = user_in.dict(exclude_unset=True)
    if 'password' in user_data and user_data['password']:
        hashed_pw = get_password_hash(user_data['password'])
        user_data['hashed_password'] = hashed_pw
        del user_data['password']
        
    for key, value in user_data.items():
        setattr(db_user, key, value)
        
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    
    # If role changed, update UserRole
    if 'role' in user_data:
        new_role_code = user_data['role']
        # Find role
        r_res = await session.exec(select(Role).where(Role.code == new_role_code))
        role_obj = r_res.first()
        
        if role_obj:
            # Remove existing roles?
            # efficient way: delete from UserRole where user_id = ...
            await session.exec(select(UserRole).where(UserRole.user_id == user_id))
            # Delete execution needs explicit delete stmt
            from sqlmodel import delete
            stmt = delete(UserRole).where(UserRole.user_id == user_id)
            await session.exec(stmt)
            
            # Add new role
            ur = UserRole(user_id=user_id, role_id=role_obj.id)
            session.add(ur)
            await session.commit()

    return db_user

@router.delete("/users/{user_id}", dependencies=[Depends(RequirePermission("users.delete"))])
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(get_session),
    admin: User = Depends(get_current_user)
):
    # Prevent deleting self
    if user_id == admin.id:
         raise HTTPException(status_code=400, detail="Cannot delete yourself")
         
    db_user = await session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    from app.models.session import UserSession
    from sqlmodel import delete
    
    # Delete sessions
    stmt_session = delete(UserSession).where(UserSession.user_id == user_id)
    await session.exec(stmt_session)
    
    # Delete user roles
    stmt_role = delete(UserRole).where(UserRole.user_id == user_id)
    await session.exec(stmt_role)
        
    await session.delete(db_user)
    await session.commit()
    return {"ok": True}
