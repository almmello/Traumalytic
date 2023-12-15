# sidemenu.py
import streamlit as st

# Importações dos módulos das páginas
from app_interface import mostrar_conteudo as mostrar_home
from app_processos import mostrar_dados_analise as mostrar_configuracao
from modulos.descritiva_clusters_ptci_pcl5.interface_descritiva_clusters_ptci_pcl5 import mostrar_clusters
from modulos.descritiva_estatisticas_idade.interface_descritiva_estatisticas_idade import mostrar_estatisticas_idade
from modulos.descritiva_estatisticas_escore_pcl5.interface_descritiva_estatisticas_escore_pcl5 import mostrar_descritiva_estatisticas_escore_pcl5
from modulos.descritiva_estatisticas_escore_ptci.interface_descritiva_estatisticas_escore_ptci import mostrar_descritiva_estatisticas_escore_ptci
from modulos.descritiva_estatisticas_clusters_pcl5.interface_descritiva_estatisticas_clusters_pcl5 import mostrar_descritiva_estatisticas_clusters_pcl5
from modulos.descritiva_estatisticas_clusters_ptci.interface_descritiva_estatisticas_clusters_ptci import mostrar_descritiva_estatisticas_clusters_ptci
from modulos.descritiva_medidas_tendencia.interface_descritiva_medidas_tendencia import mostrar_descritiva_medidas_tendencia
from modulos.descritiva_medidas_dispersao.interface_descritiva_medidas_dispersao import mostrar_descritiva_medidas_dispersao
from modulos.descritiva_frequencia_variaveis.interface_descritiva_frequencia_variaveis import mostrar_descritiva_frequencia_variaveis
from modulos.normalidade_escore_total_pcl5.interface_normalidade_escore_total_pcl5 import mostrar_normalidade_escore_total_pcl5

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
    if st.sidebar.button("Análise Estatísticas do Escore Total PTCI"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_escore_ptci'
    if st.sidebar.button("Análise Estatísticas dos Clusters PCL-5"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_clusters_pcl5'
    if st.sidebar.button("Análise Estatísticas dos Clusters PTCI"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_clusters_ptci'
    if st.sidebar.button("Análise Medidas de Tendência Central"):
        st.session_state['pagina_atual'] = 'descritiva_medidas_tendencia'
    if st.sidebar.button("Análise Medidas de Dispersão"):
        st.session_state['pagina_atual'] = 'descritiva_medidas_dispersao'
    if st.sidebar.button("Análise Frequência de Variáveis Categóricas"):
        st.session_state['pagina_atual'] = 'descritiva_frequencia_variaveis'
    if st.sidebar.button("Análise Normalidade do escore total do PCL-5"):
        st.session_state['pagina_atual'] = 'normalidade_escore_total_pcl5'


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
    elif st.session_state['pagina_atual'] == 'descritiva_estatisticas_escore_ptci':
        mostrar_descritiva_estatisticas_escore_ptci()
    elif st.session_state['pagina_atual'] == 'descritiva_estatisticas_clusters_pcl5':
        mostrar_descritiva_estatisticas_clusters_pcl5()
    elif st.session_state['pagina_atual'] == 'descritiva_estatisticas_clusters_ptci':
        mostrar_descritiva_estatisticas_clusters_ptci()
    elif st.session_state['pagina_atual'] == 'descritiva_medidas_tendencia':
        mostrar_descritiva_medidas_tendencia()
    elif st.session_state['pagina_atual'] == 'descritiva_medidas_dispersao':
        mostrar_descritiva_medidas_dispersao()
    elif st.session_state['pagina_atual'] == 'descritiva_frequencia_variaveis':
        mostrar_descritiva_frequencia_variaveis()
    elif st.session_state['pagina_atual'] == 'normalidade_escore_total_pcl5':
        mostrar_normalidade_escore_total_pcl5()
