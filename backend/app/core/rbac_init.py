import asyncio
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from app.db import get_session, engine
from app.models.role import Role, Permission, RolePermission
from app.models.user import User
from app.models.user_role import UserRole
# from app.core.logger import get_logger # Optional if needed

ROLES_PERMISSIONS = {
    "admin": [
        "dashboard.view",
        "users.view",
        "users.create",
        "users.edit",
        "users.delete",
        "billing.view",
        "billing.edit",
        "subscription.view",
        "usage.view",
        "roles.manage",
        "cache.view",
        "plans.view",
        "exchange_rates.view",
        "supported_domains.view",
        "licenses.view",
        "settings.view",
    ],
    "staff_manager": [
        "dashboard.view",
        "users.view",
        "users.create",
        "users.edit",
        "users.delete",
    ],
    "staff_viewer": [
        "dashboard.view",
        "users.view",
    ],
    "extension_user": [
        "account.view",
        "subscription.view",
        "usage.view",
        "api_keys.view",
    ]
}

async def seed_rbac():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        print("Seeding RBAC...")
        
        # 1. Create Permissions
        all_permissions = {}
        for role_code, perms in ROLES_PERMISSIONS.items():
            for perm_code in perms:
                if perm_code not in all_permissions:
                    # Check if exists
                    result = await session.exec(select(Permission).where(Permission.code == perm_code))
                    existing_perm = result.first()
                    if not existing_perm:
                        new_perm = Permission(code=perm_code, description=f"Permission {perm_code}")
                        session.add(new_perm)
                        await session.commit()
                        await session.refresh(new_perm)
                        all_permissions[perm_code] = new_perm
                    else:
                        all_permissions[perm_code] = existing_perm

        # 2. Create Roles and Assign Permissions
        for role_code, perms in ROLES_PERMISSIONS.items():
            result = await session.exec(select(Role).where(Role.code == role_code))
            role = result.first()
            if not role:
                role = Role(code=role_code, name=role_code.replace("_", " ").title())
                session.add(role)
                await session.commit()
                await session.refresh(role)
                print(f"Created role: {role.name}")
            
            # Assign permissions
            current_perms = await session.exec(select(RolePermission).where(RolePermission.role_id == role.id))
            current_perm_ids = {rp.permission_id for rp in current_perms.all()}

            for perm_code in perms:
                perm = all_permissions[perm_code]
                if perm.id not in current_perm_ids:
                    rp = RolePermission(role_id=role.id, permission_id=perm.id)
                    session.add(rp)
                    current_perm_ids.add(perm.id)
            
            await session.commit()
        
        # 3. Create Super Admin User
        from app.auth.security import get_password_hash
        admin_email = "admin@example.com"
        result = await session.exec(select(User).where(User.email == admin_email))
        if not result.first():
            print("Creating Super Admin user...")
            hashed_pw = get_password_hash("password") # Change in production
            # Find admin role
            r_res = await session.exec(select(Role).where(Role.code == "admin"))
            admin_role = r_res.first()
            
            su_user = User(
                email=admin_email,
                hashed_password=hashed_pw,
                name="Super Admin",
                is_super_admin=True,
                role="admin" # Legacy field
            )
            session.add(su_user)
            await session.commit()
            await session.refresh(su_user)
            
            if admin_role:
                ur = UserRole(user_id=su_user.id, role_id=admin_role.id)
                session.add(ur)
                await session.commit()
            print("Super Admin created: admin@example.com / password")
        
        print("RBAC Seeding Complete.")

if __name__ == "__main__":
    asyncio.run(seed_rbac())
