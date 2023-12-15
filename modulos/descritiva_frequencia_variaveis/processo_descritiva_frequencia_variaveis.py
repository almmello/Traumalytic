import streamlit as st
import pandas as pd
import os
from data_loader import DataLoader

from modulos.descritiva_frequencia_variaveis.calculo_descritiva_frequencia_variaveis import (
    calcular_descritiva_frequencia_variaveis
)

from openai_interface import (
    carregar_conclusoes,
)

def formatar_resultados(resultados):
    return pd.DataFrame(resultados, index=[0]).T.rename(columns={0: 'Valor'})

def formatar_resultados_para_texto(resultados):
    texto = ""
    for coluna, medidas in resultados.items():
        texto += f"Medidas de Tendência Central - {coluna}\n"
        for medida, valor in medidas.items():
            texto += f"{medida.capitalize()}: {valor}\n"
        texto += "\n"
    return texto

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_descritiva_frequencia_variaveis():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'descritiva_frequencia_variaveis'
    nome_analise = 'Análise Frequência de Variáveis Categóricas'
    instrucoes = "Analisando os resultados da Análise Frequência de Variáveis Categóricas, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados_agrupados = {}

    colunas_categoricas = st.session_state['data'].select_dtypes(include='object').columns
    for coluna in colunas_categoricas:
        resultados = calcular_descritiva_frequencia_variaveis(st.session_state['data'], coluna)
        
        # Exibindo os resultados no Streamlit
        st.subheader(f"Frequência de Variáveis Categóricas - {coluna}")
        st.table(resultados)

        # Armazenando os resultados
        resultados_agrupados[coluna] = resultados

    # Convertendo resultados agrupados para texto
    texto_resultados = formatar_resultados_para_texto(resultados_agrupados)

    # Passando o texto concatenado para o método carregar_conclusoes
    carregar_conclusoes(analysis_id, nome_analise, texto_resultados, instrucoes)
