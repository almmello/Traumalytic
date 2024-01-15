import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_processes import (
    processar_conclusoes_imagem,
)

from modulos.detrended_qq_ptci.conteudo_detrended_qq_ptci import (
    analysis_id,
    nome_analise,
    instrucoes,
    prompt_plot,
)

from modulos.detrended_qq_ptci.calculo_detrended_qq_ptci import (
    criar_detrended_qq_ptci
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_detrended_qq_ptci():

    APP_USER = os.getenv("ENV_USER")
    
    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    st.write(nome_analise)

    # Gerar e mostrar os gráficos para os dados do usuário
    fig = criar_detrended_qq_ptci(st.session_state['data'])
    st.pyplot(fig)
    
    # Processar resultados da Análise
    processar_conclusoes_imagem(analysis_id, fig, prompt_plot, nome_analise, instrucoes)
