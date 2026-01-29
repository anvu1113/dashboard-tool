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

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "FastAPI Dashboard Backend"}

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(subscription.router, prefix="/api/auth", tags=["subscription"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(translation.router, prefix="/api", tags=["translation"])
from app.api import session as session_api
app.include_router(session_api.router, prefix="/api", tags=["sessions"])
