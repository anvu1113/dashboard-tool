from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.auth.deps import get_current_user
from app.models.user import User
from app.services.subscription import SubscriptionService
from pydantic import BaseModel

class TranslateRequest(BaseModel):
    text: str
    target_lang: str
    engine: str = "argos" # default engine

from app.services.translation import get_translation_service

router = APIRouter()

@router.post("/translate")
async def translate(
    req: TranslateRequest,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    # Validation engine support
    # (Optional: check permission boolean here or let Orchestrator handle)
    
    from app.services.translation_orchestrator import TranslationOrchestrator
    orchestrator = TranslationOrchestrator(session, current_user)
    
    try:
        result = await orchestrator.translate(
            text=req.text,
            source='en', # Default source, ideally from req
            target=req.target_lang, # Assuming TranslateRequest has this
            engine_id=req.engine,
            context="general" # Could add to req
        )
    except Exception as e:
        if "Quota" in str(e):
             raise HTTPException(status_code=403, detail="Daily translation quota reached")
        print(f"Orchestrator Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "original": req.text,
        "translated": result["translated"],
        "engine": result["engine"],
        "source": result["source"] # db, cache, or engine
    }
