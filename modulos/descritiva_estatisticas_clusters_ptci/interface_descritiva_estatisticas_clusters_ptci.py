import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_estatisticas_clusters_ptci.processo_descritiva_estatisticas_clusters_ptci import (
    processar_descritiva_estatisticas_clusters_ptci
)

from modulos.descritiva_estatisticas_clusters_ptci.conteudo_descritiva_estatisticas_clusters_ptci import (
    explicar_descritiva_estatisticas_clusters_ptci
)

def mostrar_descritiva_estatisticas_clusters_ptci():
    st.title("Estatísticas dos Clusters PTCI")

    explicar_descritiva_estatisticas_clusters_ptci()
    processar_descritiva_estatisticas_clusters_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_descritiva_estatisticas_clusters_ptci()
