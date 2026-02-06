from fastapi import FastAPI
from app.db import init_db
from app.api import auth, subscription, admin, translation

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow Extension access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.middleware.logging_middleware import RequestLoggingMiddleware
app.add_middleware(RequestLoggingMiddleware)


@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "FastAPI Dashboard Backend"}

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(subscription.router, prefix="/api/auth", tags=["subscription"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
from app.api import supported_domains
app.include_router(supported_domains.router, prefix="/api/admin/supported-domains", tags=["supported-domains"])
app.include_router(translation.router, prefix="/api", tags=["translation"])
from app.api import session as session_api
app.include_router(session_api.router, prefix="/api", tags=["sessions"])

from app.api import public
app.include_router(public.router, prefix="/api", tags=["public"])

from app.api import cache as cache_api
app.include_router(cache_api.router, prefix="/api/admin/cache", tags=["cache"])
