import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.visualizacao_itens_clusters_pcl5.processo_visualizacao_itens_clusters_pcl5 import (
    exibir_clusters_pcl5,
)

from modulos.visualizacao_itens_clusters_pcl5.conteudo_visualizacao_itens_clusters_pcl5 import (
    explicar_visualizacao_itens_pcl5,
)

def mostrar_visualizacao_itens_clusters_pcl5():
    st.title("Visualização dos Itens do PCL-5")

    explicar_visualizacao_itens_pcl5()
    exibir_clusters_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_visualizacao_itens_clusters_pcl5()
