from abc import ABC, abstractmethod

class GameStrategy(ABC):

    def __init__(self,game_prompt:str,api_key:str):
        self.api_key = api_key
        self.game_prompt = game_prompt


    @abstractmethod
    def generate_game(self):
        pass

    @abstractmethod
    def get_json(self):
        pass

    @abstractmethod
    def build_prompt(self):
        pass

