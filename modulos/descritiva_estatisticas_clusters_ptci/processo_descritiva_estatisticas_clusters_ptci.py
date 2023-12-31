import streamlit as st
import os
from data_loader import DataLoader

from modulos.descritiva_estatisticas_clusters_ptci.conteudo_descritiva_estatisticas_clusters_ptci import (
    analysis_id,
    nome_analise,
    instrucoes,
)

from modulos.descritiva_estatisticas_clusters_ptci.calculo_descritiva_estatisticas_clusters_ptci import (
    calcular_descritiva_estatisticas_clusters_ptci
)

from openai_processes import (
    processar_conclusoes_tabela,
)

from supabase_manager import SupabaseManager

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_descritiva_estatisticas_clusters_ptci():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()
                 
    resultados = calcular_descritiva_estatisticas_clusters_ptci(st.session_state['data'])
    st.write('Estatísticas dos Clusters e do Escore Total do PTCI:', resultados)

    processar_conclusoes_tabela(analysis_id, resultados, nome_analise, instrucoes, debug)
