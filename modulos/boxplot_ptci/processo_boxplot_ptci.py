import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
)

from modulos.boxplot_ptci.calculo_boxplot_ptci import (
    criar_boxplot_ptci
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_boxplot_ptci():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'boxplot_ptci'
    nome_analise = 'Gráfico Boxplot do PTCI'
    instrucoes = "Analisando os resultados da Gráfico Boxplot do PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
    prompt_plot = "Analise visualmente o Boxplot gerado para os escores do Inventário de Cognições Pós-Traumáticas (PTCI). Descreva os elementos principais do gráfico, como a localização da mediana, a distribuição dos quartis, a presença e significado de possíveis outliers e a simetria da distribuição dos escores. Discuta o que essas características indicam sobre a variabilidade e centralidade dos escores do PTCI na amostra de estudo. Avalie se a distribuição dos escores sugere normalidade ou inclinação (para a esquerda ou direita), e explore as possíveis implicações desses padrões na compreensão das experiências traumáticas dos participantes."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    st.write('Gráfico Boxplot do PTCI:')

    # Gerar e mostrar os gráficos para os dados do usuário
    fig = criar_boxplot_ptci(st.session_state['data'])
    st.pyplot(fig)
    plt.close(fig)


    # Verificar se já existe uma conclusão armazenada
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:

        # Processar a visão dos gráficos caso não existam conclusões anteriores
        descricao_plot = processar_visao_imagem(fig, prompt_plot)

        # Preparar o texto para geração de conclusões
        resultados_texto = f"Descrição do Boxplot: {descricao_plot}"

        if debug:
            print("Texto para Geração de Conclusões: ", resultados_texto)

        # Gerar conclusões com base nos resultados e descrições
        carregar_conclusoes(analysis_id, nome_analise, resultados_texto, instrucoes)
    else:
        # Carregar conclusões existentes sem gerar novas descrições
        carregar_conclusoes(analysis_id, nome_analise)