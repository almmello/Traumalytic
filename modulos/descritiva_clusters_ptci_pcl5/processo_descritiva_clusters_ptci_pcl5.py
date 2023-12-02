import streamlit as st
import pandas as pd
from data_loader import DataLoader
from modulos.descritiva_clusters_ptci_pcl5.calculo_descritiva_clusters_ptci_pcl5 import (
    calcular_clusters_ptci, 
    calcular_clusters_pcl5, 
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

