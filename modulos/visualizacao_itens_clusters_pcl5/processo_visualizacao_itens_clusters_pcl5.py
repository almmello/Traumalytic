import streamlit as st
from data_loader import DataLoader

def exibir_clusters_pcl5():
    data_loader = DataLoader()
    st.write(data_loader.carregar_dados("itens_pcl5"))



