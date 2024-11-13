from app.schemas.progress_schm import ProgressCreated
from app.models.models import ProgressLevel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select
from app.services.user_s import get_user_by_token
from datetime import datetime


async def create_progress_level(db: AsyncSession, progress: ProgressCreated, tkn: str):
    # Recuperar user a través del token
    user = await get_user_by_token(db, tkn)
    if not user:
        return None
    # Crear instancia de ProgressLevel con el score calculado
    progress_level = ProgressLevel(
        level=progress.level,
        user_id=user.id,
        type=progress.type,
        correct=progress.correct,
        incorrect=progress.incorrect, 
        completed_at = datetime.now().date()
    )

    # Guardar en la base de datos
    db.add(progress_level)
    await db.commit()
    await db.refresh(progress_level)
    
    return progress_level

async def update_progress_level(db: AsyncSession, progress: ProgressCreated, tkn: str):
    user = await get_user_by_token(db, tkn)
    if not user:
        return None
    result = await db.execute(select(ProgressLevel).where(ProgressLevel.user_id == user.id and ProgressLevel.type == progress.type))
    progress_level = result.scalars().first()
    if progress_level:
        progress_level.correct =+ progress.correct
        progress_level.total = progress.incorrect + progress.correct
        progress_level.completed_at = datetime.now().date()
        await db.commit()
        await db.refresh(progress_level)
    return progress_level

async def get_progress_level(db: AsyncSession, tkn: str):
    user = await get_user_by_token(db, tkn)
    result = await db.execute(select(ProgressLevel).where(ProgressLevel.user_id == user.id))
    progress = result.all()
    return progress

async def check_exist_progress_level(db: AsyncSession, level: int, type: str, user_id: int):
    result = await db.execute(select(ProgressLevel).where(ProgressLevel.level == level).where(ProgressLevel.type == type).where(ProgressLevel.user_id == user_id))
    progress = result.scalars().first()
    return progress
