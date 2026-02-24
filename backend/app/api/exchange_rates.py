from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from datetime import datetime
from app.db import get_session
from app.models.currency_rate import CurrencyRate, CurrencyRateRead, CurrencyRateCreate, CurrencyRateUpdate
from app.auth.deps import get_current_user
from app.models.user import User
from app.services.exchange_rate_fetcher import exchange_rate_fetcher
from app.services.cache_manager import cache_manager

router = APIRouter()


@router.get("/", response_model=list[CurrencyRateRead])
async def get_all_rates(
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Get all exchange rates (Admin only)"""
    query = select(CurrencyRate).order_by(CurrencyRate.currency_code)
    result = await session.exec(query)
    return result.all()


@router.post("/", response_model=CurrencyRateRead)
async def create_rate(
    rate: CurrencyRateCreate,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Create new currency rate"""
    # Check if currency_code already exists
    query = select(CurrencyRate).where(CurrencyRate.currency_code == rate.currency_code)
    result = await session.exec(query)
    existing = result.first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Currency code already exists")
    
    db_rate = CurrencyRate.model_validate(rate)
    session.add(db_rate)
    await session.commit()
    await session.refresh(db_rate)
    
    # Clear cache
    cache_manager.clear("exchange_rates")
    
    return db_rate


@router.put("/{rate_id}", response_model=CurrencyRateRead)
async def update_rate(
    rate_id: int,
    rate: CurrencyRateUpdate,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Update exchange rate"""
    query = select(CurrencyRate).where(CurrencyRate.id == rate_id)
    result = await session.exec(query)
    db_rate = result.first()
    
    if not db_rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    
    # Update fields
    update_data = rate.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_rate, key, value)
    
    db_rate.updated_at = datetime.utcnow()
    session.add(db_rate)
    await session.commit()
    await session.refresh(db_rate)
    
    # Clear cache
    cache_manager.clear("exchange_rates")
    
    return db_rate


@router.delete("/{rate_id}")
async def delete_rate(
    rate_id: int,
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Delete exchange rate"""
    query = select(CurrencyRate).where(CurrencyRate.id == rate_id)
    result = await session.exec(query)
    db_rate = result.first()
    
    if not db_rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    
    await session.delete(db_rate)
    await session.commit()
    
    # Clear cache
    cache_manager.clear("exchange_rates")
    
    return {"message": "Rate deleted successfully"}


@router.post("/sync")
async def sync_rates(
    session: AsyncSession = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """Manually trigger sync from Vietcombank API"""
    try:
        rates = await exchange_rate_fetcher.fetch_rates()
        await exchange_rate_fetcher.update_database(session, rates)
        
        # Clear cache
        cache_manager.clear("exchange_rates")
        
        return {
            "message": f"Successfully synced {len(rates)} exchange rates",
            "count": len(rates)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sync failed: {str(e)}")
