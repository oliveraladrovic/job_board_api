from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.base import get_db
from models.users import User
from schemas.user import UserCreate, UserOut
from schemas.auth import LoginIn, LoginOut
from models.enums import UserRole
from services.auth import hash_password, verify_password
from services.jwt import create_access_token

router = APIRouter(prefix="/auth")

@router.post("/register", response_model=UserOut, status_code=201)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    # 0) Debug: inspect password value
    print("PASSWORD:", user_in.password)
    print("TYPE:", type(user_in.password))
    print("LEN:", len(user_in.password))
    # 1) Email unique
    result = await db.execute(select(User).where(User.email == user_in.email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="User already exists")
    # 2) New user can not be admin
    if user_in.role not in {UserRole.candidate, UserRole.employer}:
        raise HTTPException(status_code=400, detail="Invalid role")
    # 3) Hash password
    hashed_password = hash_password(user_in.password)
    # 4) Create user
    new_user = User(
        email = user_in.email,
        hashed_password = hashed_password,
        role = user_in.role,
        name = user_in.name
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user

@router.post("/login", response_model=LoginOut)
async def user_login(log_in: LoginIn, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == log_in.email))
    user = result.scalar_one_or_none()
    if user is None or not verify_password(log_in.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "access_token": create_access_token(user.id),
        "token_type": "bearer"
    }