import streamlit as st
import os
from data_loader import DataLoader

from modulos.descritiva_estatisticas_escore_ptci.calculo_descritiva_estatisticas_escore_ptci import (
    calcular_descritiva_estatisticas_escore_ptci
)

from openai_interface import (
    carregar_conclusoes,
)

from supabase_manager import SupabaseManager

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_descritiva_estatisticas_escore_ptci():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'descritiva_estatisticas_escore_ptci'
    nome_analise = 'Análise Estatísticas do Escore Total PTCI'
    instrucoes = "Analisando os resultados da Análise Estatísticas do Escore Total PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados = calcular_descritiva_estatisticas_escore_ptci(st.session_state['data'])
    st.write('Estatísticas do Escore Total PTCI:', resultados)

    carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)
