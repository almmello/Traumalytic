import streamlit as st
from .processo_analise_normalidade import (
    realizar_teste_normalidade
)

def mostrar_analise_normalidade():
    st.title("Análise de Normalidade")

    # Opções de seleção para variáveis de interesse
    selected_var = st.selectbox("Selecione uma Variável", 
                                ['PCL5_total', 'PTCI_total', 
                                 'Cluster_A', 'Cluster_B', 
                                 'Cluster_C', 'Cluster_D', 'Cluster_E'])

    if st.button('Analisar'):
        # Processos relacionados à análise de normalidade
        realizar_teste_normalidade(selected_var)


# Chamada da função principal
if __name__ == "__main__":
    mostrar_analise_normalidade()

