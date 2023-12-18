import streamlit as st
import os
from data_loader import DataLoader

from modulos.corte_tept_pcl5.calculo_corte_tept_pcl5 import (
    gerar_estatisticas_gerais_tept,
    gerar_frequencias_tept,
)

from modulos.corte_tept_pcl5.conteudo_corte_tept_pcl5 import (
    explicar_frequencias_tept
)

from openai_interface import (
    carregar_conclusoes,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_corte_tept_pcl5():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'corte_tept_pcl5'
    nome_analise = 'Análise de Frequência de Diagnóstico de TEPT com Ponto de Corte do PCL-5'
    instrucoes = "Analisando os resultados da Análise de Corte TEPT PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    # Gerar as tabelas separadas
    estatisticas_gerais = gerar_estatisticas_gerais_tept()
    frequencias = gerar_frequencias_tept(st.session_state['data'])

    # Exibir as tabelas na tela
    st.write('Estatísticas Gerais de TEPT:', estatisticas_gerais)
    explicar_frequencias_tept()
    st.write('Frequências de Diagnóstico TEPT:', frequencias)

    # Concatenar as tabelas em formato de string para a geração da conclusão
    resultados_para_conclusao = f"{estatisticas_gerais.to_string(index=False)}\n\n{frequencias.to_string(index=False)}"
    
    # Gerar conclusões baseadas nos resultados concatenados
    carregar_conclusoes(analysis_id, nome_analise, resultados_para_conclusao, instrucoes)

