from fastapi import Depends, APIRouter, Header, HTTPException
from typing import Annotated, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db import get_db
from app.schemas.user_schm import UserCreate, UserLogin, UserResponse, UserUpdate
from app.controllers import user_c as user_controller

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_controller.register_user(user, db)

@router.post("/login")
async def login_user(user: UserLogin, db: AsyncSession = Depends(get_db)):
    return await user_controller.login_user(user, db)

@router.post("/refresh")
async def refresh_access_token(refresh_token: str):
    return await user_controller.refresh_access_token(refresh_token)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_controller.get_user(db, user_id)

@router.get("/token/me", response_model=UserResponse)
async def get_user_by_token(
    bearer_token: Annotated[str | None, Header()], db: AsyncSession = Depends(get_db)
):
    if not bearer_token:
        raise HTTPException(status_code=401, detail="Authorization token missing")
    return await user_controller.get_user_by_token(db, bearer_token)

@router.put("/update", response_model=UserResponse)
async def update_user(
    user: UserUpdate, 
    bearer_token: Annotated[str | None, Header()], 
    db: AsyncSession = Depends(get_db)
):
    if not bearer_token:
        raise HTTPException(status_code=401, detail="Authorization token missing")
    return await user_controller.update_user(bearer_token, user, db)

@router.put("/update/image", response_model=UserResponse)
async def update_user_image(
    image: str, 
    bearer_token: Annotated[str | None, Header()], 
    db: AsyncSession = Depends(get_db)
    ):
    if not bearer_token:
        raise HTTPException(status_code=401, detail="Authorization token missing")
    return await user_controller.update_user_image(image, db, bearer_token)
