import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.detrended_qq_ptci.processo_detrended_qq_ptci import (
    processar_detrended_qq_ptci
)

from modulos.detrended_qq_ptci.conteudo_detrended_qq_ptci import (
    explicar_detrended_qq_ptci
)

def mostrar_detrended_qq_ptci():
    st.title("Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PTCI")

    explicar_detrended_qq_ptci()
    processar_detrended_qq_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_detrended_qq_ptci()
