import openai  # Importando a biblioteca openai
import os
from dotenv import load_dotenv

load_dotenv()

class OpenAIInterface:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key
        self.client = openai.OpenAI()  # Criando um cliente da biblioteca openai


    def generate_text_conclusion_with_template(self, content, instructions):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo", #gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{instructions}\n\n{content}"}
            ]
        )
        return completion.choices[0].message




