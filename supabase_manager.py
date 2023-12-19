from supabase import create_client, Client
from dotenv import load_dotenv
import os

class SupabaseManager:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        url = os.getenv('SUPABASE_URL')
        key = os.getenv('SUPABASE_KEY')
        self.supabase: Client = create_client(url, key)

    def inserir_conclusao(self, analysis_id, conclusion_type, conclusion, status):
        APP_USER = os.getenv("ENV_USER")
        data = {
            "user_id": APP_USER,
            "analysis_id": analysis_id,
            "type": conclusion_type,
            "conclusion": conclusion,
            "status": status
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
