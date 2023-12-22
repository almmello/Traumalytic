import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.caule_folhas_pcl5.processo_caule_folhas_pcl5 import (
    processar_caule_folhas_pcl5
)

from modulos.caule_folhas_pcl5.conteudo_caule_folhas_pcl5 import (
    explicar_caule_folhas_pcl5
)

def mostrar_caule_folhas_pcl5():
    st.title("Exibição de Caule-e-Folhas do PCL5")

    explicar_caule_folhas_pcl5()
    processar_caule_folhas_pcl5()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_caule_folhas_pcl5()
