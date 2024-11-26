from app.services.strategies.game_strategy import GameStrategy
from app.services.strategies.partners_contraries import PartnersAndContraries
from app.services.strategies.read_conclude import ReadAndConclude
from app.services.strategies.who_was import WhoWas
import os

API_KEY = os.getenv("OPENAI_API_KEY")


async def generate_game(number: int,number_excercises: int,difficulty: int):
    match number:
        case 1:
            game : GameStrategy = PartnersAndContraries("app/utils/partners_contaries_prompt.json",API_KEY)
            return game.generate_game(difficulty,number_excercises)
        case 2:
            game : GameStrategy = ReadAndConclude("app/utils/lee_y_concluye.json",API_KEY)
            return game.generate_game(difficulty,number_excercises)
        case 3:
            game : GameStrategy = WhoWas("app/utils/quien_fue.json",API_KEY)
            return game.generate_game(difficulty,number_excercises)
        case _:
            return {"message": "Game not found!"}