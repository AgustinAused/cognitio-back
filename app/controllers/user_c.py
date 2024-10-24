from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schm import UserCreate, UserLogin, UserUpdate
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


# Obtener todos los usuarios
async def get_user(db: AsyncSession, user_id: int = None):
    users = await user_s.get_user(db, user_id)
    return users


# Obtener usuario por token
async def get_user_by_token(db: AsyncSession, tkn: str):
    user = await user_s.get_user_by_token(db, tkn)
    return user

# Update user
async def update_user(user: UserUpdate, db: AsyncSession):
    db_user = await user_s.update_user(db, user)
    return db_user

# Update user image
async def update_user_image(image: str, db: AsyncSession, tkn: str):
    db_user = await user_s.update_user_image(db, image, tkn)
    return db_user


