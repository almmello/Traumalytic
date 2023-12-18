import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.corte_tept_pcl5.processo_corte_tept_pcl5 import (
    processar_corte_tept_pcl5
)

from modulos.corte_tept_pcl5.conteudo_corte_tept_pcl5 import (
    explicar_estatisticas_gerais_tept
)

def mostrar_corte_tept_pcl5():
    st.title("Análise de Frequência de Diagnóstico de TEPT com Ponto de Corte do PCL-5")

    explicar_estatisticas_gerais_tept()
    processar_corte_tept_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_corte_tept_pcl5()
