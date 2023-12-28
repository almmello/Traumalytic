import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
)

from modulos.detrended_qq_ptci.calculo_detrended_qq_ptci import (
    criar_detrended_qq_ptci
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_detrended_qq_ptci():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'detrended_qq_ptci'
    nome_analise = 'Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PTCI'
    instrucoes = "Analisando os resultados da Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
    prompt_plot = "Descreva o Gráfico de Probabilidade Normal (Q-Q) Sem Tendência para os escores do PTCI. Este gráfico visualiza a adequação da distribuição dos escores do PTCI a uma distribuição normal teórica, removendo tendências lineares para focar na normalidade dos dados. Observe como os pontos se distribuem em relação à linha diagonal, que representa a distribuição normal ideal. Avalie se os pontos seguem uma trajetória linear, sugerindo uma distribuição normal dos escores. Identifique quaisquer padrões anormais ou desvios dos pontos da linha, tais como agrupamentos ou dispersões, e discuta suas possíveis implicações. Especial atenção deve ser dada à presença de assimetria ou outliers, e como isso pode afetar a interpretação dos resultados do PTCI em um contexto de cognições pós-traumáticas."


   # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    st.write(nome_analise)

    # Gerar e mostrar os gráficos para os dados do usuário
    fig = criar_detrended_qq_ptci(st.session_state['data'])
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
