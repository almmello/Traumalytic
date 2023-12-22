import streamlit as st
import os
from data_loader import DataLoader

from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
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
    analysis_id = 'caule_folhas_pcl5'
    nome_analise = 'Exibição de Caule-e-Folhas do PCL5'
    instrucoes = "Analisando os resultados da Exibição de Caule-e-Folhas do PCL5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    fig_hist = calcular_caule_folhas_pcl5(st.session_state['data'])
    st.write('Exibição de Caule-e-Folhas do PCL-5:')

    # Display the DataFrame as a table
    st.dataframe(fig_hist)

    # Concatenar as tabelas em formato de string para a geração da conclusão
    resultados_para_conclusao = f"{fig_hist.to_string(index=False)}"
    
    # Gerar conclusões baseadas nos resultados concatenados
    carregar_conclusoes(analysis_id, nome_analise, resultados_para_conclusao, instrucoes)
