import streamlit as st
from data_loader import DataLoader

from modulos.visualizacao_itens_clusters_ptci.calculo_visualizacao_itens_clusters_ptci import (
    mostrar_apenas_clusters_ptci,
    calcular_clusters_ptci,
)

# Função para carregar os dados uma única vez
def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def exibir_clusters_ptci():
    carregar_dados()
    st.session_state['ptci_clusters'] = mostrar_apenas_clusters_ptci(st.session_state['data'])
    st.write(st.session_state['ptci_clusters'])

def processar_clusters_ptci():
    carregar_dados()
    st.session_state['ptci_clusters_calculos'] = calcular_clusters_ptci(st.session_state['data'])
    st.write(st.session_state['ptci_clusters_calculos'])
