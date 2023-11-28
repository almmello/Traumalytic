import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.analise_descritiva.processo_analise_descritiva import (
    processar_exibir_clusters_ptci,
    processar_exibir_clusters_pcl5,
)

from modulos.analise_descritiva.conteudo_analise_descritiva import (
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
