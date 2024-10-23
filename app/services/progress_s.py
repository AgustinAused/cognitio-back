from app.schemas.progress_schm import ProgressCreated
from app.models.models import ProgressLevel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select
from app.services.user_s import get_user_by_token


async def create_progress_level(db: AsyncSession, progress: ProgressCreated, tkn: str):
    # Recuperar user a través del token
    user = await get_user_by_token(db, tkn)
    if not user:
        return None
    
    exercises_completed = [
        progress.ex1_completed,
        progress.ex2_completed,
        progress.ex3_completed,
        progress.ex4_completed,
        progress.ex5_completed
    ]
    
    total_exercises = len(exercises_completed)  
    completed_exercises = sum(exercises_completed)  
    
    # Calcular el porcentaje de ejercicios completados
    score = (completed_exercises / total_exercises) * 100


    # Crear instancia de ProgressLevel con el score calculado
    progress_level = ProgressLevel(
        level=progress.level,
        user_id=user.id,
        ex1_completed=progress.ex1_completed,
        ex2_completed=progress.ex2_completed,
        ex3_completed=progress.ex3_completed,
        ex4_completed=progress.ex4_completed,
        ex5_completed=progress.ex5_completed,
        score=score, 
        completed_at=progress.completed_at
    )

    # Guardar en la base de datos
    db.add(progress_level)
    await db.commit()
    await db.refresh(progress_level)
    
    return progress_level


async def get_progress_level(db: AsyncSession, tkn: str):
    user = await get_user_by_token(db, tkn)
    result = await db.execute(select(ProgressLevel).where(ProgressLevel.user_id == user.id))
    progress = result.all()
    return progress

