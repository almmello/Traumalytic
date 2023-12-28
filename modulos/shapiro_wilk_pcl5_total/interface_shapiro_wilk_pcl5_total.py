import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.shapiro_wilk_pcl5_total.processo_shapiro_wilk_pcl5_total import (
    processar_shapiro_wilk_pcl5_total
)

from modulos.shapiro_wilk_pcl5_total.conteudo_shapiro_wilk_pcl5_total import (
    explicar_shapiro_wilk_pcl5_total
)

def mostrar_shapiro_wilk_pcl5_total():
    st.title("Teste de Shapiro-Wilk para PCL-5 Total")

    explicar_shapiro_wilk_pcl5_total()
    processar_shapiro_wilk_pcl5_total()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_shapiro_wilk_pcl5_total()
