import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.detrended_qq_pcl5.processo_detrended_qq_pcl5 import (
    processar_detrended_qq_pcl5
)

from modulos.detrended_qq_pcl5.conteudo_detrended_qq_pcl5 import (
    explicar_detrended_qq_pcl5
)

def mostrar_detrended_qq_pcl5():
    st.title("Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PCL-5")

    explicar_detrended_qq_pcl5()
    processar_detrended_qq_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_detrended_qq_pcl5()
