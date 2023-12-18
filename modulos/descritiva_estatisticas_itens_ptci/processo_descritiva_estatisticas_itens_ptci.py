import streamlit as st
import os
from data_loader import DataLoader

from modulos.descritiva_estatisticas_itens_ptci.calculo_descritiva_estatisticas_itens_ptci import (
    calcular_descritiva_estatisticas_itens_ptci,
    formatar_resultados_para_conclusao
)

from openai_interface import (
    carregar_conclusoes,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_descritiva_estatisticas_itens_ptci():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'descritiva_estatisticas_itens_ptci'
    nome_analise = 'Análise Estatísticas dos Itens do PTCI'
    instrucoes = "Analisando os resultados da Análise Estatísticas dos Itens do PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados = calcular_descritiva_estatisticas_itens_ptci(st.session_state['data'])
    st.write('Estatísticas dos Itens do PTCI:', resultados)

    # Formatar os resultados para a conclusão
    resultados_formatados = formatar_resultados_para_conclusao(resultados)

    # Carregar as conclusões
    carregar_conclusoes(analysis_id, nome_analise, resultados_formatados, instrucoes)
