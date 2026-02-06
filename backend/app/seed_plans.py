import asyncio
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.db import engine
from app.models.subscription import Plan, PlanFeature

async def seed_plans():
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    
    async with async_session() as session:
        print("Seeding Plans...")
        
        # 1. Free Plan
        result = await session.exec(select(Plan).where(Plan.code == "free"))
        free_plan = result.first()
        if not free_plan:
            print("Creating Free Plan...")
            free_plan = Plan(code="free", name="Free Plan", price=0, billing_cycle="forever")
            session.add(free_plan)
            await session.commit()
            await session.refresh(free_plan)
            
            # Features
            features = [
                PlanFeature(plan_id=free_plan.id, key="translate_requests", value="100"),
                PlanFeature(plan_id=free_plan.id, key="use_ai_engine", value="false"),
                PlanFeature(plan_id=free_plan.id, key="engine_argos", value="true")
            ]
            for f in features:
                session.add(f)
            await session.commit()
        else:
            print("Free Plan already exists.")
            
        # 2. Pro Plan
        result = await session.exec(select(Plan).where(Plan.code == "pro"))
        pro_plan = result.first()
        if not pro_plan:
            print("Creating Pro Plan...")
            pro_plan = Plan(code="pro", name="Pro Plan", price=200000, billing_cycle="monthly")
            session.add(pro_plan)
            await session.commit()
            await session.refresh(pro_plan)
            
            # Features
            features = [
                PlanFeature(plan_id=pro_plan.id, key="translate_requests", value="5000"),
                PlanFeature(plan_id=pro_plan.id, key="use_ai_engine", value="true"),
                PlanFeature(plan_id=pro_plan.id, key="engine_argos", value="true")
            ]
            for f in features:
                session.add(f)
            await session.commit()
        else:
             print("Pro Plan already exists.")
             
        print("Seeding Plans Completed.")

if __name__ == "__main__":
    asyncio.run(seed_plans())
