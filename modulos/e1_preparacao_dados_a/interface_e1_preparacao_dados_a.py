import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.e1_preparacao_dados_a.processo_e1_preparacao_dados_a import (
    processar_e1_preparacao_dados_a
)

from modulos.e1_preparacao_dados_a.conteudo_e1_preparacao_dados_a import (
    explicar_e1_preparacao_dados_a
)

def mostrar_e1_preparacao_dados_a():
    st.title("Preparação dos Dados da Grandeza A")

    explicar_e1_preparacao_dados_a()
    processar_e1_preparacao_dados_a()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_e1_preparacao_dados_a()
