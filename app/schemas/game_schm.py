from pydantic import BaseModel

class GameDto(BaseModel):
    game_number: int
    difficulty: int
    number_excercises: int