# sidemenu.py
import streamlit as st

# Importações dos módulos das páginas
from app_interface import mostrar_conteudo as mostrar_home
from app_processos import mostrar_dados_analise as mostrar_configuracao
from modulos.visualizacao_itens_clusters_pcl5.interface_visualizacao_itens_clusters_pcl5 import mostrar_visualizacao_itens_clusters_pcl5
from modulos.visualizacao_itens_clusters_ptci.interface_visualizacao_itens_clusters_ptci import mostrar_visualizacao_itens_clusters_ptci
from modulos.descritiva_estatisticas_idade.interface_descritiva_estatisticas_idade import mostrar_descritiva_estatisticas_idade
from modulos.descritiva_estatisticas_itens_pcl5.interface_descritiva_estatisticas_itens_pcl5 import mostrar_descritiva_estatisticas_itens_pcl5
from modulos.descritiva_estatisticas_itens_ptci.interface_descritiva_estatisticas_itens_ptci import mostrar_descritiva_estatisticas_itens_ptci
from modulos.descritiva_estatisticas_clusters_pcl5.interface_descritiva_estatisticas_clusters_pcl5 import mostrar_descritiva_estatisticas_clusters_pcl5
from modulos.descritiva_estatisticas_clusters_ptci.interface_descritiva_estatisticas_clusters_ptci import mostrar_descritiva_estatisticas_clusters_ptci

def create_sidebar():
    st.sidebar.title("Traumalytics")
    if st.sidebar.button("Home"):
        st.session_state['pagina_atual'] = 'home'
    if st.sidebar.button("Configurações"):
        st.session_state['pagina_atual'] = 'configuracoes'

    st.sidebar.markdown("## Visualização dos Dados")
    if st.sidebar.button("Itens e Clusters do PCL-5"):
        st.session_state['pagina_atual'] = 'visualizacao_itens_clusters_pcl5'
    if st.sidebar.button("Itens e Clusters do PTCI"):
        st.session_state['pagina_atual'] = 'visualizacao_itens_clusters_ptci'
    st.sidebar.markdown("## Análise Descritiva")
    if st.sidebar.button("Idade"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_idade'
    if st.sidebar.button("Itens do PCL5"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_itens_pcl5'
    if st.sidebar.button("Itens do PTCI"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_itens_ptci'
    if st.sidebar.button("Clusters e Escore Total do PCL-5"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_clusters_pcl5'
    if st.sidebar.button("Clusters e Escore Total do PTCI"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_clusters_ptci'


    # Exibição de Conteúdo Baseado na Página Atual
    if st.session_state['pagina_atual'] == 'home':
        mostrar_home()
    elif st.session_state['pagina_atual'] == 'configuracoes':
        mostrar_configuracao()
    elif st.session_state['pagina_atual'] == 'visualizacao_itens_clusters_pcl5':
        mostrar_visualizacao_itens_clusters_pcl5()
    elif st.session_state['pagina_atual'] == 'visualizacao_itens_clusters_ptci':
        mostrar_visualizacao_itens_clusters_ptci()
    elif st.session_state['pagina_atual'] == 'descritiva_estatisticas_idade':
        mostrar_descritiva_estatisticas_idade()
    elif st.session_state['pagina_atual'] == 'descritiva_estatisticas_itens_pcl5':
        mostrar_descritiva_estatisticas_itens_pcl5()
    elif st.session_state['pagina_atual'] == 'descritiva_estatisticas_itens_ptci':
        mostrar_descritiva_estatisticas_itens_ptci()
    elif st.session_state['pagina_atual'] == 'descritiva_estatisticas_clusters_pcl5':
        mostrar_descritiva_estatisticas_clusters_pcl5()
    elif st.session_state['pagina_atual'] == 'descritiva_estatisticas_clusters_ptci':
        mostrar_descritiva_estatisticas_clusters_ptci()
