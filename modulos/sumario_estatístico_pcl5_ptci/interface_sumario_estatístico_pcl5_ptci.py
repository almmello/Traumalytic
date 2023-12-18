import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.sumario_estatístico_pcl5_ptci.processo_sumario_estatístico_pcl5_ptci import (
    processar_sumario_estatístico_pcl5_ptci
)

from modulos.sumario_estatístico_pcl5_ptci.conteudo_sumario_estatístico_pcl5_ptci import (
    explicar_sumario_validade_pcl5_ptci
)

def mostrar_sumario_estatístico_pcl5_ptci():
    st.title("Sumário Estatístico do PCL-5 e PTCI")

    explicar_sumario_validade_pcl5_ptci()
    processar_sumario_estatístico_pcl5_ptci()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_sumario_estatístico_pcl5_ptci()
