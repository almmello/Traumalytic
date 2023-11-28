import os
from openai_parser import OpenAIInterface  # Importando a classe OpenAIInterface

def gerar_conclusao_estatisticas_idade(estatisticas_idade):
    dir_path = 'modulos/analise_descritiva/conclusoes_analise_descritiva'
    conclusao_path = os.path.join(dir_path, 'conclusao_estatistica_idade.txt')

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    if not os.path.exists(conclusao_path):
        openai_interface = OpenAIInterface()
        content = f"Estatísticas de Idade: {estatisticas_idade}"
        instructions = "Analisando as seguintes estatísticas de idade, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

        response = openai_interface.generate_text_conclusion_with_template(content, instructions)
        conclusion_text = response.content  # Acesso direto ao conteúdo

        with open(conclusao_path, 'w') as file:
            file.write(conclusion_text)
    else:
        with open(conclusao_path, 'r') as file:
            conclusion_text = file.read()

    return conclusion_text


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
