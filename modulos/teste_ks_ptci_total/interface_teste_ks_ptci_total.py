import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.teste_ks_ptci_total.processo_teste_ks_ptci_total import (
    processar_teste_ks_ptci_total
)

from modulos.teste_ks_ptci_total.conteudo_teste_ks_ptci_total import (
    explicar_teste_ks_ptci_total
)

def mostrar_teste_ks_ptci_total():
    st.title("Teste Kolmogorov-Smirnov para PTCI Total")

    explicar_teste_ks_ptci_total()
    processar_teste_ks_ptci_total()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_teste_ks_ptci_total()
