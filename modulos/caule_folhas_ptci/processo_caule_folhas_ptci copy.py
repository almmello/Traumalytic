import streamlit as st
import os
from data_loader import DataLoader

from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
)

from modulos.caule_folhas_ptci.calculo_caule_folhas_ptci import (
    calcular_caule_folhas_ptci
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_caule_folhas_ptci():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'caule_folhas_ptci'
    nome_analise = 'Exibição de Caule-e-Folhas do PTCI'
    instrucoes = "Analisando os resultados da Exibição de Caule-e-Folhas do PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    fig_hist, ax = calcular_caule_folhas_ptci(st.session_state['data'])
    st.write('Exibição de Caule-e-Folhas do PTCI:')
    st.pyplot(fig_hist)

    # Verificar se já existe uma conclusão armazenada
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:

        # Processar a visão dos gráficos caso não existam conclusões anteriores
        prompt_hist = "Descrição do gráfico de caule-e-folhas dos valores totais do PTCI, representando a distribuição dos escores de trauma na amostra de dados. Explique as características da distribuição evidenciadas pelo gráfico, incluindo a frequência de ocorrência dos escores em diferentes intervalos e quaisquer padrões ou tendências observáveis na distribuição dos dados."

        descricao_hist = processar_visao_imagem(fig_hist, prompt_hist)

        # Preparar o texto para geração de conclusões
        resultados_texto = f"Descrição do Diagrama: {descricao_hist}"

        if debug:
            print("Texto para Geração de Conclusões: ", resultados_texto)

        # Gerar conclusões com base nos resultados e descrições
        carregar_conclusoes(analysis_id, nome_analise, resultados_texto, instrucoes)
    else:
        # Carregar conclusões existentes sem gerar novas descrições
        carregar_conclusoes(analysis_id, nome_analise)