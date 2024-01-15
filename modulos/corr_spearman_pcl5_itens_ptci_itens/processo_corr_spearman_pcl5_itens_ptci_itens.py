import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_processes import (
    processar_conclusoes_tabela,
)

from modulos.corr_spearman_pcl5_itens_ptci_itens.calculo_corr_spearman_pcl5_itens_ptci_itens import (
    criar_corr_spearman_pcl5_itens_ptci_itens
)

from modulos.corr_spearman_pcl5_itens_ptci_itens.conteudo_corr_spearman_pcl5_itens_ptci_itens import (
    analysis_id,
    nome_analise,
    instrucoes,
)


def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_corr_spearman_pcl5_itens_ptci_itens():

    APP_USER = os.getenv("ENV_USER")

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    # Gerar e mostrar os gráficos para os dados do usuário
    resultados = criar_corr_spearman_pcl5_itens_ptci_itens(st.session_state['data'])

    # Carregar as conclusões
    processar_conclusoes_tabela(analysis_id, resultados, nome_analise, instrucoes)