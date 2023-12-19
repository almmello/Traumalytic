import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.sumario_estatistico_ptci.processo_sumario_estatistico_ptci import (
    processar_sumario_estatistico_ptci
)

from modulos.sumario_estatistico_ptci.conteudo_sumario_estatistico_ptci import (
    explicar_sumario_validade_ptci
)

def mostrar_sumario_estatistico_ptci():
    st.title("Sumário Estatístico do PTCI")

    explicar_sumario_validade_ptci()
    processar_sumario_estatistico_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_sumario_estatistico_ptci()
