import streamlit as st
import os
from data_loader import DataLoader

from modulos.teste_ks_ptci_total.calculo_teste_ks_ptci_total import (
    calcular_teste_ks_ptci_total
)

from openai_interface import (
    carregar_conclusoes,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_teste_ks_ptci_total():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'teste_ks_ptci_total'
    nome_analise = 'Teste Kolmogorov-Smirnov para PTCI Total'
    instrucoes = "Analisando os resultados da Teste Kolmogorov-Smirnov para PTCI Total, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados = calcular_teste_ks_ptci_total(st.session_state['data'])
    st.write('Teste Kolmogorov-Smirnov para PTCI Total:', resultados)

    carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)
