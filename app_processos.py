import streamlit as st
from data_loader import DataLoader
from app_conteudo import explicar_filtro_idade, explicar_filtro_idade_nulos, explicar_filtro_pcti, explicar_filtro_pcl5


def mostrar_dados_analise():
    st.title("Dados da Análise")

    explicar_filtro_idade()
    min_age, max_age = st.slider("Selecione a faixa etária:", 0, 100, (st.session_state['min_age'], st.session_state['max_age']), 1)

    explicar_filtro_idade_nulos()
    remover_nulos_idade = st.checkbox("Remover linhas com idades nulas", st.session_state['remover_nulos_idade'])

    # Novos combo boxes para seleção de filtros
    explicar_filtro_pcti()
    remover_nulos_pcti = st.checkbox("Remover linhas com dados nulos no questionário PCTI", st.session_state['remover_nulos_pcti'])


    explicar_filtro_pcl5()
    remover_nulos_pcl5 = st.checkbox("Remover linhas com resultados nulos no PCL-5", st.session_state['remover_nulos_pcl5'])

    if st.button('Aplicar Filtro'):
        st.session_state['min_age'] = min_age
        st.session_state['max_age'] = max_age
        st.session_state['remover_nulos_idade'] = remover_nulos_idade
        st.session_state['remover_nulos_pcti'] = remover_nulos_pcti
        st.session_state['remover_nulos_pcl5'] = remover_nulos_pcl5
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()
        st.session_state['filtro_aplicado'] = True
        st.success("Filtros aplicados com sucesso.")
    
    if st.session_state.get('filtro_aplicado', False):
        st.session_state['filtro_aplicado'] = False


if __name__ == "__main__":
    mostrar_dados_analise()