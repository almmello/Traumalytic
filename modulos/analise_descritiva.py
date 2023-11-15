import streamlit as st

# Importar a classe DataLoader do diretório pai
import sys
sys.path.append('..')  # Adiciona o diretório pai ao sys.path
from data_loader import DataLoader

from calculations import (
    calcular_clusters_ptci, 
    calcular_clusters_pcl5, 
    calcular_estatisticas, 
    calcular_escores_pcl5, 
    calcular_escores_ptci,
    calcular_clusters_ptci_e_retornar,
    calcular_clusters_pcl5_e_retornar,
    calcular_estatisticas_clusters_pcl5,
    calcular_estatisticas_clusters_ptci
)


def mostrar_analise_descritiva():
    st.title("Análise Descritiva")

    # Inicializar o DataLoader
    data_loader = DataLoader()

    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = data_loader.carregar_dados()

    # Botões e lógica para Análise Descritiva
    if st.button('Calcular Clusters PTCI'):
        st.session_state['data'] = calcular_clusters_ptci(st.session_state['data'])
        st.write(st.session_state['data'])

    if st.button('Calcular Clusters PCL-5'):
        st.session_state['data'] = calcular_clusters_pcl5(st.session_state['data'])
        st.write(st.session_state['data'])

    if st.button('Calcular Estatísticas de Idade'):
        estatisticas_idade = calcular_estatisticas(st.session_state['data'], 'IDADE')
        st.write('Estatísticas de Idade:', estatisticas_idade)

    if st.button('Calcular Estatísticas do Escore Total PCL-5'):
        estatisticas_pcl5_total = calcular_escores_pcl5(st.session_state['data'])
        st.write('Estatísticas do Escore Total PCL-5:', estatisticas_pcl5_total)

    if st.button('Calcular Estatísticas do Escore Total PTCI'):
        estatisticas_ptci_total = calcular_escores_ptci(st.session_state['data'])
        st.write('Estatísticas do Escore Total PTCI:', estatisticas_ptci_total)

    if st.button('Exibir Clusters PTCI'):
        ptci_clusters = calcular_clusters_ptci_e_retornar(st.session_state['data'])
        st.write(ptci_clusters)

    if st.button('Exibir Clusters PCL-5'):
        pcl5_clusters = calcular_clusters_pcl5_e_retornar(st.session_state['data'])
        st.write(pcl5_clusters)

    if st.button('Calcular Estatísticas dos Clusters PCL-5'):
        estatisticas_clusters_pcl5 = calcular_estatisticas_clusters_pcl5(st.session_state['data'])
        st.write('Estatísticas dos Clusters PCL-5:', estatisticas_clusters_pcl5)

    if st.button('Calcular Estatísticas dos Clusters PTCI'):
        estatisticas_clusters_ptci = calcular_estatisticas_clusters_ptci(st.session_state['data'])
        st.write('Estatísticas dos Clusters PTCI:', estatisticas_clusters_ptci)

# Chamada da função principal
if __name__ == "__main__":
    mostrar_analise_descritiva()
