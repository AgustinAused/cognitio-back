from fastapi import APIRouter
from app.controllers import game_c
from app.models.models import GameDto

router = APIRouter()

@router.get("/generate/")
async def generate_game(game: GameDto):
    return await game_c.generate_game(game)