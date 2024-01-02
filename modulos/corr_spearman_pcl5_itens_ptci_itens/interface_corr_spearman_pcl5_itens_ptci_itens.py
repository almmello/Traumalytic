import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.corr_spearman_pcl5_itens_ptci_itens.processo_corr_spearman_pcl5_itens_ptci_itens import (
    processar_corr_spearman_pcl5_itens_ptci_itens
)

from modulos.corr_spearman_pcl5_itens_ptci_itens.conteudo_corr_spearman_pcl5_itens_ptci_itens import (
    explicar_corr_spearman_pcl5_itens_ptci_itens
)

def mostrar_corr_spearman_pcl5_itens_ptci_itens():
    st.title("Correlação Spearman entre os Itens do PCL5 e PTCI")

    explicar_corr_spearman_pcl5_itens_ptci_itens()
    processar_corr_spearman_pcl5_itens_ptci_itens()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_corr_spearman_pcl5_itens_ptci_itens()
