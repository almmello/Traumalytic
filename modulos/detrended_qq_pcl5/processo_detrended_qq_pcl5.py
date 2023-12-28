import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
)

from modulos.detrended_qq_pcl5.calculo_detrended_qq_pcl5 import (
    criar_detrended_qq_pcl5
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_detrended_qq_pcl5():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'detrended_qq_pcl5'
    nome_analise = 'Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PCL-5'
    instrucoes = "Analisando os resultados da Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
    prompt_plot = "Descreva o Gráfico de Probabilidade Normal (Q-Q) Sem Tendência para os escores do PCL-5. Este gráfico é utilizado para avaliar a normalidade dos dados, removendo tendências lineares para uma análise mais precisa. Observe como os pontos no gráfico se alinham em relação à linha diagonal, que representa a distribuição normal ideal. Avalie se os pontos seguem uma linha reta, o que indicaria que os escores estão distribuídos normalmente. Identifique qualquer desvio significativo dos pontos em relação à linha, como padrões de agrupamento ou dispersão, e discuta o que esses desvios podem revelar sobre a distribuição dos escores de estresse pós-traumático na amostra. Destaque a presença de assimetria ou outliers e suas implicações para a interpretação dos dados do PCL-5."


   # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    st.write(nome_analise)

    # Gerar e mostrar os gráficos para os dados do usuário
    fig = criar_detrended_qq_pcl5(st.session_state['data'])
    st.pyplot(fig)
    plt.close(fig)


    # Verificar se já existe uma conclusão armazenada
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:

        # Processar a visão dos gráficos caso não existam conclusões anteriores
        descricao_plot = processar_visao_imagem(fig, prompt_plot)

        # Preparar o texto para geração de conclusões
        resultados_texto = f"Descrição do {nome_analise} {descricao_plot}"

        if debug:
            print("Texto para Geração de Conclusões: ", resultados_texto)

        # Gerar conclusões com base nos resultados e descrições
        carregar_conclusoes(analysis_id, nome_analise, resultados_texto, instrucoes)
    else:
        # Carregar conclusões existentes sem gerar novas descrições
        carregar_conclusoes(analysis_id, nome_analise)

