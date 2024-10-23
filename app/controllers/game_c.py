from fastapi import HTTPException
from app.services import game_s
from app.models.models import GameDto

async def generate_game(game : GameDto):
    game : object = await game_s.generate_game(game.game_number,game.number_excercises,game.difficulty)
    if not game:
        raise HTTPException(status_code=400, detail="Error generating game")
    return game