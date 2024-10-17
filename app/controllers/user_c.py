from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schm import UserCreate, UserLogin
from app.services import user_s
from app.utils.jwt import create_access_token, create_refresh_token


# Registro de usuario
async def register_user(user: UserCreate, db: AsyncSession):
    db_user = await user_s.create_user(db, user)
    return db_user

# Login de usuario
async def login_user(user: UserLogin, db: AsyncSession):
    db_user = await user_s.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": db_user.email})
    refresh_token = create_refresh_token(data={"sub": db_user.email})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

# Refresh Token Endpoint
async def refresh_access_token(refresh_token: str):
    new_access_token = await user_s.refresh_access_token(refresh_token)
    if not new_access_token:
        raise HTTPException(status_code=400, detail="Invalid refresh token")
    
    return {"access_token": new_access_token, "token_type": "bearer"}