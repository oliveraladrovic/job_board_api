from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.base import get_db
from models.users import User
from models.enums import UserRole
from schemas.user import UserOut
from schemas.auth import NewRole
from dependencies.roles import require_admin

router = APIRouter(prefix="/admin")

@router.get("/users", response_model=list[UserOut])
async def get_users(db: AsyncSession = Depends(get_db), admin = Depends(require_admin)):
    result = await db.execute(select(User))
    return result.scalars().all()

@router.put("/users/{user_id}/role", status_code=200)
async def change_user_role(user_id: int, new_role: NewRole, db: AsyncSession = Depends(get_db), admin = Depends(require_admin)):
    # 1) User must exist
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # 2) role must exist
    if new_role not in UserRole:
        raise HTTPException(status_code=400, detail="Role does not exist")
    # 3) Change role
    user.role = new_role
    await db.commit()
    await db.refresh(user)
    # Inače vraćamo update-ani resurs, ali po API Contractu ovdje nemamo Returns