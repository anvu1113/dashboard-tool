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
    source_lang: str = "en" # Default to English
    engine: str = "auto" # default engine


from app.services.translation import get_translation_service
from app.services.translation_orchestrator import TranslationOrchestrator
from app.core.exceptions import PlanNotFoundException, QuotaExceededException, FeatureNotEnabledException, LanguageNotSupportedException

router = APIRouter()

@router.post("/translate")
async def translate(
    req: TranslateRequest,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    # Validation engine support
    # (Optional: check permission boolean here or let Orchestrator handle)
    
    orchestrator = TranslationOrchestrator(session, current_user)
    
    try:
        result = await orchestrator.translate(
            text=req.text,
            source=req.source_lang,
            target=req.target_lang,
            engine_id="auto", # Force BE to decide, ignore req.engine (often 'argos' from legacy ext)
            context="general" # Could add to req
        )
    except PlanNotFoundException:
        raise HTTPException(status_code=403, detail="Tài khoản chưa có gói dịch vụ. Vui lòng liên hệ hỗ trợ.")
    except QuotaExceededException:
         raise HTTPException(status_code=403, detail="Bạn đã dùng hết giới hạn dịch trong ngày cho gói hiện tại.")
    except FeatureNotEnabledException:
         raise HTTPException(status_code=403, detail="Gói cước của bạn không hỗ trợ tính năng hoặc engine dịch này.")
    except LanguageNotSupportedException as e:
         raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Orchestrator Error: {e}")
        raise HTTPException(status_code=500, detail="Lỗi hệ thống dịch: " + str(e))

    return {
        "original": req.text,
        "translated": result["translated"],
        "engine": result["engine"],
        "source": result["source"] # db, cache, or engine
    }
