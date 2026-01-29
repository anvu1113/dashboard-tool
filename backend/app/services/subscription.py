from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from datetime import datetime
from app.models.subscription import Subscription, Plan, UsageLog, PlanFeature
from app.models.user import User

class SubscriptionService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_active_subscription(self, user: User) -> Subscription | None:
        # Get active sub
        query = select(Subscription).where(
            Subscription.user_id == user.id,
            Subscription.status == "active"
        ).order_by(Subscription.starts_at.desc())
        
        result = await self.session.exec(query)
        subscription = result.first()

        # Check expiration
        if subscription:
             if subscription.ends_at and subscription.ends_at < datetime.utcnow():
                 return None 
             return subscription
        
        # If no subscription, assign FREE plan
        # We need to fetch Free plan first
        query_plan = select(Plan).where(Plan.code == "free")
        result_plan = await self.session.exec(query_plan)
        free_plan = result_plan.first()

        if free_plan:
            new_sub = Subscription(
                user_id=user.id,
                plan_id=free_plan.id,
                starts_at=datetime.utcnow(),
                status="active"
            )
            self.session.add(new_sub)
            await self.session.commit()
            await self.session.refresh(new_sub)
            return new_sub

        return None

    async def can_use_feature(self, user: User, feature_key: str) -> bool:
        subscription = await self.get_active_subscription(user)
        if not subscription:
            return False
        
        # Eager load plan features? SQLModel relationships are lazy by default or no?
        # We need to fetch plan features
        # Assuming eager load or explicit fetch
        # Let's fetch feature
        query = select(PlanFeature).where(
            PlanFeature.plan_id == subscription.plan_id,
            PlanFeature.key == feature_key
        )
        result = await self.session.exec(query)
        feature = result.first()

        if not feature:
            return False
        
        if feature.value == "true":
            return True
        if feature.value == "false":
            return False
        
        try:
            limit = int(feature.value)
            if limit > 0:
                # Check daily usage
                today_str = datetime.utcnow().strftime('%Y-%m-%d')
                query_log = select(UsageLog).where(
                    UsageLog.user_id == user.id,
                    UsageLog.feature_key == feature_key,
                    UsageLog.date == today_str
                )
                result_log = await self.session.exec(query_log)
                log = result_log.first()
                
                usage = log.count if log else 0
                return usage < limit
        except ValueError:
            pass
            
        return True # Default allow if not bool/int? Or False?

    async def increment_usage(self, user: User, feature_key: str):
        today_str = datetime.utcnow().strftime('%Y-%m-%d')
        query_log = select(UsageLog).where(
            UsageLog.user_id == user.id,
            UsageLog.feature_key == feature_key,
            UsageLog.date == today_str
        )
        result_log = await self.session.exec(query_log)
        log = result_log.first()

        if not log:
            log = UsageLog(
                user_id=user.id,
                feature_key=feature_key,
                count=0,
                date=today_str
            )
            self.session.add(log)
        
        log.count += 1
        await self.session.commit()
        await self.session.refresh(log)
        return log.count
