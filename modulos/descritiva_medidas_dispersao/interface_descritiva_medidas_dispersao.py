import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_medidas_dispersao.processo_descritiva_medidas_dispersao import (
    processar_descritiva_medidas_dispersao
)

from modulos.descritiva_medidas_dispersao.conteudo_descritiva_medidas_dispersao import (
    explicar_descritiva_medidas_dispersao
)

def mostrar_descritiva_medidas_dispersao():
    st.title("Medidas de Dispersão")

    explicar_descritiva_medidas_dispersao()
    processar_descritiva_medidas_dispersao()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_descritiva_medidas_dispersao()
