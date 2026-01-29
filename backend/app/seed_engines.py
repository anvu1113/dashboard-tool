import asyncio
from app.db import get_session, engine
from app.models.subscription import Plan, PlanFeature
from sqlmodel import select, Session
import argostranslate.package
import argostranslate.translate

def install_argos_models():
    print("Updating Argos package index...")
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    
    pairs = [('en', 'vi'), ('vi', 'en')]
    
    for from_code, to_code in pairs:
        print(f"Checking model {from_code} -> {to_code}...")
        package_to_install = next(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            ), None
        )
        if package_to_install:
            print(f"Downloading & Installing {from_code} -> {to_code}...")
            argostranslate.package.install_from_path(package_to_install.download())
        else:
            print(f"Package {from_code} -> {to_code} not found.")

async def seed_engines():
    # Install models first
    try:
        install_argos_models()
    except Exception as e:
        print(f"Failed to install models: {e}")

    print("Seeding Translation Engine features...")
    async with engine.begin() as conn:
        # We need a session
        from sqlalchemy.orm import sessionmaker
        from sqlmodel.ext.asyncio.session import AsyncSession
        async_session = sessionmaker(
            engine, class_=AsyncSession, expire_on_commit=False
        )
        async with async_session() as session:
            # Get all plans
            result = await session.exec(select(Plan))
            plans = result.all()
            
            for plan in plans:
                print(f"Checking plan: {plan.name}")
                # Check if feature exists
                query = select(PlanFeature).where(
                    PlanFeature.plan_id == plan.id,
                    PlanFeature.key == "engine_argos"
                )
                existing = await session.exec(query)
                if not existing.first():
                    print(f"Adding engine_argos to {plan.name}")
                    feature = PlanFeature(
                        plan_id=plan.id,
                        key="engine_argos",
                        value="true"
                    )
                    session.add(feature)
            
            await session.commit()
            print("Seeding complete.")

if __name__ == "__main__":
    asyncio.run(seed_engines())
