import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from fig_management import FigManagement
from supabase_manager import SupabaseManager

from openai_processes import (
    processar_conclusoes_imagem
)

from modulos.histograma_ptci.conteudo_histograma_ptci import (
    analysis_id,
    nome_analise,
    instrucoes,
    prompt_plot,
)

from modulos.histograma_ptci.calculo_histograma_ptci import (
    criar_histograma
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_histograma_ptci():

    APP_USER = os.getenv("ENV_USER")
    
    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    st.write('Gráfico Histograma PTCI:')

    # Gerar e mostrar os gráficos para os dados do usuário
    descricao_x_hist = f'PTCI Total'
    descricao_y_hist = 'Frequência'
    fig = criar_histograma(st.session_state['data'], "PTCI_Total", descricao_x_hist, descricao_y_hist)
    st.pyplot(fig)

    # Processar resultados da Análise
    processar_conclusoes_imagem(analysis_id, fig, prompt_plot, nome_analise, instrucoes)