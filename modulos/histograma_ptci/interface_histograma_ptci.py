import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.histograma_ptci.processo_histograma_ptci import (
    processar_histograma_ptci
)

from modulos.histograma_ptci.conteudo_histograma_ptci import (
    explicar_histograma_ptci
)

def mostrar_histograma_ptci():
    st.title("Gráfico Histograma PTCI")

    explicar_histograma_ptci()
    processar_histograma_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_histograma_ptci()
