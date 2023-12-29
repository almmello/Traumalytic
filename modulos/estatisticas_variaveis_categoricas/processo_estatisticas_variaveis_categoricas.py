import streamlit as st
import os
from data_loader import DataLoader

from modulos.estatisticas_variaveis_categoricas.calculo_estatisticas_variaveis_categoricas import (
    calcular_estatisticas_variaveis_categoricas,
    formatar_resultados_para_texto
)

from openai_interface import (
    carregar_conclusoes,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_estatisticas_variaveis_categoricas():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'estatisticas_variaveis_categoricas'
    nome_analise = 'Estatísticas de Variáveis Categóricas'
    instrucoes = "Analisando os resultados da Estatísticas de Variáveis Categóricas, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

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

    # Convertendo resultados agrupados para texto
    texto_resultados = formatar_resultados_para_texto(resultados_agrupados)

    # Passando o texto concatenado para o método carregar_conclusoes
    carregar_conclusoes(analysis_id, nome_analise, texto_resultados, instrucoes)


