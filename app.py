import streamlit as st
import pandas as pd
from auth import mostrar_tela_login


# Importações dos módulos
from modulos.analise_descritiva.interface_analise_descritiva import mostrar_analise_descritiva
from modulos.analise_normalidade.interface_analise_normalidade import mostrar_analise_normalidade
from modulos.analise_correlacao.interface_analise_correlacao import mostrar_analise_correlacao
from modulos.teste_t_student.interface_teste_t_student import mostrar_teste_t_student
from app_processos import mostrar_dados_analise
from app_conteudo import mostrar_conteudo


def main():
    # Inicialização das variáveis de sessão
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'pagina_atual' not in st.session_state:
        st.session_state['pagina_atual'] = 'home'
    if 'data' not in st.session_state:
        st.session_state['data'] = pd.DataFrame(columns=['IDADE', 'SEXO', 'INSTRUCAO'])  # Colunas como exemplo
    if 'min_age' not in st.session_state:
        st.session_state['min_age'] = 18  # Valor padrão para idade mínima
    if 'max_age' not in st.session_state:
        st.session_state['max_age'] = 60  # Valor padrão para idade máxima
    if 'remover_nulos_pcti' not in st.session_state:
        st.session_state['remover_nulos_pcti'] = True  # Valor padrão para o filtro PTCI
    if 'remover_nulos_pcl5' not in st.session_state:
        st.session_state['remover_nulos_pcl5'] = True  # Valor padrão para o filtro PCL-5

    # Mostrar tela de login
    if not st.session_state['logged_in']:
        st.session_state['logged_in'] = mostrar_tela_login()
        if st.session_state['logged_in']:
            st.rerun()

    # Sidebar e Navegação
    if st.session_state['logged_in']:
        st.sidebar.title("Menu")
        if st.sidebar.button("Dados da Análise"):
            st.session_state['pagina_atual'] = 'dados_analise'
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
            mostrar_conteudo()
        elif st.session_state['pagina_atual'] == 'analise_descritiva':
            mostrar_analise_descritiva()
        elif st.session_state['pagina_atual'] == 'analise_normalidade':
            mostrar_analise_normalidade()
        elif st.session_state['pagina_atual'] == 'analise_correlacao':
            mostrar_analise_correlacao()
        elif st.session_state['pagina_atual'] == 'teste_t_student':
            mostrar_teste_t_student()
        elif st.session_state['pagina_atual'] == 'dados_analise':
            mostrar_dados_analise()

if __name__ == "__main__":
    main()
