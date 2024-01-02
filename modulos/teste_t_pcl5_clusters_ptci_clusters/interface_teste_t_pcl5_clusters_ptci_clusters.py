import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.teste_t_pcl5_clusters_ptci_clusters.processo_teste_t_pcl5_clusters_ptci_clusters import (
    processar_teste_t_pcl5_clusters_ptci_clusters
)

from modulos.teste_t_pcl5_clusters_ptci_clusters.conteudo_teste_t_pcl5_clusters_ptci_clusters import (
    explicar_teste_t_pcl5_clusters_ptci_clusters
)

def mostrar_teste_t_pcl5_clusters_ptci_clusters():
    st.title("Teste T Student entre os Clusters do PCL5 e PTCI")

    explicar_teste_t_pcl5_clusters_ptci_clusters()
    processar_teste_t_pcl5_clusters_ptci_clusters()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_teste_t_pcl5_clusters_ptci_clusters()
