import streamlit as st
import os
from data_loader import DataLoader

from openai_processes import (
    processar_conclusoes_tabela,
)

from modulos.caule_folhas_pcl5.conteudo_caule_folhas_pcl5 import (
    analysis_id,
    nome_analise,
    instrucoes,
)

from modulos.caule_folhas_pcl5.calculo_caule_folhas_pcl5 import (
    calcular_caule_folhas_pcl5,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_caule_folhas_pcl5():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    
    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados = calcular_caule_folhas_pcl5(st.session_state['data'])
    st.write('Exibição de Caule-e-Folhas do PCL-5:')

    # Display the DataFrame as a table
    st.dataframe(resultados)

    # Carregar as conclusões
    processar_conclusoes_tabela(analysis_id, resultados, nome_analise, instrucoes, debug)
