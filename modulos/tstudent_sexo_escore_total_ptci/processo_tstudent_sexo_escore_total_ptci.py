import streamlit as st
import os
from data_loader import DataLoader

from modulos.tstudent_sexo_escore_total_ptci.calculo_tstudent_sexo_escore_total_ptci import (
    calcular_tstudent_sexo_escore_total_ptci
)

from openai_interface import (
    carregar_conclusoes,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_tstudent_sexo_escore_total_ptci():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'tstudent_sexo_escore_total_ptci'
    nome_analise = 'Teste t de Student - Sexo vs Escore Total do PTCI'
    instrucoes = "Analisando os resultados da Teste t de Student - Sexo vs Escore Total do PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados = calcular_tstudent_sexo_escore_total_ptci(st.session_state['data'])
    st.write('Teste t de Student - Sexo vs Escore Total do PTCI:', resultados)

    carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)
