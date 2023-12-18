import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_estatisticas_idade.processo_descritiva_estatisticas_idade import (
    processar_estatisticas_idade,
)

from modulos.descritiva_estatisticas_idade.conteudo_descritiva_estatisticas_idade import (
    explicar_estatisticas_idade,
)

def mostrar_descritiva_estatisticas_idade():
    st.title("Estatísticas de Idade")

    explicar_estatisticas_idade()
    processar_estatisticas_idade()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_descritiva_estatisticas_idade()


