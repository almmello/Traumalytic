import openai  # Importando a biblioteca openai
import os
from dotenv import load_dotenv

load_dotenv()

class OpenAIInterface:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = "gpt-3.5-turbo"  # ou "gpt-4-1106-preview" conforme a necessidade
        self.max_tokens = 150  # Valor padrão, ajuste conforme necessário
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

