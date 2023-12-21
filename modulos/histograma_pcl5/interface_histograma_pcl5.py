import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.histograma_pcl5.processo_histograma_pcl5 import (
    processar_histograma_pcl5
)

from modulos.histograma_pcl5.conteudo_histograma_pcl5 import (
    explicar_histograma_pcl5
)

def mostrar_histograma_pcl5():
    st.title("Histograma do PCL-5")

    explicar_histograma_pcl5()
    processar_histograma_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_histograma_pcl5()
