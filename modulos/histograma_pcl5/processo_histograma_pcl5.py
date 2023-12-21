import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from fig_management import FigManagement
from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
)

from modulos.histograma_pcl5.calculo_histograma_pcl5 import (
    criar_histograma,
)

from openai_interface import (
    carregar_conclusoes,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_histograma_pcl5():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'histograma_pcl5'
    nome_analise = 'Gráfico Histograma PCL-5'
    instrucoes = "Analisando os resultados da Gráfico Histograma PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    st.write('Gráfico Histograma PCL-5:')

    # Gerar e mostrar os gráficos para os dados do usuário
    descricao_x_hist = f'PCL-5 Total'
    descricao_y_hist = 'Frequência'
    fig_hist = criar_histograma(st.session_state['data'], "PCL5_total", descricao_x_hist, descricao_y_hist)
    st.pyplot(fig_hist)
    plt.close(fig_hist)


    # Verificar se já existe uma conclusão armazenada
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:

        # Processar a visão dos gráficos caso não existam conclusões anteriores
        prompt_hist = "Descrição do histograma de frequência dos valores totais do PCL-5, representando a distribuição dos escores de trauma na amostra de dados. Explique a forma da distribuição e indique a tendência central, se visível."
        descricao_hist = processar_visao_imagem(fig_hist, prompt_hist)

        # Preparar o texto para geração de conclusões
        resultados_texto = f"Descrição do Histograma: {descricao_hist}"

        if debug:
            print("Texto para Geração de Conclusões: ", resultados_texto)

        # Gerar conclusões com base nos resultados e descrições
        carregar_conclusoes(analysis_id, nome_analise, resultados_texto, instrucoes)
    else:
        # Carregar conclusões existentes sem gerar novas descrições
        carregar_conclusoes(analysis_id, nome_analise)

