from fastapi import APIRouter
from app.controllers import game_c
from app.schemas.game_schm import GameDto

router = APIRouter()

@router.post("/generate/")
async def generate_game(game: GameDto):
    return await game_c.generate_game(game)