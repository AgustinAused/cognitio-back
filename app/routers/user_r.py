from app.controllers import user_c
from fastapi import Depends, APIRouter
from app.database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schm import UserCreate, UserLogin, UserResponse

router = APIRouter()

@router.post("/register", response_model= UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_c.register_user(user, db)


@router.post("/login")
async def login_user(user: UserLogin, db: AsyncSession = Depends(get_db)):
    return await user_c.login_user(user, db)

@router.post("/refresh")
async def refresh_access_token(refresh_token: str):
    return await user_c.refresh_access_token(refresh_token)

@router.get("/{user_id}")
async def get_user(db: AsyncSession = Depends(get_db), user_id:int = None) -> UserResponse:
    return await user_c.get_user(db, user_id)