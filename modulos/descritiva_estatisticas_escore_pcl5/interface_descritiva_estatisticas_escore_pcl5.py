import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_estatisticas_escore_pcl5.processo_descritiva_estatisticas_escore_pcl5 import (
    processar_descritiva_estatisticas_escore_pcl5
)

from modulos.descritiva_estatisticas_escore_pcl5.conteudo_descritiva_estatisticas_escore_pcl5 import (
    explicar_descritiva_estatisticas_escore_pcl5
)

def mostrar_descritiva_estatisticas_escore_pcl5():
    st.title("Estatísticas do Escore Total PCL-5")

    explicar_descritiva_estatisticas_escore_pcl5()
    processar_descritiva_estatisticas_escore_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_descritiva_estatisticas_escore_pcl5()
