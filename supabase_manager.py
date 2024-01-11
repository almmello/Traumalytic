from supabase import create_client, Client
from dotenv import load_dotenv
import os

class SupabaseManager:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        url = os.getenv('SUPABASE_URL')
        key = os.getenv('SUPABASE_KEY')
        self.supabase: Client = create_client(url, key)

    def inserir_conclusao(self, analysis_id, etapa_analise, conclusion_type, conclusion, status):
        APP_USER = os.getenv("ENV_USER")

        # Converte 'etapa_analise' para um inteiro
        try:
            etapa_analise_int = int(etapa_analise)
        except ValueError:
            # Aqui você pode lidar com a situação em que 'etapa_analise' não é um número válido
            # Por exemplo, registrar um erro ou definir um valor padrão
            etapa_analise_int = 0  # ou qualquer valor padrão adequado
        data = {
            "user_id": APP_USER,
            "analysis_id": analysis_id,
            "type": conclusion_type,
            "conclusion": conclusion,
            "status": status, 
            "etapa": etapa_analise_int
        }
        return self.supabase.table("conclusions").insert(data).execute()

    def recuperar_conclusoes(self, analysis_id):
        APP_USER = os.getenv("ENV_USER")  # Get the system user from environment variable
        response = self.supabase.table("conclusions").select("*").eq("analysis_id", analysis_id).eq("user_id", APP_USER).execute()
        # Assuming the response contains a 'data' attribute with the actual results
        return response.data if response else []
    
    def atualizar_conclusao(self, id, updated_data):
        return self.supabase.table("conclusions").update(updated_data).eq("id", id).execute()

    def apagar_conclusao(self, id):
        return self.supabase.table("conclusions").delete().eq("id", id).execute()
    
    def recuperar_resultado(self, analysis_id):
        APP_USER = os.getenv("ENV_USER")  # Get the system user from environment variable
        response = self.supabase.table("conclusions").select("*").eq("analysis_id", analysis_id).eq("user_id", APP_USER).eq("type",'resultado').execute()

        if response and 'data' in response and isinstance(response['data'], list):
            # Extrair o campo 'conclusion' de cada item na lista
            resultados = [item.get('conclusion', '') for item in response['data'] if 'conclusion' in item]
            return resultados
        else:
            return []

    def atualizar_resultado(self, analysis_id, novo_resultado):
        # Filtrar para obter apenas a ocorrência de resultado
        existing_data = self.supabase.table("conclusions").select("*").eq("analysis_id", analysis_id).eq("type", "resultado").execute()

        if existing_data.data:
            id_conclusao = existing_data.data[0]['id']
            updated_data = {"conclusion": novo_resultado}
            return self.supabase.table("conclusions").update(updated_data).eq("id", id_conclusao).execute()