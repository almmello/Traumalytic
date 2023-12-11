import streamlit as st
import os
from data_loader import DataLoader

from modulos.descritiva_estatisticas_idade.calculo_descritiva_estatisticas_idade import (
    calcular_estatisticas,
)

from openai_interface import (
    carregar_conclusoes,
)

from supabase_manager import SupabaseManager

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_estatisticas_idade():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'descritiva_estatisticas_idade'
    nome_analise = 'Análise Descritiva'
    instrucoes = "Analisando os resultados da análise de estatísticas de idade, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados = calcular_estatisticas(st.session_state['data'], 'IDADE')
    st.write('Estatísticas de Idade:', resultados)

    carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)







