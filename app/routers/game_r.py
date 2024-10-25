from fastapi import APIRouter
from app.controllers import game_c
from app.schemas.game_schm import GameDto

router = APIRouter()

@router.post("/generate/syn_ant")
async def generate_game(game: GameDto):
    return await game_c.generate_game(game)