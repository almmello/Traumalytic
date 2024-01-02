import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.corr_spearman_pcl5_total_ptci_total.processo_corr_spearman_pcl5_total_ptci_total import (
    processar_corr_spearman_pcl5_total_ptci_total
)

from modulos.corr_spearman_pcl5_total_ptci_total.conteudo_corr_spearman_pcl5_total_ptci_total import (
    explicar_corr_spearman_pcl5_total_ptci_total
)

def mostrar_corr_spearman_pcl5_total_ptci_total():
    st.title("Correlação Spearman entre PCL5 Total e PTCI Total")

    explicar_corr_spearman_pcl5_total_ptci_total()
    processar_corr_spearman_pcl5_total_ptci_total()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_corr_spearman_pcl5_total_ptci_total()
