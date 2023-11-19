import streamlit as st
from .processo_analise_correlacao import (
    correlacao_escores_totais,
    correlacao_clusters,
    correlacao_sintomas_itens
)

from .conteudo_analise_correlacao import (
    explicar_correlacao_escores_totais,
    explicar_correlacao_clusters,
    explicar_correlacao_sintomas_itens
)

def mostrar_analise_correlacao():
    st.title("Análise de Correlação")

    explicar_correlacao_escores_totais()
    if st.button('Correlação entre escores totais da PCL-5 e PTCI'):
        correlacao_escores_totais()

    explicar_correlacao_clusters()
    if st.button('Correlações entre clusters da PCL-5 e PTCI'):
        correlacao_clusters()

    explicar_correlacao_sintomas_itens()
    if st.button('Correlações entre sintomas da PCL-5 e itens do PTCI'):
        correlacao_sintomas_itens()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_analise_correlacao()
