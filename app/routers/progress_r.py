from app.controllers import progress_c
from app.services import user_s
from fastapi import Depends, APIRouter, Header, HTTPException
from typing import Annotated
from app.database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.progress_schm import ProgressCreated, ProgressOut

router = APIRouter()

@router.post("/", response_model=ProgressOut)
async def add_progress_level(
    progress: ProgressCreated,
    bearer_token: Annotated[str | None, Header()],
    db: AsyncSession = Depends(get_db)
):
    if not bearer_token:
        raise HTTPException(status_code=401, detail="Authorization token is missing")

    # Extraer user_id desde el token
    user = await user_s.get_user_by_token(db, bearer_token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Comprobamos si el nivel de progreso ya existe
    existing_progress = await progress_c.check_exist_progress_level(db, progress.type, user.id)
    if existing_progress:
        # Si existe
        return await progress_c.update_progress_level(progress, db, bearer_token)
    # Si no existe
    return await progress_c.create_progress_level(progress, db, bearer_token)


@router.get("/", response_model=list[ProgressOut])    
async def get_progres_by_usr(bearer_token: Annotated[str | None, Header()], db: AsyncSession = Depends(get_db)):
    return await progress_c.get_progress_level(db, bearer_token)

