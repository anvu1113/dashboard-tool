from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.auth.deps import get_current_user
from app.auth.permission import RequirePermission
from app.models.user import User
from app.models.role import Role, Permission, RolePermission, RoleRead
from typing import List
from sqlalchemy.orm import selectinload

router = APIRouter()

@router.get("/roles", response_model=List[RoleRead], dependencies=[Depends(RequirePermission(["roles.view", "users.create", "users.edit"]))])
async def get_roles(session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    # Accessible by roles.view OR users.create/edit (to populate dropdowns)
    # Eager load permissions
    query = select(Role).options(selectinload(Role.permissions))
    result = await session.exec(query)
    return result.all()

@router.get("/permissions", response_model=List[Permission], dependencies=[Depends(RequirePermission(["roles.manage", "roles.view"]))])
async def get_permissions(session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    query = select(Permission)
    result = await session.exec(query)
    return result.all()

@router.post("/roles", response_model=Role, dependencies=[Depends(RequirePermission("roles.manage"))])
async def create_role(role_data: Role, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    # usage: role_data is Role model (validated)
    # check unique code
    res = await session.exec(select(Role).where(Role.code == role_data.code))
    if res.first():
        raise HTTPException(status_code=400, detail="Role code already exists")
    
    session.add(role_data)
    await session.commit()
    await session.refresh(role_data)
    return role_data

@router.put("/roles/{role_id}", response_model=Role, dependencies=[Depends(RequirePermission("roles.manage"))])
async def update_role(role_id: int, role_in: dict, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    # user role_in dict for now
    # eager load permissions to return full object
    query = select(Role).where(Role.id == role_id).options(selectinload(Role.permissions))
    result = await session.exec(query)
    db_role = result.first()
    
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    for key, value in role_in.items():
        if key in ['code', 'name', 'description']:
            setattr(db_role, key, value)
            
    session.add(db_role)
    await session.commit()
    await session.refresh(db_role)
    return db_role

@router.delete("/roles/{role_id}", dependencies=[Depends(RequirePermission("roles.manage"))])
async def delete_role(role_id: int, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    db_role = await session.get(Role, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    # Check if any users have this role?
    # ... logic skipped for now
    # Also delete RolePermission links? Cascade should handle if configured, otherwise manual
    # For many-to-many, usually we need to clear links first if no cascade
    
    await session.delete(db_role)
    await session.commit()
    return {"ok": True}

from fastapi import Body

@router.post("/roles/{role_id}/permissions", dependencies=[Depends(RequirePermission("roles.manage"))])
async def update_role_permissions(
    role_id: int, 
    permission_ids: List[int] = Body(...), 
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_current_user)
):
    print(f"DEBUG: update_role_permissions called for role_id={role_id}. Permission IDs received: {permission_ids}")
    # Get Role
    role = await session.get(Role, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    # Clear existing permissions
    # Delete from RolePermission where role_id == role_id
    from sqlmodel import delete
    await session.exec(delete(RolePermission).where(RolePermission.role_id == role_id))
    
    # Add new permissions
    for perm_id in permission_ids:
        print(f"DEBUG: Adding permission {perm_id} to role {role_id}")
        rp = RolePermission(role_id=role_id, permission_id=perm_id)
        session.add(rp)
    
    await session.commit()
    print("DEBUG: Commit successful")
    return {"ok": True}

@router.post("/permissions", response_model=Permission, dependencies=[Depends(RequirePermission("roles.manage"))])
async def create_permission(perm_data: Permission, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    res = await session.exec(select(Permission).where(Permission.code == perm_data.code))
    if res.first():
        raise HTTPException(status_code=400, detail="Permission code already exists")
    
    session.add(perm_data)
    await session.commit()
    await session.refresh(perm_data)
    return perm_data

@router.put("/permissions/{permission_id}", response_model=Permission, dependencies=[Depends(RequirePermission("roles.manage"))])
async def update_permission(permission_id: int, perm_in: dict, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    db_perm = await session.get(Permission, permission_id)
    if not db_perm:
        raise HTTPException(status_code=404, detail="Permission not found")
        
    for key, value in perm_in.items():
        if key in ['code', 'description']:
            setattr(db_perm, key, value)
            
    session.add(db_perm)
    await session.commit()
    await session.refresh(db_perm)
    return db_perm

@router.delete("/permissions/{permission_id}", dependencies=[Depends(RequirePermission("roles.manage"))])
async def delete_permission(permission_id: int, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    db_perm = await session.get(Permission, permission_id)
    if not db_perm:
        raise HTTPException(status_code=404, detail="Permission not found")
        
    # Delete RolePermission links first
    from sqlmodel import delete
    await session.exec(delete(RolePermission).where(RolePermission.permission_id == permission_id))
    
    await session.delete(db_perm)
    await session.commit()
    return {"ok": True}
