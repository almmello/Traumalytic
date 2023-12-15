import streamlit as st
import pandas as pd
import os
from data_loader import DataLoader

from modulos.descritiva_medidas_dispersao.calculo_descritiva_medidas_dispersao import (
    calcular_descritiva_medidas_dispersao
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

def processar_descritiva_medidas_dispersao():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'descritiva_medidas_dispersao'
    nome_analise = 'Análise Medidas de Dispersão'
    instrucoes = "Analisando os resultados da Análise Medidas de Dispersão, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados_agrupados = {}

    colunas_numericas = st.session_state['data'].select_dtypes(include='number').columns
    for coluna in colunas_numericas:
        resultados = calcular_descritiva_medidas_dispersao(st.session_state['data'], coluna)
        
        # Exibindo os resultados no Streamlit
        st.subheader(f"Medidas de Dispersão - {coluna}")
        st.table(formatar_resultados(resultados))

        # Armazenando os resultados
        resultados_agrupados[coluna] = resultados

    # Convertendo resultados agrupados para texto
    texto_resultados = formatar_resultados_para_texto(resultados_agrupados)

    # Passando o texto concatenado para o método carregar_conclusoes
    carregar_conclusoes(analysis_id, nome_analise, texto_resultados, instrucoes)
