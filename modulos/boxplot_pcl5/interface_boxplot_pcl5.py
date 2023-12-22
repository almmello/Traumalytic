import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.boxplot_pcl5.processo_boxplot_pcl5 import (
    processar_boxplot_pcl5
)

from modulos.boxplot_pcl5.conteudo_boxplot_pcl5 import (
    explicar_boxplot_pcl5
)

def mostrar_boxplot_pcl5():
    st.title("Gráfico Boxplot do PCL-5")

    explicar_boxplot_pcl5()
    processar_boxplot_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_boxplot_pcl5()
