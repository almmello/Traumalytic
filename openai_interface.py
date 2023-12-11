# Importações necessárias
from openai_parser import OpenAIInterface
from supabase_manager import SupabaseManager
import streamlit as st
import os


def carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes):

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
        for message in chat_history:
            if message['type'] == 'response':
                st.subheader('Conclusão: ' + nome_analise)
            elif message['type'] == 'comment':
                st.subheader('Comentário:')
            st.markdown(message['conclusion'])

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
    supabase_manager.inserir_conclusao(analysis_id, 'comment', comentario, 'ativa')
    supabase_manager.inserir_conclusao(analysis_id, 'response', updated_conclusion, 'ativa')

    return updated_conclusion