import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
)

from modulos.boxplot_pcl5.calculo_boxplot_pcl5 import (
    criar_boxplot_pcl5
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_boxplot_pcl5():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'boxplot_pcl5'
    nome_analise = 'Gráfico Boxplot do PCL-5'
    instrucoes = "Analisando os resultados da Gráfico Boxplot do PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
    prompt_plot = "Descreva os elementos-chave do gráfico, incluindo a posição da mediana, a amplitude dos quartis, a presença de outliers e a simetria da distribuição. Discuta o que essas características visuais podem sugerir sobre a variabilidade e a tendência central dos escores do PCL-5 na amostra estudada. Avalie se a distribuição parece ser normal, inclinada para a esquerda ou para a direita, e quais implicações isso pode ter para a interpretação dos resultados em um contexto de estresse pós-traumático."



    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    st.write('Gráfico Boxplot do PCL-5:')

    # Gerar e mostrar os gráficos para os dados do usuário
    fig = criar_boxplot_pcl5(st.session_state['data'])
    st.pyplot(fig)
    plt.close(fig)


    # Verificar se já existe uma conclusão armazenada
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:

        # Processar a visão dos gráficos caso não existam conclusões anteriores
        descricao_plot = processar_visao_imagem(fig, prompt_plot)

        # Preparar o texto para geração de conclusões
        resultados_texto = f"Descrição do {nome_analise}: {descricao_plot}"

        if debug:
            print("Texto para Geração de Conclusões: ", resultados_texto)

        # Gerar conclusões com base nos resultados e descrições
        carregar_conclusoes(analysis_id, nome_analise, resultados_texto, instrucoes)
    else:
        # Carregar conclusões existentes sem gerar novas descrições
        carregar_conclusoes(analysis_id, nome_analise)
