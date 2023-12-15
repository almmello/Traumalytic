import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_estatisticas_escore_ptci.processo_descritiva_estatisticas_escore_ptci import (
    processar_descritiva_estatisticas_escore_ptci
)

from modulos.descritiva_estatisticas_escore_ptci.conteudo_descritiva_estatisticas_escore_ptci import (
    explicar_descritiva_estatisticas_escore_ptci
)

def mostrar_descritiva_estatisticas_escore_ptci():
    st.title("Estatísticas do Escore Total PTCI")

    explicar_descritiva_estatisticas_escore_ptci()
    processar_descritiva_estatisticas_escore_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_descritiva_estatisticas_escore_ptci()
