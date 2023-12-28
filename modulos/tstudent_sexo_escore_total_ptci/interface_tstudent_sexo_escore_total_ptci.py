import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.tstudent_sexo_escore_total_ptci.processo_tstudent_sexo_escore_total_ptci import (
    processar_tstudent_sexo_escore_total_ptci
)

from modulos.tstudent_sexo_escore_total_ptci.conteudo_tstudent_sexo_escore_total_ptci import (
    explicar_tstudent_sexo_escore_total_ptci
)

def mostrar_tstudent_sexo_escore_total_ptci():
    st.title("Teste t de Student - Sexo vs Escore Total do PTCI")

    explicar_tstudent_sexo_escore_total_ptci()
    processar_tstudent_sexo_escore_total_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_tstudent_sexo_escore_total_ptci()
