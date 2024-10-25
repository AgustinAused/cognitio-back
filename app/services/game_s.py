from app.services.strategies.game_strategy import GameStrategy
from app.services.strategies.partners_contraries import PartnersAndContraries
import os

API_KEY = os.getenv("OPENAI_API_KEY")


async def generate_game(number: int,number_excercises: int,difficulty: int):
    match number:
        case 1:
            game : GameStrategy = PartnersAndContraries("D:/Codigo/Programacion/Proyectos/cognitio-back/app/utils/partners_contaries_prompt.json",API_KEY)
            return game.generate_game(difficulty,number_excercises)
        case _:
            return {"message": "Game not found!"}