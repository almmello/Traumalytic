import streamlit as st
from data_loader import DataLoader

from modulos.visualizacao_itens_clusters_pcl5.calculo_visualizacao_itens_clusters_pcl5 import (
    mostrar_apenas_clusters_pcl5,
    calcular_clusters_pcl5,
)

# Função para carregar os dados uma única vez
def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def exibir_clusters_pcl5():
    carregar_dados()
    st.session_state['pcl5_clusters'] = mostrar_apenas_clusters_pcl5(st.session_state['data'])
    st.write(st.session_state['pcl5_clusters'])

def processar_clusters_pcl5():
    carregar_dados()
    st.session_state['pcl5_clusters_calculos'] = calcular_clusters_pcl5(st.session_state['data'])
    st.write(st.session_state['pcl5_clusters_calculos'])

