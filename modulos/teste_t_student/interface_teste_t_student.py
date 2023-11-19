import streamlit as st
from .processo_teste_t_student import (
    processar_teste_t_student_sexo_ptci_total,
    processar_teste_t_student_sexo_clusters_ptci
)

from .conteudo_teste_t_student import (
    explicar_teste_t_student_sexo_ptci_total,
    explicar_teste_t_student_sexo_clusters_ptci
)

def mostrar_teste_t_student():
    st.title("Teste t de Student")

    explicar_teste_t_student_sexo_ptci_total()
    if st.button('Teste t de Student - Sexo vs Escore Total do PTCI'):
        processar_teste_t_student_sexo_ptci_total()

    explicar_teste_t_student_sexo_clusters_ptci()
    if st.button('Teste t de Student - Sexo vs Clusters do PTCI'):
        processar_teste_t_student_sexo_clusters_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_teste_t_student()
