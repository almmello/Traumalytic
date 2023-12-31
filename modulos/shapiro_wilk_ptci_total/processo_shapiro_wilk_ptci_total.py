import streamlit as st
import os
from data_loader import DataLoader

from modulos.shapiro_wilk_ptci_total.conteudo_shapiro_wilk_ptci_total import (
    analysis_id,
    nome_analise,
    instrucoes,
)

from modulos.shapiro_wilk_ptci_total.calculo_shapiro_wilk_ptci_total import (
    calcular_shapiro_wilk_ptci_total
)

from openai_processes import (
    processar_conclusoes_tabela,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_shapiro_wilk_ptci_total():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    
    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados = calcular_shapiro_wilk_ptci_total(st.session_state['data'])
    st.write('Teste de Shapiro-Wilk para PTCI Total:', resultados)

    # Carregar as conclusões
    processar_conclusoes_tabela(analysis_id, resultados, nome_analise, instrucoes, debug)
