import streamlit as st
import pandas as pd
from auth import mostrar_tela_login
from data_loader import DataLoader

# Importações dos módulos
from modulos.analise_descritiva.interface_analise_descritiva import mostrar_analise_descritiva
from modulos.analise_normalidade.interface_analise_normalidade import mostrar_analise_normalidade
from modulos.analise_correlacao.interface_analise_correlacao import mostrar_analise_correlacao
from modulos.teste_t_student.interface_teste_t_student import mostrar_teste_t_student


def mostrar_dados_analise():
    st.title("Dados da Análise")
    min_age, max_age = st.slider("Selecione a faixa etária:", 0, 100, (18, 60), 1)

    # Novos combo boxes para seleção de filtros
    remover_nulos_pcti = st.checkbox("Remover linhas com dados nulos no questionário PCTI")
    remover_nulos_pcl5 = st.checkbox("Remover linhas com resultados nulos no PCL-5")

    if st.button('Aplicar Filtro'):
        st.session_state['min_age'] = min_age
        st.session_state['max_age'] = max_age
        st.session_state['remover_nulos_pcti'] = remover_nulos_pcti
        st.session_state['remover_nulos_pcl5'] = remover_nulos_pcl5
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()
        st.session_state['filtro_aplicado'] = True
        st.success("Filtros aplicados com sucesso.")
    
    if st.session_state.get('filtro_aplicado', False):
        st.session_state['filtro_aplicado'] = False



def main():
    # Inicialização das variáveis de sessão
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'pagina_atual' not in st.session_state:
        st.session_state['pagina_atual'] = 'home'
    if 'data' not in st.session_state:
        st.session_state['data'] = pd.DataFrame(columns=['IDADE', 'SEXO', 'INSTRUCAO'])  # Colunas como exemplo


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
            st.title("Bem-vindo à Aplicação")
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
