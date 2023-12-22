# Importações necessárias
from openai_parser import OpenAIInterface
from supabase_manager import SupabaseManager
from fig_management import FigManagement
import streamlit as st
import os


def carregar_conclusoes(analysis_id, nome_analise, resultados=None, instrucoes=None):

    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    # Verificar se existem conclusões anteriores
    if not existing_conclusions:
        # Gerar e inserir a primeira conclusão se não existir
        nova_conclusao = gerar_conclusao(analysis_id, instrucoes, resultados)
        st.subheader('Nova Conclusão: ' + nome_analise)
        st.markdown(nova_conclusao)
    else:
        # Exibir o histórico de chat existente
        chat_history = sorted(
            existing_conclusions,
            key=lambda x: x['created_at']
        )
        contador = 1
        st.subheader('Conclusão:')
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
        gerar_nova_conclusao(analysis_id, comentario)
        st.session_state['reset_counter'] += 1

        st.rerun()



def gerar_conclusao(analysis_id, instrucoes, resultados):
    openai_interface = OpenAIInterface()

    response = openai_interface.criar_conclusao(instrucoes, resultados)
    texto_conclusao = response.content  # Acesso correto ao conteúdo

    supabase_manager = SupabaseManager()
    supabase_manager.inserir_conclusao(analysis_id, 'resposta', texto_conclusao, 'ativa')

    return texto_conclusao



def gerar_nova_conclusao(analysis_id, comentario):

    supabase_manager = SupabaseManager()
    openai_interface = OpenAIInterface()

    # Recuperar todas as conclusões existentes para a análise
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    # Solicitar à OpenAI para processar o chat e fornecer uma conclusão atualizada
    response = openai_interface.criar_conclusao("", "", comentario, existing_conclusions)  # "" representa instrucoes e resultados vazios
    updated_conclusion = response.content

    # Inserir o novo comentário e a conclusão atualizada no banco de dados
    supabase_manager.inserir_conclusao(analysis_id, 'comentario', comentario, 'ativa')
    supabase_manager.inserir_conclusao(analysis_id, 'resposta', updated_conclusion, 'ativa')

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