import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.visualizacao_itens_clusters_ptci.processo_visualizacao_itens_clusters_ptci import (
    exibir_clusters_ptci,
    processar_clusters_ptci,
)

from modulos.visualizacao_itens_clusters_ptci.conteudo_visualizacao_itens_clusters_ptci import (
    explicar_visualizacao_itens_ptci,
    explicar_visualizacao_clusters_ptci
)

def mostrar_visualizacao_itens_clusters_ptci():
    st.title("Visualização dos Itens do PTCI")

    explicar_visualizacao_itens_ptci()
    exibir_clusters_ptci()
    explicar_visualizacao_clusters_ptci()
    processar_clusters_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_visualizacao_itens_clusters_ptci()
