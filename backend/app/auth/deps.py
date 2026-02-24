from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.models.user import User
from app.auth.security import ALGORITHM, SECRET_KEY

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)

from app.models.session import UserSession
from sqlmodel import select

async def get_current_user(
    token: str = Depends(reusable_oauth2),
    session: AsyncSession = Depends(get_session)
) -> User:
    try:
        # print(f"DEBUG: Validating token: {token[:10]}...")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = payload.get("sub")
        jti = payload.get("jti")
        
        if token_data is None:
             print("DEBUG: Token data (sub) is None")
             raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )
    except (JWTError, ValidationError) as e:
        print(f"DEBUG: Token validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    # Check Session if JTI exists
    if jti:
        result = await session.exec(select(UserSession).where(UserSession.token_jti == jti))
        user_session = result.first()
        
        if not user_session or not user_session.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session revoked or expired",
            )
        
        # Update last active
        from datetime import datetime
        user_session.last_active_at = datetime.utcnow()
        session.add(user_session)
        await session.commit()

    # token_data is user_id
    from sqlalchemy.orm import selectinload
    from app.models.role import Role
    
    query = select(User).where(User.id == int(token_data)).options(
        selectinload(User.roles).selectinload(Role.permissions)
    )
    result = await session.exec(query)
    user = result.first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
