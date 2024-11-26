from .game_strategy import GameStrategy
import json
from openai import OpenAI


class ReadAndConclude(GameStrategy):
    def __init__(self, game_prompt: str ,api_key:str):
        self.api_key = api_key
        self.game_prompt = game_prompt


    def generate_game(self,difficulty,number_excercises):
        client:OpenAI = OpenAI()
        prompt : object = self.build_prompt(difficulty,number_excercises)
        json_prompt: object = self.get_json()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content":json.dumps(json_prompt)},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        response_object = response.choices[0].message.content
        beautify_response = json.loads(response_object)

        return beautify_response
    
    

    def get_json(self):
        with open(self.game_prompt) as f:
            return json.load(f)
        
    def build_prompt(self,difficulty,number_excercises):
        return f"Genera {number_excercises} ejercicios de nivel {difficulty} "
        