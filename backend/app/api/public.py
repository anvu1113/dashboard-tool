from fastapi import APIRouter, Depends, Response
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.models.supported_domain import SupportedDomain, SupportedDomainRead
from app.models.currency_rate import CurrencyRate, CurrencyRateRead
from datetime import timedelta
from app.services.cache_manager import cache_manager

router = APIRouter()

# Register cache on module load
CACHE_NAME = "supported_domains"
cache_manager.register_cache(CACHE_NAME, timedelta(weeks=1))

# Register cache for exchange rates
CACHE_NAME_RATES = "exchange_rates"
cache_manager.register_cache(CACHE_NAME_RATES, timedelta(hours=1))


@router.get("/supported-domains", response_model=list[SupportedDomainRead])
async def get_public_supported_domains(
    response: Response,
    session: AsyncSession = Depends(get_session)
):
    # Set HTTP Cache-Control header for client-side caching (1 week)
    response.headers["Cache-Control"] = "public, max-age=604800"
    
    # Check server-side cache
    cached_data = cache_manager.get(CACHE_NAME)
    if cached_data is not None:
        # LOG: Cache hit
        print(f"🔵 CACHE HIT - Returning {len(cached_data)} domains from cache")
        for domain in cached_data:
            print(f"   → {domain.domain}: source={domain.source_language}, target={domain.target_language}")
        return cached_data

    # Fetch from DB
    query = select(SupportedDomain).where(SupportedDomain.is_active == True)
    result = await session.exec(query)
    domains = result.all()
    
    # LOG: Fresh data from DB
    print(f"🟢 DB FETCH - Retrieved {len(domains)} domains")
    for domain in domains:
        print(f"   → {domain.domain}: source={domain.source_language}, target={domain.target_language}")
    
    # Update cache
    cache_manager.set(CACHE_NAME, domains)
    
    return domains


@router.get("/exchange-rates", response_model=list[CurrencyRateRead])
async def get_public_exchange_rates(
    response: Response,
    session: AsyncSession = Depends(get_session),
    currency_codes: str = None
):
    """
    Public API to get current exchange rates (cached for 24 hours)
    
    Args:
        currency_codes: Optional comma-separated list of currency codes to filter
                       Example: ?currency_codes=USD,EUR,JPY
    """
    response.headers["Cache-Control"] = "public, max-age=3600"
    
    # Parse currency codes if provided
    codes_list = None
    if currency_codes:
        codes_list = [code.strip().upper() for code in currency_codes.split(',') if code.strip()]
    
    # If filtering by codes, skip cache and query directly
    if codes_list:
        print(f"🔍 FILTER - Querying for specific currency codes: {codes_list}")
        query = select(CurrencyRate).where(
            CurrencyRate.currency_code.in_(codes_list)
        ).order_by(CurrencyRate.currency_code)
        result = await session.exec(query)
        rates = result.all()
        print(f"✓ Found {len(rates)} matching rates")
        return rates
    
    # No filter - use cache for all rates
    cached_data = cache_manager.get(CACHE_NAME_RATES)
    if cached_data is not None:
        print(f"🔵 CACHE HIT - Returning {len(cached_data)} exchange rates from cache")
        return cached_data
    
    # Fetch all from DB
    query = select(CurrencyRate).order_by(CurrencyRate.currency_code)
    result = await session.exec(query)
    rates = result.all()
    
    print(f"🟢 DB FETCH - Retrieved {len(rates)} exchange rates")
    
    # Update cache
    cache_manager.set(CACHE_NAME_RATES, rates)
    
    return rates

