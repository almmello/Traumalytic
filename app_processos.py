import streamlit as st
from data_loader import DataLoader
from app_conteudo import explicar_filtro_idade, explicar_filtro_pcti, explicar_filtro_pcl5


def mostrar_dados_analise():
    st.title("Dados da Análise")

    explicar_filtro_idade()
    min_age, max_age = st.slider("Selecione a faixa etária:", 0, 100, (18, 65), 1)

    # Novos combo boxes para seleção de filtros
    explicar_filtro_pcti()
    remover_nulos_pcti = st.checkbox("Remover linhas com dados nulos no questionário PCTI")

    explicar_filtro_pcl5()
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