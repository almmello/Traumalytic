import streamlit as st
import os
from data_loader import DataLoader

from modulos.corte_tept_pcl5.conteudo_corte_tept_pcl5 import (
    analysis_id,
    nome_analise,
    instrucoes,
)

from modulos.corte_tept_pcl5.calculo_corte_tept_pcl5 import (
    gerar_estatisticas_gerais_tept,
    gerar_frequencias_tept,
)

from modulos.corte_tept_pcl5.conteudo_corte_tept_pcl5 import (
    explicar_frequencias_tept
)

from openai_processes import (
    processar_conclusoes_texto,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_corte_tept_pcl5():

    APP_USER = os.getenv("ENV_USER")
    

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
    resultados = f"{estatisticas_gerais.to_string(index=False)}\n\n{frequencias.to_string(index=False)}"
    
    # Gerar conclusões baseadas nos resultados concatenados
    processar_conclusoes_texto(analysis_id, resultados, nome_analise, instrucoes)

