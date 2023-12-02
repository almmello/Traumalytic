import streamlit as st
import os
from data_loader import DataLoader
from modulos.descritiva_estatisticas_idade.calculo_descritiva_estatisticas_idade import calcular_estatisticas
from modulos.descritiva_estatisticas_idade.conclusao_descritiva_estatisticas_idade import (
    gerar_conclusao_estatisticas_idade,
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
    
    conclusao = next((conclusion for conclusion in existing_conclusions if conclusion['analysis_id'] == analysis_id and conclusion['user_id'] == APP_USER), None)

    if conclusao:
        st.subheader('Conclusão da Análise Descritiva:')
        st.markdown(conclusao['conclusion'])
    else:
        nova_conclusao = gerar_conclusao_estatisticas_idade(estatisticas_idade, analysis_id)
        st.subheader('Nova Conclusão da Análise Descritiva:')
        st.markdown(nova_conclusao)



