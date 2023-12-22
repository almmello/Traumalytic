import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.caule_folhas_ptci.processo_caule_folhas_ptci import (
    processar_caule_folhas_ptci
)

from modulos.caule_folhas_ptci.conteudo_caule_folhas_ptci import (
    explicar_caule_folhas_ptci
)

def mostrar_caule_folhas_ptci():
    st.title("Exibição de Caule-e-Folhas do PTCI")

    explicar_caule_folhas_ptci()
    processar_caule_folhas_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_caule_folhas_ptci()
