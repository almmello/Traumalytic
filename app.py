import streamlit as st
from auth import mostrar_tela_login
from sidemenu import create_sidebar
from data_loader import DataLoader
from supabase_manager import SupabaseManager  # Import the SupabaseManager

def main():

    # Inicialização das variáveis de sessão com valores do arquivo de configuração
    data_loader = DataLoader()
    data_loader.load_state_from_config()
    st.session_state['data'] = data_loader.carregar_dados()

    # Mostrar tela de login
    if not st.session_state['logged_in']:
        st.session_state['logged_in'] = mostrar_tela_login()
        if st.session_state['logged_in']:
            st.rerun()

    # Criar sidebar e gerenciar navegação
    if st.session_state['logged_in']:
        create_sidebar()

if __name__ == "__main__":
    main()
