import streamlit as st
import os
from data_loader import DataLoader

from modulos.descritiva_estatisticas_clusters_pcl5.conteudo_descritiva_estatisticas_clusters_pcl5 import (
    analysis_id,
    nome_analise,
    instrucoes,
)

from modulos.descritiva_estatisticas_clusters_pcl5.calculo_descritiva_estatisticas_clusters_pcl5 import (
    calcular_descritiva_estatisticas_clusters_pcl5
)

from openai_processes import (
    processar_conclusoes_tabela,
)

from supabase_manager import SupabaseManager

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_descritiva_estatisticas_clusters_pcl5():

    APP_USER = os.getenv("ENV_USER")
    
    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados = calcular_descritiva_estatisticas_clusters_pcl5(st.session_state['data'])

    st.write('Estatísticas dos Clusters e do Escore Total do PCL-5:', resultados)

    # Carregar as conclusões
    processar_conclusoes_tabela(analysis_id, resultados, nome_analise, instrucoes)
