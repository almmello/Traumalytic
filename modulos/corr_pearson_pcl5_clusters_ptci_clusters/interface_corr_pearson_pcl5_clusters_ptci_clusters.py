import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.corr_pearson_pcl5_clusters_ptci_clusters.processo_corr_pearson_pcl5_clusters_ptci_clusters import (
    processar_corr_pearson_pcl5_clusters_ptci_clusters
)

from modulos.corr_pearson_pcl5_clusters_ptci_clusters.conteudo_corr_pearson_pcl5_clusters_ptci_clusters import (
    explicar_corr_pearson_pcl5_clusters_ptci_clusters
)

def mostrar_corr_pearson_pcl5_clusters_ptci_clusters():
    st.title("Correlação Paramétrica entre os Clusters do PCL5 e PTCI")

    explicar_corr_pearson_pcl5_clusters_ptci_clusters()
    processar_corr_pearson_pcl5_clusters_ptci_clusters()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_corr_pearson_pcl5_clusters_ptci_clusters()
