from app.schemas.progress_schm import ProgressCreated
from app.models.models import ProgressLevel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select, delete
from sqlalchemy.exc import SQLAlchemyError
from app.services.user_s import get_user_by_token
from datetime import datetime


async def create_progress_level(db: AsyncSession, progress: ProgressCreated, tkn: str):
    # Recuperar user a través del token
    user = await get_user_by_token(db, tkn)
    if not user:
        return None

    # Crear instancia de ProgressLevel
    progress_level = ProgressLevel(
        level=progress.level,
        user_id=user.id,
        type=progress.type,
        correct=progress.correct,
        total=progress.incorrect + progress.correct,
        completed_at = datetime.now()  # Guardar como datetime
    )

    # Guardar en la base de datos
    db.add(progress_level)
    await db.commit()
    await db.refresh(progress_level)

    # Formatear salida para cumplir con ProgressOut
    return {
        "id": progress_level.id,
        "level": progress_level.level,
        "type": progress_level.type,
        "completed_at": progress_level.completed_at.isoformat(),  # Convertir a str
        "correct": progress_level.correct,
        "total": progress_level.total 
    }


async def update_progress_level(progress: ProgressCreated, db: AsyncSession, tkn: str):
    user = await get_user_by_token(db, tkn)
    if not user:
        return None

    result = await db.execute(
        select(ProgressLevel).where(
            ProgressLevel.user_id == user.id,
            ProgressLevel.type == progress.type
        )
    )
    progress_level = result.scalars().first()
    if progress_level:
        progress_level.correct += progress.correct
        progress_level.total += progress.incorrect + progress.correct 
        progress_level.completed_at = datetime.now()  # Actualizar fecha

        await db.commit()
        await db.refresh(progress_level)

        # Formatear salida para cumplir con ProgressOut
        return {
            "id": progress_level.id,
            "level": progress_level.level,
            "type": progress_level.type,
            "completed_at": progress_level.completed_at.isoformat(),  # Convertir a str
            "correct": progress_level.correct,
            "total": progress_level.total
        }

    return None


async def get_progress_level(db: AsyncSession, tkn: str):
    # Obtener el usuario a partir del token
    user = await get_user_by_token(db, tkn)
    
    if not user:
        raise ValueError("Usuario no encontrado")

    try:
        result = await db.execute(select(ProgressLevel).where(ProgressLevel.user_id == user.id))

        progress = result.scalars().all()
        
        return progress
    except SQLAlchemyError as e:
        # Manejo de errores si la consulta falla
        print(f"Error al obtener los niveles de progreso: {str(e)}")
        raise

async def check_exist_progress_level(db: AsyncSession, type: str, user_id: int):
    result = await db.execute(select(ProgressLevel).where(ProgressLevel.type == type).where(ProgressLevel.user_id == user_id))
    progress = result.scalars().first()
    return progress

async def delete_progress_level(db: AsyncSession, progress_id: int):
    try:
        await db.execute(delete(ProgressLevel).where(ProgressLevel.id == progress_id))
        await db.commit()
        return True
    except SQLAlchemyError as e:
        print(f"Error al eliminar el nivel de progreso: {str(e)}")
        raise

