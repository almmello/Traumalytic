import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_processes import (
    processar_conclusoes_imagem
)

from modulos.teste_t_pcl5_total_ptci_total.calculo_teste_t_pcl5_total_ptci_total import (
    criar_teste_t_pcl5_total_ptci_total
)

from modulos.teste_t_pcl5_total_ptci_total.conteudo_teste_t_pcl5_total_ptci_total import (
    analysis_id,
    nome_analise,
    instrucoes,
    prompt_plot,
)


def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_teste_t_pcl5_total_ptci_total():

    APP_USER = os.getenv("ENV_USER")

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    # Gerar e mostrar os gráficos para os dados do usuário
    fig, resultados = criar_teste_t_pcl5_total_ptci_total(st.session_state['data'])
    st.pyplot(fig)
    st.dataframe(resultados)

    # Processar resultados da Análise
    processar_conclusoes_imagem(analysis_id, fig, prompt_plot, nome_analise, instrucoes)

    

