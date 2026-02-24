from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.db import get_session
from app.models.user import User, UserCreate, UserRead
from app.auth.security import get_password_hash, verify_password, create_access_token
from app.auth.deps import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register", response_model=dict)
async def register(user_in: UserCreate, request: Request, session: AsyncSession = Depends(get_session)):
    # Check existing
    result = await session.exec(select(User).where(User.email == user_in.email))
    existing_user = result.first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    user = User(
        email=user_in.email,
        name=user_in.name,
        phone=user_in.phone,
        hashed_password=get_password_hash(user_in.password),
        role="user"
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)

    # Auto login
    # Auto login with session
    import uuid
    from app.models.session import UserSession
    jti = str(uuid.uuid4())
    user_session = UserSession(
        user_id=user.id,
        token_jti=jti,
        ip_address=request.client.host if request.client else None,
        user_agent=request.headers.get("user-agent")
    )
    session.add(user_session)
    await session.commit()

    access_token = create_access_token(user.id, jti=jti)
    return {
        "success": True,
        "message": "Đăng ký thành công",
        "data": {
            "user": user,
            "token": access_token,
            "token_type": "Bearer"
        }
    }

@router.post("/login", response_model=dict)
async def login(
    login_data: dict, # Receiving JSON body {email, password}
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    email = login_data.get("email")
    password = login_data.get("password")

    # Eager load roles and permissions
    from sqlalchemy.orm import selectinload
    from app.models.role import Role
    
    query = select(User).where(User.email == email).options(
        selectinload(User.roles).selectinload(Role.permissions)
    )
    result = await session.exec(query)
    user = result.first()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Email hoặc mật khẩu không đúng")
    
    # Create Session
    import uuid
    from app.models.session import UserSession
    
    jti = str(uuid.uuid4())
    user_session = UserSession(
        user_id=user.id,
        token_jti=jti,
        ip_address=request.client.host if request.client else None,
        user_agent=request.headers.get("user-agent")
    )
    session.add(user_session)
    await session.commit()

    access_token = create_access_token(user.id, jti=jti)
    
    # Flatten permissions
    permissions = set()
    roles = []
    if user.is_super_admin:
        permissions.add("*") # Or handle super admin logic in FE differently. 
        # Typically super admin has all. For now let's just mark it.
        # Actually user spec says backend checks permissions.
        # But for FE display, maybe we send a special flag or all permissions?
        # Let's send all existing permissions if super admin? Or just "*" and FE handles it?
        # FE Helper: if user.is_super_admin return true.
        roles.append("super_admin")
    
    if user.roles:
        for role in user.roles:
            roles.append(role.code)
            if role.permissions:
                for perm in role.permissions:
                    permissions.add(perm.code)
    
    return {
        "success": True, 
        "data": {
            "token": access_token,
            "token_type": "bearer",
            "user": user,
            "roles": roles,
            "permissions": list(permissions)
        }
    }

@router.get("/me", response_model=dict)
async def read_users_me(current_user: User = Depends(get_current_user)):
    # Current user from deps already has roles/permissions loaded if we updated deps.py correctly
    # deps.py get_current_user was updated to use selectinload.
    
    permissions = set()
    roles = []
    if current_user.is_super_admin:
        roles.append("super_admin")
    
    if current_user.roles:
        for role in current_user.roles:
            roles.append(role.code)
            if role.permissions:
                for perm in role.permissions:
                    permissions.add(perm.code)

    return {
        "success": True,
        "data": {
            "user": current_user,
            "roles": roles,
            "permissions": list(permissions)
        }
    }
