import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.probabilidade_normal_ptci.processo_probabilidade_normal_ptci import (
    processar_probabilidade_normal_ptci
)

from modulos.probabilidade_normal_ptci.conteudo_probabilidade_normal_ptci import (
    explicar_probabilidade_normal_ptci
)

def mostrar_probabilidade_normal_ptci():
    st.title("Gráfico de Probabilidade Normal do PTCI")

    explicar_probabilidade_normal_ptci()
    processar_probabilidade_normal_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_probabilidade_normal_ptci()
