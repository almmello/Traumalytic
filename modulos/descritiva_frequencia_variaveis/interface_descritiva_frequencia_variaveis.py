import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.descritiva_frequencia_variaveis.processo_descritiva_frequencia_variaveis import (
    processar_descritiva_frequencia_variaveis
)

from modulos.descritiva_frequencia_variaveis.conteudo_descritiva_frequencia_variaveis import (
    explicar_descritiva_frequencia_variaveis
)

def mostrar_descritiva_frequencia_variaveis():
    st.title("Frequência de Variáveis Categóricas")

    explicar_descritiva_frequencia_variaveis()
    processar_descritiva_frequencia_variaveis()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_descritiva_frequencia_variaveis()
