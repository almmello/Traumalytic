import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.tstudent_sexo_clusters_pcl5.processo_tstudent_sexo_clusters_pcl5 import (
    processar_tstudent_sexo_clusters_pcl5
)

from modulos.tstudent_sexo_clusters_pcl5.conteudo_tstudent_sexo_clusters_pcl5 import (
    explicar_tstudent_sexo_clusters_pcl5
)

def mostrar_tstudent_sexo_clusters_pcl5():
    st.title("Teste t de Student - Sexo vs Clusters do PCL-5")

    explicar_tstudent_sexo_clusters_pcl5()
    processar_tstudent_sexo_clusters_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_tstudent_sexo_clusters_pcl5()
