import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
)

from modulos.probabilidade_normal_ptci.calculo_probabilidade_normal_ptci import (
    criar_probabilidade_normal_ptci
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_probabilidade_normal_ptci():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'probabilidade_normal_ptci'
    nome_analise = 'Gráfico de Probabilidade Normal do PTCI'
    instrucoes = "Analisando os resultados da Gráfico de Probabilidade Normal do PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
    prompt_plot = "Analise o Gráfico de Probabilidade Normal para os escores do Inventário de Cognições Pós-Traumáticas (PTCI). Comente sobre a aderência dos pontos à linha reta teórica que representa uma distribuição normal. Identifique se os pontos seguem uma linha reta ou se há desvios significativos, o que indicaria a presença de assimetria ou outliers nos dados. Reflita sobre o que a forma do gráfico sugere acerca da distribuição dos escores de cognições pós-traumáticas e considere as possíveis interpretações psicológicas desses achados em relação à experiência de trauma nos participantes."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    st.write(nome_analise)

    # Gerar e mostrar os gráficos para os dados do usuário
    fig = criar_probabilidade_normal_ptci(st.session_state['data'])
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
