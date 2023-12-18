import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_estatisticas_itens_ptci.processo_descritiva_estatisticas_itens_ptci import (
    processar_descritiva_estatisticas_itens_ptci
)

from modulos.descritiva_estatisticas_itens_ptci.conteudo_descritiva_estatisticas_itens_ptci import (
    explicar_descritiva_estatisticas_itens_ptci
)

def mostrar_descritiva_estatisticas_itens_ptci():
    st.title("Estatísticas dos Itens do PTCI")

    explicar_descritiva_estatisticas_itens_ptci()
    processar_descritiva_estatisticas_itens_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_descritiva_estatisticas_itens_ptci()
