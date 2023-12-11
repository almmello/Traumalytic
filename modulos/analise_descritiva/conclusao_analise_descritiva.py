import os
from openai_parser import OpenAIInterface  # Importando a classe OpenAIInterface

def processar_comentario_e_atualizar_conclusao(comentario):
    dir_path = 'modulos/analise_descritiva/conclusoes_analise_descritiva'
    conclusao_path = os.path.join(dir_path, 'conclusao_estatistica_idade.txt')

    # Verifying if the conclusion file exists...
    if os.path.exists(conclusao_path):
        with open(conclusao_path, 'r') as file:
            conclusao_atual = file.read()
        openai_interface = OpenAIInterface()

        response = openai_interface.process_comment_and_update_conclusion(comentario, conclusao_atual)
        nova_conclusao = response.content

        with open(conclusao_path, 'w') as file:
            file.write(nova_conclusao)
        
        return nova_conclusao
    else:

        return None
