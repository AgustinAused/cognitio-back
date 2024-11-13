from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.progress_schm import ProgressCreated
from app.services import progress_s


async def create_progress_level(progress: ProgressCreated, db: AsyncSession, tkn: str):
    progress = await progress_s.create_progress_level(db, progress, tkn)
    if not progress:
        raise HTTPException(status_code=400, detail="Error creating progress")
    return progress

async def get_progress_level(db: AsyncSession, tkn: str):
    progress = await progress_s.get_progress_level(db, tkn)
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return progress


async def update_progress_level(progress: ProgressCreated, db: AsyncSession, tkn: str):
    progress = await progress_s.update_progress_level(db, progress, tkn)
    if not progress:
        raise HTTPException(status_code=400, detail="Error updating progress")
    return progress

async def check_exist_progress_level(db: AsyncSession,  type: str, user_id: int):
    progress = await progress_s.check_exist_progress_level(db, type, user_id)
    if not progress:
        return None
    return progress






