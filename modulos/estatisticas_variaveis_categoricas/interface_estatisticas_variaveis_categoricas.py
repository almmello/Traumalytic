import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.estatisticas_variaveis_categoricas.processo_estatisticas_variaveis_categoricas import (
    processar_estatisticas_variaveis_categoricas
)

from modulos.estatisticas_variaveis_categoricas.conteudo_estatisticas_variaveis_categoricas import (
    explicar_estatisticas_variaveis_categoricas
)

def mostrar_estatisticas_variaveis_categoricas():
    st.title("Estatísticas de Variáveis Categóricas")

    explicar_estatisticas_variaveis_categoricas()
    processar_estatisticas_variaveis_categoricas()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_estatisticas_variaveis_categoricas()
