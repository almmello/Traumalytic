import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.probabilidade_normal_pcl5.processo_probabilidade_normal_pcl5 import (
    processar_probabilidade_normal_pcl5
)

from modulos.probabilidade_normal_pcl5.conteudo_probabilidade_normal_pcl5 import (
    explicar_probabilidade_normal_pcl5
)

def mostrar_probabilidade_normal_pcl5():
    st.title("Gráfico de Probabilidade Normal do PCL-5")

    explicar_probabilidade_normal_pcl5()
    processar_probabilidade_normal_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_probabilidade_normal_pcl5()
