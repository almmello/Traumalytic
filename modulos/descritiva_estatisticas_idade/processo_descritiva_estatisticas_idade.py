import streamlit as st
import os
from data_loader import DataLoader

from modulos.descritiva_estatisticas_idade.calculo_descritiva_estatisticas_idade import (
    calcular_estatisticas,
)

from modulos.descritiva_estatisticas_idade.conclusao_descritiva_estatisticas_idade import (
    gerar_conclusao_estatisticas_idade,
    processar_comentario_e_atualizar_conclusao
)

from supabase_manager import SupabaseManager

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_estatisticas_idade():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'descritiva_estatisticas_idade'

    carregar_dados()
    estatisticas_idade = calcular_estatisticas(st.session_state['data'], 'IDADE')
    st.write('Estatísticas de Idade:', estatisticas_idade)

    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.get_conclusions()

    # Filter and sort the conclusions and comments by creation time
    chat_history = sorted(
        [c for c in existing_conclusions if c['analysis_id'] == analysis_id and c['user_id'] == APP_USER],
        key=lambda x: x['created_at']
    )

    # Display the chat history
    for message in chat_history:
        if message['type'] == 'response':
            st.subheader('Conclusão da Análise Descritiva:')
        elif message['type'] == 'comment':
            st.subheader('Comentário:')
        st.markdown(message['conclusion'])

    # Initialize counter in session state if not exists
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    # Use a unique key for the text area based on the counter
    comentario = st.text_area("Faça comentários sobre a conclusão de forma que possa ser atualizada:", key=f"comment_{st.session_state['reset_counter']}")

    if st.button('Enviar Comentário'):
        processar_comentario_e_atualizar_conclusao(comentario, analysis_id)
        st.session_state['reset_counter'] += 1
        st.rerun()






