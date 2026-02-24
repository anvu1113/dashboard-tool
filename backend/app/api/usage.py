from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, func, desc
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.auth.deps import get_current_user
from app.auth.permission import RequirePermission
from app.models.user import User
from app.models.translation_log import TranslationLog
from typing import List, Optional
from datetime import datetime, date

router = APIRouter()

@router.get("/", dependencies=[Depends(RequirePermission("usage.view"))])
async def get_usage_logs(
    page: int = 1,
    limit: int = 20,
    date_filter: Optional[date] = Query(None, alias="date"),
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_current_user)
):
    skip = (page - 1) * limit
    
    # Base query
    query = select(TranslationLog, User.email).join(User, isouter=True).order_by(desc(TranslationLog.created_at))
    
    if date_filter:
        # Filter by date (start of day to end of day)
        # simplistic: cast to date or range
        # For simplicity in SQLModel/SQLAlchemy with sqlite/pg compatibility:
        # We can filter where created_at >= date and created_at < date + 1 day
        start_of_day = datetime.combine(date_filter, datetime.min.time())
        end_of_day = datetime.combine(date_filter, datetime.max.time())
        query = query.where(TranslationLog.created_at >= start_of_day, TranslationLog.created_at <= end_of_day)

    # Count total for pagination UI
    count_query = select(func.count()).select_from(TranslationLog)
    if date_filter:
        start_of_day = datetime.combine(date_filter, datetime.min.time())
        end_of_day = datetime.combine(date_filter, datetime.max.time())
        count_query = count_query.where(TranslationLog.created_at >= start_of_day, TranslationLog.created_at <= end_of_day)
    total_result = await session.exec(count_query)
    total_count = total_result.one()
    
    query = query.offset(skip).limit(limit)
    result = await session.exec(query)
    logs = result.all()
    
    # Format response
    data = []
    for log, email in logs:
        data.append({
            "id": log.id,
            "created_at": log.created_at,
            "user_email": email or "Unknown/System",
            "action": log.action,
            "engine": log.engine,
            "source_lang": log.source_lang,
            "target_lang": log.target_lang,
            "char_count": log.char_count,
            "latency_ms": log.latency_ms,
            "cost_estimate": log.cost_estimate
        })
    
    import math
    total_pages = math.ceil(total_count / limit) if total_count > 0 else 1
        
    return {
        "data": data,
        "total": total_count,
        "page": page,
        "limit": limit,
        "total_pages": total_pages
    }
