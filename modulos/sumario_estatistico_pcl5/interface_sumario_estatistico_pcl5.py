import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.sumario_estatistico_pcl5.processo_sumario_estatistico_pcl5 import (
    processar_sumario_estatistico_pcl5
)

from modulos.sumario_estatistico_pcl5.conteudo_sumario_estatistico_pcl5 import (
    explicar_sumario_validade_pcl5
)

def mostrar_sumario_estatistico_pcl5():
    st.title("Sumário Estatístico do PCL-5")

    explicar_sumario_validade_pcl5()
    processar_sumario_estatistico_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_sumario_estatistico_pcl5()
