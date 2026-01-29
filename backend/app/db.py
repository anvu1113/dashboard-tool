from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
import os

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

import asyncio

async def init_db():
    retries = 5
    while retries > 0:
        try:
            async with engine.begin() as conn:
                # await conn.run_sync(SQLModel.metadata.drop_all)
                await conn.run_sync(SQLModel.metadata.create_all)
            print("Database connected and initialized.")
            break
        except Exception as e:
            print(f"Database connection failed, retrying in 5s... ({retries} left)")
            print(e)
            retries -= 1
            await asyncio.sleep(5)
            if retries == 0:
                raise e

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
