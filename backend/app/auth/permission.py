from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.auth.deps import get_current_user

from typing import List, Union

class RequirePermission:
    def __init__(self, permission_code: Union[str, List[str]]):
        self.permission_codes = [permission_code] if isinstance(permission_code, str) else permission_code

    async def __call__(self, user: User = Depends(get_current_user)) -> User:
        if user.is_super_admin:
            return user
        
        # Check permissions
        has_permission = False
        if user.roles:
            for role in user.roles:
                if role.permissions:
                    for perm in role.permissions:
                        if perm.code in self.permission_codes:
                            has_permission = True
                            break
                if has_permission:
                    break
        
        if not has_permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission denied: {self.permission_codes} required"
            )
        return user
