import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_estatisticas_escore_pcl5.processo_descritiva_estatisticas_escore_pcl5 import (
    processar_estatisticas_escore_total_pcl5,
)

from modulos.descritiva_estatisticas_escore_pcl5.conteudo_descritiva_estatisticas_escore_pcl5 import (
    explicar_estatisticas_escore_total_pcl5,
)


def mostrar_descritiva_estatisticas_escore_pcl5():
    st.title("Estatísticas de Idade")

    processar_estatisticas_escore_total_pcl5()
    explicar_estatisticas_escore_total_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_descritiva_estatisticas_escore_pcl5()


