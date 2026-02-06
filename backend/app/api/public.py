from fastapi import APIRouter, Depends, Response
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.models.supported_domain import SupportedDomain, SupportedDomainRead
from datetime import timedelta
from app.services.cache_manager import cache_manager

router = APIRouter()

# Register cache on module load
CACHE_NAME = "supported_domains"
cache_manager.register_cache(CACHE_NAME, timedelta(weeks=1))

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
