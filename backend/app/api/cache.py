from fastapi import APIRouter, Depends
from app.auth.deps import get_current_user
from app.models.user import User
from app.services.cache_manager import cache_manager

router = APIRouter()

@router.get("/status")
async def get_cache_status(
    user: User = Depends(get_current_user)
):
    """Get status of all caches"""
    # TODO: Add admin role check
    return {
        "success": True,
        "data": cache_manager.get_all_status()
    }

@router.post("/clear/{cache_name}")
async def clear_cache(
    cache_name: str,
    user: User = Depends(get_current_user)
):
    """Clear specific cache"""
    # TODO: Add admin role check
    success = cache_manager.clear(cache_name)
    
    if not success:
        return {
            "success": False,
            "message": f"Cache '{cache_name}' not found"
        }
    
    return {
        "success": True,
        "message": f"Cache '{cache_name}' cleared successfully"
    }

@router.post("/clear-all")
async def clear_all_caches(
    user: User = Depends(get_current_user)
):
    """Clear all caches"""
    # TODO: Add admin role check
    cache_manager.clear_all()
    
    return {
        "success": True,
        "message": "All caches cleared successfully"
    }
