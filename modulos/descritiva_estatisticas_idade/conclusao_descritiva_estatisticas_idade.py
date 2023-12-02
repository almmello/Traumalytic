import os
from openai_parser import OpenAIInterface  # Importando a classe OpenAIInterface
from dotenv import load_dotenv
from supabase_manager import SupabaseManager

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Usuário e senha carregados do arquivo .env
APP_USER = os.getenv("ENV_USER")

def gerar_conclusao_estatisticas_idade(estatisticas_idade, analysis_id):
    APP_USER = os.getenv("ENV_USER")
    openai_interface = OpenAIInterface()
    content = f"Estatísticas de Idade: {estatisticas_idade}"
    instructions = "Analisando as seguintes estatísticas de idade, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    response = openai_interface.generate_text_conclusion_with_template(content, instructions)
    conclusion_text = response.content

    supabase_manager = SupabaseManager()
    supabase_manager.insert_conclusion(APP_USER, analysis_id, 'response', conclusion_text, 'active')

    return conclusion_text




def processar_comentario_e_atualizar_conclusao(comentario, analysis_id):
    APP_USER = os.getenv("ENV_USER")
    supabase_manager = SupabaseManager()

    existing_conclusions = supabase_manager.get_conclusions()
    conclusao_atual = next((conclusion for conclusion in existing_conclusions if conclusion['analysis_id'] == analysis_id), None)

    if conclusao_atual:
        openai_interface = OpenAIInterface()
        response = openai_interface.process_comment_and_update_conclusion(comentario, conclusao_atual['conclusion'])
        updated_conclusion = response.content

        supabase_manager.update_conclusion(conclusao_atual['id'], {"conclusion": updated_conclusion, "type": "comment", "status": "active"})
        return updated_conclusion
    else:
        return None

