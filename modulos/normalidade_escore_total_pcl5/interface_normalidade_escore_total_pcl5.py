import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.normalidade_escore_total_pcl5.processo_normalidade_escore_total_pcl5 import (
    processar_normalidade_escore_total_pcl5
)

from modulos.normalidade_escore_total_pcl5.conteudo_normalidade_escore_total_pcl5 import (
    explicar_normalidade_escore_total_pcl5
)

def mostrar_normalidade_escore_total_pcl5():
    st.title("Normalidade do escore total do PCL-5")

    explicar_normalidade_escore_total_pcl5()
    processar_normalidade_escore_total_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_normalidade_escore_total_pcl5()
