
import os
import openai
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar la API Key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIService:
    def generate_exercise(self, topic: str, difficulty: str) -> str:
        # Definir el mensaje de entrada para el modelo
        prompt = f"Genera un ejercicio de {difficulty} nivel sobre el tema: {topic}."
        
        # Hacer la llamada a la API de ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-003",  # Modelo a usar
            prompt=prompt,
            max_tokens=200,  # Ajusta el límite de tokens
            n=1,
            stop=None,
            temperature=0.7  # Ajusta la creatividad
        )
        
        # Retornar el texto generado
        return response.choices[0].text.strip()
