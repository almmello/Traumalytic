import streamlit as st
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Usuário e senha carregados do arquivo .env
APP_USER = os.getenv("ENV_USER")
APP_PASSWORD = os.getenv("ENV_PASSWORD")

# Função para ativar o modo de debug (remova ou defina como False em produção)
DEBUG_MODE = False

def mostrar_tela_login():
    """
    Mostra a tela de login e verifica as credenciais.
    """
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Usuário")
    password = st.sidebar.text_input("Senha", type="password")

    # Modo debug para diagnóstico
    if DEBUG_MODE:
        st.sidebar.write("Modo Debug Ativado")
        st.sidebar.write(f"Usuário Esperado: {APP_USER}")
        st.sidebar.write(f"Senha Esperada: {APP_PASSWORD}")

    if st.sidebar.button("Entrar"):
        if username == APP_USER and password == APP_PASSWORD:
            return True
        else:
            st.sidebar.error("Usuário ou senha incorretos.")
            if DEBUG_MODE:
                st.sidebar.write(f"Usuário Inserido: {username}")
                st.sidebar.write(f"Senha Inserida: {password}")
            return False
    return False
