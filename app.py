import streamlit as st
from auth import mostrar_tela_login

# Importações dos módulos
from modulos.analise_descritiva.interface_analise_descritiva import mostrar_analise_descritiva
from modulos.analise_normalidade.interface_analise_normalidade import mostrar_analise_normalidade
from modulos.analise_correlacao.interface_analise_correlacao import mostrar_analise_correlacao
from modulos.teste_t_student.interface_teste_t_student import mostrar_teste_t_student


def main():
    # Inicialização das variáveis de sessão
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'pagina_atual' not in st.session_state:
        st.session_state['pagina_atual'] = 'home'

    # Mostrar tela de login
    if not st.session_state['logged_in']:
        st.session_state['logged_in'] = mostrar_tela_login()
        if st.session_state['logged_in']:
            st.rerun()

    # Sidebar e Navegação
    if st.session_state['logged_in']:
        st.sidebar.title("Menu")
        if st.sidebar.button("Análise Descritiva"):
            st.session_state['pagina_atual'] = 'analise_descritiva'
        if st.sidebar.button("Análise de Normalidade"):
            st.session_state['pagina_atual'] = 'analise_normalidade'
        if st.sidebar.button("Análise de Correlação"):
            st.session_state['pagina_atual'] = 'analise_correlacao'
        if st.sidebar.button("Teste t de Student"):
            st.session_state['pagina_atual'] = 'teste_t_student'

        # Exibição de Conteúdo Baseado na Página Atual
        if st.session_state['pagina_atual'] == 'home':
            st.title("Bem-vindo à Aplicação")
        elif st.session_state['pagina_atual'] == 'analise_descritiva':
            mostrar_analise_descritiva()
        elif st.session_state['pagina_atual'] == 'analise_normalidade':
            mostrar_analise_normalidade()
        elif st.session_state['pagina_atual'] == 'analise_correlacao':
            mostrar_analise_correlacao()
        elif st.session_state['pagina_atual'] == 'teste_t_student':
            mostrar_teste_t_student()

if __name__ == "__main__":
    main()
