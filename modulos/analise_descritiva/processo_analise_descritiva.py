import streamlit as st
from data_loader import DataLoader
from .calculo_analise_descritiva import (
    calcular_clusters_ptci, 
    calcular_clusters_pcl5, 
    calcular_estatisticas, 
    calcular_escores_pcl5, 
    calcular_escores_ptci,
    calcular_estatisticas_clusters_pcl5,
    calcular_estatisticas_clusters_ptci,
    calcular_distribuicao_por_sexo
)

# Função para carregar os dados uma única vez
def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_exibir_clusters_ptci():
    carregar_dados()
    st.session_state['ptci_clusters'] = calcular_clusters_ptci(st.session_state['data'])
    st.write(st.session_state['ptci_clusters'])

def processar_exibir_clusters_pcl5():
    carregar_dados()
    st.session_state['pcl5_clusters'] = calcular_clusters_pcl5(st.session_state['data'])
    st.write(st.session_state['pcl5_clusters'])

def processar_estatisticas_idade():
    carregar_dados()
    estatisticas_idade = calcular_estatisticas(st.session_state['data'], 'IDADE')
    st.write('Estatísticas de Idade:', estatisticas_idade)

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

def processar_calculo_distribuicao_por_sexo():
    carregar_dados()
    distribuicao_sexo = calcular_distribuicao_por_sexo(st.session_state['data'])
    st.write('Distribuição Porcentual por Sexo:', distribuicao_sexo)
