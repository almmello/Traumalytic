# sidemenu.py
import streamlit as st

# Importações dos módulos das páginas
from app_interface import mostrar_conteudo as mostrar_home
from app_processos import mostrar_dados_analise as mostrar_configuracao
from modulos.descritiva_clusters_ptci_pcl5.interface_descritiva_clusters_ptci_pcl5 import mostrar_clusters
from modulos.descritiva_estatisticas_idade.interface_descritiva_estatisticas_idade import mostrar_estatisticas_idade
from modulos.descritiva_estatisticas_escore_pcl5.interface_descritiva_estatisticas_escore_pcl5 import mostrar_descritiva_estatisticas_escore_pcl5

def create_sidebar():
    st.sidebar.title("Traumalytics")
    if st.sidebar.button("Home"):
        st.session_state['pagina_atual'] = 'home'
    if st.sidebar.button("Configurações"):
        st.session_state['pagina_atual'] = 'configuracoes'

    st.sidebar.markdown("## Análise Descritiva")
    if st.sidebar.button("Clusters PTCi e PCL-5"):
        st.session_state['pagina_atual'] = 'clusters_pcti_pcl5'
    if st.sidebar.button("Análises Estatísticas de Idade"):
        st.session_state['pagina_atual'] = 'analise_estatisticas_idade'
    if st.sidebar.button("Análise Estatísticas do Escore Total PCL-5"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_escore_pcl5'

    # Exibição de Conteúdo Baseado na Página Atual
    if st.session_state['pagina_atual'] == 'home':
        mostrar_home()
    elif st.session_state['pagina_atual'] == 'configuracoes':
        mostrar_configuracao()
    elif st.session_state['pagina_atual'] == 'clusters_pcti_pcl5':
        mostrar_clusters()
    elif st.session_state['pagina_atual'] == 'analise_estatisticas_idade':
        mostrar_estatisticas_idade()
    elif st.session_state['pagina_atual'] == 'descritiva_estatisticas_escore_pcl5':
        mostrar_descritiva_estatisticas_escore_pcl5()
