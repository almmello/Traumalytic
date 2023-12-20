import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.teste_ks_pcl5_total.processo_teste_ks_pcl5_total import (
    processar_teste_ks_pcl5_total
)

from modulos.teste_ks_pcl5_total.conteudo_teste_ks_pcl5_total import (
    explicar_teste_ks_pcl5_total
)

def mostrar_teste_ks_pcl5_total():
    st.title("Teste Kolmogorov-Smirnov para PCL-5 Total")

    explicar_teste_ks_pcl5_total()
    processar_teste_ks_pcl5_total()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_teste_ks_pcl5_total()
