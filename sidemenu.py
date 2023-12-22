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
from modulos.corte_tept_pcl5.interface_corte_tept_pcl5 import mostrar_corte_tept_pcl5
from modulos.sumario_estatistico_pcl5.interface_sumario_estatistico_pcl5 import mostrar_sumario_estatistico_pcl5
from modulos.sumario_estatistico_ptci.interface_sumario_estatistico_ptci import mostrar_sumario_estatistico_ptci
from modulos.histograma_pcl5.interface_histograma_pcl5 import mostrar_histograma_pcl5
from modulos.histograma_ptci.interface_histograma_ptci import mostrar_histograma_ptci
from modulos.caule_folhas_pcl5.interface_caule_folhas_pcl5 import mostrar_caule_folhas_pcl5
from modulos.caule_folhas_ptci.interface_caule_folhas_ptci import mostrar_caule_folhas_ptci
from modulos.boxplot_pcl5.interface_boxplot_pcl5 import mostrar_boxplot_pcl5
from modulos.boxplot_ptci.interface_boxplot_ptci import mostrar_boxplot_ptci

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
    if st.sidebar.button("Estatísticas de Idade"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_idade'
    if st.sidebar.button("Estatísticas dos Itens do PCL5"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_itens_pcl5'
    if st.sidebar.button("Estatísticas dos Itens do PTCI"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_itens_ptci'
    if st.sidebar.button("Estatísticas dos Clusters PCL-5"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_clusters_pcl5'
    if st.sidebar.button("Estatísticas dos Clusters PTCI"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_clusters_ptci'
    if st.sidebar.button("Análise de Corte TEPT PCL-5"):
        st.session_state['pagina_atual'] = 'corte_tept_pcl5'
    if st.sidebar.button("Sumário Estatístico do PCL-5"):
        st.session_state['pagina_atual'] = 'sumario_estatistico_pcl5'
    if st.sidebar.button("Sumário Estatístico do PTCI"):
        st.session_state['pagina_atual'] = 'sumario_estatistico_ptci'
    if st.sidebar.button("Gráfico Histograma PCL-5"):
        st.session_state['pagina_atual'] = 'histograma_pcl5'
    if st.sidebar.button("Gráfico Histograma PTCI"):
        st.session_state['pagina_atual'] = 'histograma_ptci'
    if st.sidebar.button("Exibição de Caule-e-Folhas do PCL5"):
        st.session_state['pagina_atual'] = 'caule_folhas_pcl5'
    if st.sidebar.button("Exibição de Caule-e-Folhas do PTCI"):
        st.session_state['pagina_atual'] = 'caule_folhas_ptci'
    if st.sidebar.button("Gráfico Boxplot do PCL-5"):
        st.session_state['pagina_atual'] = 'boxplot_pcl5'
    if st.sidebar.button("Gráfico Boxplot do PTCI"):
        st.session_state['pagina_atual'] = 'boxplot_ptci'


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
    elif st.session_state['pagina_atual'] == 'corte_tept_pcl5':
        mostrar_corte_tept_pcl5()
    elif st.session_state['pagina_atual'] == 'sumario_estatistico_pcl5':
        mostrar_sumario_estatistico_pcl5()
    elif st.session_state['pagina_atual'] == 'sumario_estatistico_ptci':
        mostrar_sumario_estatistico_ptci()
    elif st.session_state['pagina_atual'] == 'histograma_pcl5':
        mostrar_histograma_pcl5()
    elif st.session_state['pagina_atual'] == 'histograma_ptci':
        mostrar_histograma_ptci()
    elif st.session_state['pagina_atual'] == 'caule_folhas_pcl5':
        mostrar_caule_folhas_pcl5()
    elif st.session_state['pagina_atual'] == 'caule_folhas_ptci':
        mostrar_caule_folhas_ptci()
    elif st.session_state['pagina_atual'] == 'boxplot_pcl5':
        mostrar_boxplot_pcl5()
    elif st.session_state['pagina_atual'] == 'boxplot_ptci':
        mostrar_boxplot_ptci()
