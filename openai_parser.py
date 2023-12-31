import openai  # Importando a biblioteca openai
import os
import base64
from dotenv import load_dotenv

load_dotenv()

class OpenAIInterface:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model =  "gpt-4-1106-preview"  # "gpt-3.5-turbo"  # ou "gpt-4-1106-preview" conforme a necessidade
        self.vision_model = "gpt-4-vision-preview"  # Modelo para visão
        self.max_tokens = 4000  # Valor padrão, ajuste conforme necessário (máximo = 4000)
        self.system_message_content = "Você é um assistente analítico especializado em dados de trauma e TEPT. Forneça insights e gere conclusões que possam auxiliar na compreensão do impacto do trauma nos indivíduos."
        openai.api_key = self.api_key
        self.client = openai.OpenAI()  # Criando um cliente da biblioteca openai


    def criar_conclusao(self, instrucoes, resultados, comentario=None, historico_conclusoes=None):
        # Construção da mensagem inicial com os resultados da análise
        instrucao_completa = f"{instrucoes}\n\nResultados da análise:\n{resultados}"

        # Construção das mensagens
        messages = [
            {"role": "system", "content": self.system_message_content},
            {"role": "user", "content": instrucao_completa}
        ]

        # Adicionar cada entrada do histórico de conclusões ao histórico de mensagens
        if historico_conclusoes:
            for conclusao in historico_conclusoes:
                role = "system" if conclusao['type'] == 'resposta' else "user"
                messages.append({"role": role, "content": conclusao['conclusion']})

        # Se houver um novo comentário, adicionar ao final da lista de mensagens
        if comentario:
            messages.append({"role": "user", "content": comentario})

        # Chamada à API OpenAI para processar as mensagens e gerar uma conclusão
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
        )

        # Retornar a conclusão gerada pelo modelo
        return response.choices[0].message

    # Codifica uma imagem local em base64.
    def encode_image_to_base64(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Envia uma imagem codificada em base64 para a GPT-4 com visão e retorna uma descrição textual da imagem.
    def descrever_imagem_base64(self, base64_image, prompt_text="What’s in this image?"):
        response = self.client.chat.completions.create(
            model=self.vision_model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ],
                }
            ],
            max_tokens=self.max_tokens
        )
        return response.choices[0].message.content
