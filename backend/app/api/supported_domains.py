from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.auth.deps import get_current_user
from app.models.user import User
from app.models.supported_domain import SupportedDomain, SupportedDomainCreate, SupportedDomainRead, SupportedDomainUpdate

router = APIRouter()

@router.get("/", response_model=list[SupportedDomainRead])
async def get_supported_domains(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_current_user)
):
    # TODO: Add admin check if needed
    query = select(SupportedDomain)
    result = await session.exec(query)
    return result.all()

@router.post("/", response_model=SupportedDomainRead)
async def create_supported_domain(
    domain_in: SupportedDomainCreate,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_current_user)
):
    # Check if exists
    query = select(SupportedDomain).where(SupportedDomain.domain == domain_in.domain)
    result = await session.exec(query)
    if result.first():
        raise HTTPException(status_code=400, detail="Domain already exists")
    
    db_obj = SupportedDomain.from_orm(domain_in)
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

@router.put("/{domain_id}", response_model=SupportedDomainRead)
async def update_supported_domain(
    domain_id: int,
    domain_in: SupportedDomainUpdate,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_current_user)
):
    db_obj = await session.get(SupportedDomain, domain_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Domain not found")
    
    hero_data = domain_in.dict(exclude_unset=True)
    for key, value in hero_data.items():
        setattr(db_obj, key, value)
        
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

@router.delete("/{domain_id}")
async def delete_supported_domain(
    domain_id: int,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_current_user)
):
    db_obj = await session.get(SupportedDomain, domain_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Domain not found")
        
    await session.delete(db_obj)
    await session.commit()
    return {"ok": True}
