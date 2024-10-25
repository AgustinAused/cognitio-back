from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schm import UserCreate, UserLogin, UserUpdate
from app.services import user_s as user_service
from app.utils.jwt import create_access_token, create_refresh_token

async def register_user(user: UserCreate, db: AsyncSession):
    db_user = await user_service.create_user(db, user)
    return db_user

async def login_user(user: UserLogin, db: AsyncSession):
    db_user = await user_service.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token = create_access_token(data={"sub": db_user.email})
    refresh_token = create_refresh_token(data={"sub": db_user.email})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

async def refresh_access_token(refresh_token: str):
    new_access_token = await user_service.refresh_access_token(refresh_token)
    if not new_access_token:
        raise HTTPException(status_code=400, detail="Invalid refresh token")
    return {"access_token": new_access_token, "token_type": "bearer"}

async def get_user(db: AsyncSession, user_id: int):
    user = await user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def get_user_by_token(db: AsyncSession, tkn: str):
    user = await user_service.get_user_by_token(db, tkn)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def update_user(tkn: str, user: UserUpdate, db: AsyncSession):
    db_user = await user_service.update_user(db, user, tkn)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found or invalid token")
    return db_user

async def update_user_image(image: str, db: AsyncSession, tkn: str):
    db_user = await user_service.update_user_image(db, image, tkn)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found or invalid token")
    return db_user
