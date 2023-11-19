import streamlit as st
from .processo_teste_t_student import (
    processar_teste_t_student_sexo_ptci_total,
    processar_teste_t_student_sexo_clusters_ptci
)

def mostrar_teste_t_student():
    st.title("Teste t de Student")

    # Botão para realizar o teste t de Student comparando Sexo e Escore Total do PTCI
    if st.button('Teste t de Student - Sexo vs Escore Total do PTCI'):
        processar_teste_t_student_sexo_ptci_total()

    # Botão para realizar o teste t de Student para cada cluster do PTCI
    if st.button('Teste t de Student - Sexo vs Clusters do PTCI'):
        processar_teste_t_student_sexo_clusters_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_teste_t_student()
