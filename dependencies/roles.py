from fastapi import Depends, HTTPException
from models.enums import UserRole
from models.users import User
from dependencies.auth import get_current_user

def require_roles(*allowed_roles: UserRole):
    async def checker(user: User = Depends(get_current_user)) -> User:
        if user.role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return checker

require_admin = require_roles(UserRole.admin)
require_employer = require_roles(UserRole.employer)
require_candidate = require_roles(UserRole.candidate)
require_employer_or_admin = require_roles(UserRole.employer, UserRole.admin)