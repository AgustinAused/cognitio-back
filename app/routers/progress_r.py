from app.controllers import progress_c
from fastapi import Depends, APIRouter, Header
from typing import Annotated
from app.database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.progress_schm import ProgressCreated, ProgressOut

router = APIRouter()

@router.post("/", response_model= ProgressOut)
async def create_progress_level(progress: ProgressCreated, bearer_token: Annotated[str | None, Header()], db: AsyncSession = Depends(get_db)):
    return await progress_c.create_progress_level(progress, db, bearer_token)

@router.get("/", response_model= ProgressOut)    
async def get_progress_level(bearer_token: Annotated[str | None, Header()], db: AsyncSession = Depends(get_db)):
    return await progress_c.get_progress_level(db, bearer_token)

