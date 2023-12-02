from supabase import create_client, Client
from dotenv import load_dotenv
import os

class SupabaseManager:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        url = os.getenv('SUPABASE_URL')
        key = os.getenv('SUPABASE_KEY')
        self.supabase: Client = create_client(url, key)

    def insert_conclusion(self, user_id, analysis_id, conclusion_type, conclusion, status):
        data = {
            "user_id": user_id,
            "analysis_id": analysis_id,
            "type": conclusion_type,
            "conclusion": conclusion,
            "status": status
        }
        return self.supabase.table("conclusions").insert(data).execute()

    def get_conclusions(self):
        response = self.supabase.table("conclusions").select("*").execute()
        # Assuming the response contains a 'data' attribute with the actual results
        return response.data if response else []

    def update_conclusion(self, id, updated_data):
        return self.supabase.table("conclusions").update(updated_data).eq("id", id).execute()

    def delete_conclusion(self, id):
        return self.supabase.table("conclusions").delete().eq("id", id).execute()

    # Additional methods for data insertion, querying, etc., can be added here
