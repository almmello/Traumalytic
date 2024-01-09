import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.app_config.processo_app_config import (
    processar_app_config
)

from modulos.app_config.conteudo_app_config import (
    explicar_app_config
)

def mostrar_app_config():
    st.title("Configuração")

    explicar_app_config()
    processar_app_config()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_app_config()
