import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.tstudent_sexo_clusters_ptci.processo_tstudent_sexo_clusters_ptci import (
    processar_tstudent_sexo_clusters_ptci
)

from modulos.tstudent_sexo_clusters_ptci.conteudo_tstudent_sexo_clusters_ptci import (
    explicar_tstudent_sexo_clusters_ptci
)

def mostrar_tstudent_sexo_clusters_ptci():
    st.title("Teste t de Student - Sexo vs Clusters do PTCI")

    explicar_tstudent_sexo_clusters_ptci()
    processar_tstudent_sexo_clusters_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_tstudent_sexo_clusters_ptci()
