import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.analise_descritiva.processo_analise_descritiva import (
    processar_estatisticas_idade,
)

from modulos.analise_descritiva.conteudo_analise_descritiva import (
    explicar_estatisticas_idade,
)

def mostrar_estatisticas_idade():
    st.title("Estatísticas de Idade")

    explicar_estatisticas_idade()
    processar_estatisticas_idade()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_estatisticas_idade()


