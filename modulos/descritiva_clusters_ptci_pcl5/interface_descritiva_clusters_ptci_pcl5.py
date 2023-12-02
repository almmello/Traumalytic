import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_clusters_ptci_pcl5.processo_descritiva_clusters_ptci_pcl5 import (
    processar_exibir_clusters_ptci,
    processar_exibir_clusters_pcl5,
)

from modulos.descritiva_clusters_ptci_pcl5.conteudo_descritiva_clusters_ptci_pcl5 import (
    explicar_clusters_ptci,
    explicar_clusters_pcl5,
)

def mostrar_clusters():
    st.title("Clusters PTCI e PCL-5")

    explicar_clusters_ptci()
    processar_exibir_clusters_ptci()

    explicar_clusters_pcl5()
    processar_exibir_clusters_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_clusters()
