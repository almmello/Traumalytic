import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_medidas_tendencia.processo_descritiva_medidas_tendencia import (
    processar_descritiva_medidas_tendencia
)

from modulos.descritiva_medidas_tendencia.conteudo_descritiva_medidas_tendencia import (
    explicar_descritiva_medidas_tendencia
)

def mostrar_descritiva_medidas_tendencia():
    st.title("Medidas de Tendência Central")

    explicar_descritiva_medidas_tendencia()
    processar_descritiva_medidas_tendencia()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_descritiva_medidas_tendencia()
