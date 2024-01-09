import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.e1_preparacao_dados_b.processo_e1_preparacao_dados_b import (
    processar_e1_preparacao_dados_b
)

from modulos.e1_preparacao_dados_b.conteudo_e1_preparacao_dados_b import (
    explicar_e1_preparacao_dados_b
)

def mostrar_e1_preparacao_dados_b():
    st.title("Preparação dos Dados da Grandeza B")

    explicar_e1_preparacao_dados_b()
    processar_e1_preparacao_dados_b()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_e1_preparacao_dados_b()
