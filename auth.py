import streamlit as st
from dotenv import load_dotenv
import os

# Em seu módulo específico
import logging

# Obter um logger para o módulo atual
logger = logging.getLogger(__name__)

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Usuário e senha carregados do arquivo .env
APP_USER = os.getenv("ENV_USER")
APP_PASSWORD = os.getenv("ENV_PASSWORD")

def mostrar_tela_login():
    """
    Mostra a tela de login e verifica as credenciais.
    """
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Usuário", autocomplete="username")
    password = st.sidebar.text_input("Senha", type="password", autocomplete="current-password")
    logger.debug(f"Usuário Esperado: {APP_USER}")
    logger.debug(f"Senha Esperada: {APP_PASSWORD}")

    if st.sidebar.button("Entrar"):
        if username == APP_USER and password == APP_PASSWORD:
            return True
        else:
            st.sidebar.error("Usuário ou senha incorretos.")
            logger.debug(f"Usuário Inserido: {username}")
            logger.debug(f"Senha Inserida: {password}")
            return False
    return False
