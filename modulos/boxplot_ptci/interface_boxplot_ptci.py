import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.boxplot_ptci.processo_boxplot_ptci import (
    processar_boxplot_ptci
)

from modulos.boxplot_ptci.conteudo_boxplot_ptci import (
    explicar_boxplot_ptci
)

def mostrar_boxplot_ptci():
    st.title("Gráfico Boxplot do PTCI")

    explicar_boxplot_ptci()
    processar_boxplot_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_boxplot_ptci()
