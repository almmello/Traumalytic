import streamlit as st
import os
from data_loader import DataLoader

from modulos.estatisticas_variaveis_categoricas.conteudo_estatisticas_variaveis_categoricas import (
    analysis_id,
    nome_analise,
    instrucoes,
)

from modulos.estatisticas_variaveis_categoricas.calculo_estatisticas_variaveis_categoricas import (
    calcular_estatisticas_variaveis_categoricas,
)

from openai_processes import (
    processar_conclusoes_tabela,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_estatisticas_variaveis_categoricas():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()
    
    resultados_agrupados = {}

    colunas_categoricas = st.session_state['data'].select_dtypes(include='object').columns
    for coluna in colunas_categoricas:
        resultados = calcular_estatisticas_variaveis_categoricas(st.session_state['data'], coluna)
        
        # Exibindo os resultados no Streamlit
        st.subheader(f"Estatísticas de Variáveis Categóricas: - {coluna}")
        st.table(resultados)

        # Armazenando os resultados
        resultados_agrupados[coluna] = resultados

    # Passando o texto concatenado para o método carregar_conclusoes
    processar_conclusoes_tabela(analysis_id, resultados_agrupados, nome_analise, instrucoes, debug)

