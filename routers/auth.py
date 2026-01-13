from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.base import get_db
from models.users import User
from schemas.user import UserCreate, UserOut
from services.auth import hash_password

route = APIRouter(prefix="/auth")

@route.post("/register", response_model=UserOut)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed_password = hash_password(user_in.password)
    query = await db.execute(select(User).where(User.email == user_in.email))
    double_user = query.scalar_one_or_none()
    if double_user is not None:
        raise HTTPException(status_code=409, detail="User already exists")
    new_user = User(
        email = user_in.email,
        hashed_password = hashed_password,
        role = user_in.role,
        name = user_in.name
    )
    db.add(new_user)
    await db.commit()
    await db.refresh
    return new_user