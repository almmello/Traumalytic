import streamlit as st
import os
from data_loader import DataLoader

from modulos.descritiva_estatisticas_idade.calculo_descritiva_estatisticas_idade import (
    calcular_estatisticas,
)

from openai_interface import (
    carregar_conclusoes,
)

from supabase_manager import SupabaseManager

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_estatisticas_idade():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'descritiva_estatisticas_idade'
    nome_analise = 'Análise Descritiva'
    instrucoes = "Analisando os resultados da análise de estatísticas de idade, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    resultados = calcular_estatisticas(st.session_state['data'], 'IDADE')
    st.write('Estatísticas de Idade:', resultados)

    carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)


def processar_estatisticas_escore_total_pcl5():
    carregar_dados()
    estatisticas_pcl5_total = calcular_escores_pcl5(st.session_state['data'])
    st.write('Estatísticas do Escore Total PCL-5:', estatisticas_pcl5_total)

def processar_estatisticas_escore_total_ptci():
    carregar_dados()
    estatisticas_ptci_total = calcular_escores_ptci(st.session_state['data'])
    st.write('Estatísticas do Escore Total PTCI:', estatisticas_ptci_total)

def processar_estatisticas_clusters_pcl5():
    carregar_dados()
    estatisticas_clusters_pcl5 = calcular_estatisticas_clusters_pcl5(st.session_state['data'])
    st.write('Estatísticas dos Clusters PCL-5:', estatisticas_clusters_pcl5)

def processar_estatisticas_clusters_ptci():
    carregar_dados()
    estatisticas_clusters_ptci = calcular_estatisticas_clusters_ptci(st.session_state['data'])
    st.write('Estatísticas dos Clusters PTCI:', estatisticas_clusters_ptci)

def formatar_resultados(resultados):
    return pd.DataFrame(resultados, index=[0]).T.rename(columns={0: 'Valor'})

def processar_medidas_tendencia_central():
    carregar_dados()
    colunas_numericas = st.session_state['data'].select_dtypes(include='number').columns
    for coluna in colunas_numericas:
        resultados = calcular_medidas_tendencia_central(st.session_state['data'], coluna)
        st.subheader(f"Medidas de Tendência Central - {coluna}")
        st.table(formatar_resultados(resultados))

def processar_medidas_dispersao():
    carregar_dados()
    colunas_numericas = st.session_state['data'].select_dtypes(include='number').columns
    for coluna in colunas_numericas:
        resultados = calcular_medidas_dispersao(st.session_state['data'], coluna)
        st.subheader(f"Medidas de Dispersão - {coluna}")
        st.table(formatar_resultados(resultados))

def processar_frequencia_categoricas():
    carregar_dados()
    colunas_categoricas = st.session_state['data'].select_dtypes(include='object').columns
    for coluna in colunas_categoricas:
        resultados = calcular_frequencia_categoricas(st.session_state['data'], coluna)
        st.subheader(f"Frequência de Variáveis Categóricas - {coluna}")
        st.table(resultados)
