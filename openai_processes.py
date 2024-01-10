# Importações necessárias
from openai_parser import OpenAIInterface
from supabase_manager import SupabaseManager
from fig_management import FigManagement
import streamlit as st
import os


def carregar_conclusoes(analysis_id, etapa_analise, nome_analise, resultados=None, instrucoes=None):

    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    # Filtrar conclusões que não são do tipo "resultado"
    existing_conclusions = [conclusion for conclusion in existing_conclusions if conclusion['type'] != 'resultado']

    # Verificar se existem conclusões anteriores
    if not existing_conclusions:
        # Gerar e inserir a primeira conclusão se não existir
        nova_conclusao = gerar_conclusao(analysis_id, etapa_analise, instrucoes, resultados)
        st.subheader(f"Nova Conclusão: {nome_analise}")
        st.markdown(nova_conclusao)
    else:
        # Exibir o histórico de chat existente
        chat_history = sorted(
            existing_conclusions,
            key=lambda x: x['created_at']
        )
        contador = 1
        for message in chat_history:
            if message['type'] == 'resposta':
                
                st.subheader(f'Conclusão {contador:02d}')                
            elif message['type'] == 'comentario':
                contador -= 1
                st.subheader(f'Comentário {contador:02d}')
            
            st.markdown(message['conclusion'])
            contador += 1

    # Caixa de texto e botão para comentários
    comentario = st.text_area("Faça comentários sobre a conclusão de forma que possa ser atualizada:", key=f"comment_{st.session_state['reset_counter']}")
    if st.button('Enviar Comentário'):
        gerar_nova_conclusao(analysis_id, etapa_analise, comentario, resultados=None, instrucoes=None)
        st.session_state['reset_counter'] += 1

        st.rerun()

def gravar_resultados(analysis_id, etapa_analise, resultados_texto):
    supabase_manager = SupabaseManager()
    resultado = supabase_manager.inserir_conclusao(analysis_id, etapa_analise, 'resultado', resultados_texto, 'ativa')
    # Verificar se a operação foi bem-sucedida
    if resultado:
        return True
    else:
        return False

def gerar_conclusao(analysis_id, etapa_analise, instrucoes, resultados):
    openai_interface = OpenAIInterface()

    response = openai_interface.criar_conclusao(instrucoes, resultados)
    texto_conclusao = response.content

    supabase_manager = SupabaseManager()
    supabase_manager.inserir_conclusao(analysis_id, etapa_analise, 'resposta', texto_conclusao, 'ativa')

    return texto_conclusao

def gerar_nova_conclusao(analysis_id, etapa_analise, comentario, resultados=None, instrucoes=None):
    debug = True  # Defina como False para desativar os logs de depuração
    supabase_manager = SupabaseManager()
    openai_interface = OpenAIInterface()

    if debug:
        print("\nIniciando a geração de nova conclusão para a análise ID:", analysis_id, "\n")

    # Recuperar todas as conclusões existentes para a análise
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)
    if debug:
        print("\nConclusões existentes recuperadas:", existing_conclusions, "\n")

    # Solicitar à OpenAI para processar o chat e fornecer uma conclusão atualizada
    response = openai_interface.criar_conclusao(instrucoes, resultados, comentario, existing_conclusions)  # "" representa instrucoes e resultados vazios
    updated_conclusion = response.content
    if debug:
        print("\nResposta da OpenAI recebida:", updated_conclusion, "\n")

    # Inserir o novo comentário e a conclusão atualizada no banco de dados
    supabase_manager.inserir_conclusao(analysis_id, etapa_analise, 'comentario', comentario, 'ativa')
    if debug:
        print("\nNovo comentário inserido no banco de dados para a análise ID:", analysis_id, "\n")

    supabase_manager.inserir_conclusao(analysis_id, etapa_analise, 'resposta', updated_conclusion, 'ativa')
    if debug:
        print("\nConclusão atualizada inserida no banco de dados para a análise ID:", analysis_id, "\n")

    return updated_conclusion

def processar_visao_imagem(figura, prompt_text):
    debug = True  # Defina como False para desativar os logs de depuração
    fig_manager = FigManagement()
    openai_interface = OpenAIInterface()

    # Salvar e converter a figura em base64
    caminho_figura = fig_manager.salvar_grafico(figura)
    imagem_base64 = openai_interface.encode_image_to_base64(caminho_figura)
    descricao = openai_interface.descrever_imagem_base64(imagem_base64, prompt_text)
    fig_manager.apagar_grafico(caminho_figura)

    if debug:
        print(f"Descrição da Imagem ({prompt_text}):", descricao)

    return descricao

def processar_conclusoes_imagem(analysis_id, etapa_analise, fig, prompt_plot, nome_analise, instrucoes, debug):
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:
        descricao_plot = processar_visao_imagem(fig, prompt_plot)
        resultados = f"Resultados {nome_analise}: {descricao_plot}"

        if debug:
            print("\nTexto para Geração de Conclusões: ", resultados, "\n")

        gravacao_bem_sucedida = gravar_resultados(analysis_id, etapa_analise, resultados)

        if debug:
            print("\nRetorno Gravação: ", gravacao_bem_sucedida, "\n")

        if gravacao_bem_sucedida:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)

    else:
        resultados = supabase_manager.recuperar_resultados(analysis_id)
        
        if resultados:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)



def processar_conclusoes_tabela(analysis_id, tabela_resultados, nome_analise, instrucoes, debug):
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:
        # Formatar os resultados agrupados para texto
        texto_resultados = formatar_resultados_para_texto(tabela_resultados)
        resultados= f"Resultados {nome_analise}: {texto_resultados}"

        if debug:
            print("\nTexto para Geração de Conclusões: ", resultados, "\n")

        # Gravar os resultados formatados
        gravacao_bem_sucedida = gravar_resultados(analysis_id, resultados)

        if debug:
            print("\nRetorno Gravação: ", gravacao_bem_sucedida, "\n")

        if gravacao_bem_sucedida:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)

    else:
        # Carregar conclusões existentes sem gerar novas descrições
        resultados = supabase_manager.recuperar_resultados(analysis_id)

        if resultados:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)

# Função auxiliar para formatar resultados para texto
def formatar_resultados_para_texto(tabela_resultados):
    texto = ""
    for coluna, estatisticas in tabela_resultados.items():
        texto += f"Valores na coluna '{coluna}':\n"
        texto += estatisticas.to_string() + "\n\n"
    return texto


def processar_conclusoes_texto(analysis_id, etapa_analise, texto_resultados, nome_analise, instrucoes, debug):
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:
        # Preparar o texto dos resultados
        resultados = f"Resultados {nome_analise}: {texto_resultados}"

        if debug:
            print("\nTexto para Geração de Conclusões: ", resultados, "\n")

        # Gravar os resultados formatados
        gravacao_bem_sucedida = gravar_resultados(analysis_id, etapa_analise, resultados)

        if debug:
            print("\nRetorno Gravação: ", gravacao_bem_sucedida, "\n")

        if gravacao_bem_sucedida:
            carregar_conclusoes(analysis_id, etapa_analise, nome_analise, resultados, instrucoes)

    else:
        # Carregar conclusões existentes sem gerar novas descrições
        resultados = supabase_manager.recuperar_resultados(analysis_id)

        if resultados:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)


