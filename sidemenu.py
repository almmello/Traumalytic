# sidemenu.py
import streamlit as st

# Importações dos módulos das páginas
from app_interface import mostrar_conteudo as mostrar_home
from app_processos import mostrar_dados_analise as mostrar_configuracao
from modulos.visualizacao_itens_clusters_pcl5.interface_visualizacao_itens_clusters_pcl5 import mostrar_visualizacao_itens_clusters_pcl5
from modulos.visualizacao_itens_clusters_ptci.interface_visualizacao_itens_clusters_ptci import mostrar_visualizacao_itens_clusters_ptci
from modulos.estatisticas_variaveis_categoricas.interface_estatisticas_variaveis_categoricas import mostrar_estatisticas_variaveis_categoricas
from modulos.descritiva_estatisticas_itens_pcl5.interface_descritiva_estatisticas_itens_pcl5 import mostrar_descritiva_estatisticas_itens_pcl5
from modulos.descritiva_estatisticas_itens_ptci.interface_descritiva_estatisticas_itens_ptci import mostrar_descritiva_estatisticas_itens_ptci
from modulos.descritiva_estatisticas_clusters_pcl5.interface_descritiva_estatisticas_clusters_pcl5 import mostrar_descritiva_estatisticas_clusters_pcl5
from modulos.descritiva_estatisticas_clusters_ptci.interface_descritiva_estatisticas_clusters_ptci import mostrar_descritiva_estatisticas_clusters_ptci
from modulos.corte_tept_pcl5.interface_corte_tept_pcl5 import mostrar_corte_tept_pcl5
from modulos.histograma_pcl5.interface_histograma_pcl5 import mostrar_histograma_pcl5
from modulos.histograma_ptci.interface_histograma_ptci import mostrar_histograma_ptci
from modulos.caule_folhas_pcl5.interface_caule_folhas_pcl5 import mostrar_caule_folhas_pcl5
from modulos.caule_folhas_ptci.interface_caule_folhas_ptci import mostrar_caule_folhas_ptci
from modulos.boxplot_pcl5.interface_boxplot_pcl5 import mostrar_boxplot_pcl5
from modulos.boxplot_ptci.interface_boxplot_ptci import mostrar_boxplot_ptci
from modulos.teste_ks_pcl5_total.interface_teste_ks_pcl5_total import mostrar_teste_ks_pcl5_total
from modulos.teste_ks_ptci_total.interface_teste_ks_ptci_total import mostrar_teste_ks_ptci_total
from modulos.shapiro_wilk_pcl5_total.interface_shapiro_wilk_pcl5_total import mostrar_shapiro_wilk_pcl5_total
from modulos.shapiro_wilk_ptci_total.interface_shapiro_wilk_ptci_total import mostrar_shapiro_wilk_ptci_total
from modulos.probabilidade_normal_pcl5.interface_probabilidade_normal_pcl5 import mostrar_probabilidade_normal_pcl5
from modulos.probabilidade_normal_ptci.interface_probabilidade_normal_ptci import mostrar_probabilidade_normal_ptci
from modulos.detrended_qq_pcl5.interface_detrended_qq_pcl5 import mostrar_detrended_qq_pcl5
from modulos.detrended_qq_ptci.interface_detrended_qq_ptci import mostrar_detrended_qq_ptci
from modulos.corr_pearson_pcl5_total_ptci_total.interface_corr_pearson_pcl5_total_ptci_total import mostrar_corr_pearson_pcl5_total_ptci_total
from modulos.corr_pearson_pcl5_clusters_ptci_clusters.interface_corr_pearson_pcl5_clusters_ptci_clusters import mostrar_corr_pearson_pcl5_clusters_ptci_clusters
from modulos.corr_pearson_pcl5_itens_ptci_itens.interface_corr_pearson_pcl5_itens_ptci_itens import mostrar_corr_pearson_pcl5_itens_ptci_itens
from modulos.corr_spearman_pcl5_total_ptci_total.interface_corr_spearman_pcl5_total_ptci_total import mostrar_corr_spearman_pcl5_total_ptci_total
from modulos.corr_spearman_pcl5_clusters_ptci_clusters.interface_corr_spearman_pcl5_clusters_ptci_clusters import mostrar_corr_spearman_pcl5_clusters_ptci_clusters
from modulos.corr_spearman_pcl5_itens_ptci_itens.interface_corr_spearman_pcl5_itens_ptci_itens import mostrar_corr_spearman_pcl5_itens_ptci_itens
from modulos.teste_t_pcl5_total_ptci_total.interface_teste_t_pcl5_total_ptci_total import mostrar_teste_t_pcl5_total_ptci_total
from modulos.teste_t_pcl5_clusters_ptci_clusters.interface_teste_t_pcl5_clusters_ptci_clusters import mostrar_teste_t_pcl5_clusters_ptci_clusters

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
    if st.sidebar.button("Estatísticas de Variáveis Categóricas"):
        st.session_state['pagina_atual'] = 'estatisticas_variaveis_categoricas'
    if st.sidebar.button("Estatísticas dos Itens do PCL5"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_itens_pcl5'
    if st.sidebar.button("Estatísticas dos Itens do PTCI"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_itens_ptci'
    if st.sidebar.button("Estatísticas dos Clusters PCL-5"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_clusters_pcl5'
    if st.sidebar.button("Estatísticas dos Clusters PTCI"):
        st.session_state['pagina_atual'] = 'descritiva_estatisticas_clusters_ptci'
    if st.sidebar.button("Corte TEPT PCL-5"):
        st.session_state['pagina_atual'] = 'corte_tept_pcl5'
    if st.sidebar.button("Gráfico Histograma PCL-5"):
        st.session_state['pagina_atual'] = 'histograma_pcl5'
    if st.sidebar.button("Gráfico Histograma PTCI"):
        st.session_state['pagina_atual'] = 'histograma_ptci'
    if st.sidebar.button("Exibição de Caule-e-Folhas do PCL5"):
        st.session_state['pagina_atual'] = 'caule_folhas_pcl5'
    if st.sidebar.button("Exibição de Caule-e-Folhas do PTCI"):
        st.session_state['pagina_atual'] = 'caule_folhas_ptci'
    st.sidebar.markdown("## Análise de Normalidade")
    if st.sidebar.button("Gráfico Boxplot do PCL-5"):
        st.session_state['pagina_atual'] = 'boxplot_pcl5'
    if st.sidebar.button("Gráfico Boxplot do PTCI"):
        st.session_state['pagina_atual'] = 'boxplot_ptci'
    if st.sidebar.button("Teste K-S para PCL-5 Total"):
        st.session_state['pagina_atual'] = 'teste_ks_pcl5_total'
    if st.sidebar.button("Teste K-S para PTCI Total"):
        st.session_state['pagina_atual'] = 'teste_ks_ptci_total'
    if st.sidebar.button("Teste de Shapiro-Wilk para PCL-5 Total"):
        st.session_state['pagina_atual'] = 'shapiro_wilk_pcl5_total'
    if st.sidebar.button("Teste de Shapiro-Wilk para PTCI Total"):
        st.session_state['pagina_atual'] = 'shapiro_wilk_ptci_total'
    if st.sidebar.button("Gráfico de Probabilidade Normal (Q-Q) do PCL-5"):
        st.session_state['pagina_atual'] = 'probabilidade_normal_pcl5'
    if st.sidebar.button("Gráfico de Probabilidade Normal (Q-Q) do PTCI"):
        st.session_state['pagina_atual'] = 'probabilidade_normal_ptci'
    if st.sidebar.button("Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PCL-5"):
        st.session_state['pagina_atual'] = 'detrended_qq_pcl5'
    if st.sidebar.button("Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PTCI"):
        st.session_state['pagina_atual'] = 'detrended_qq_ptci'
    st.sidebar.markdown("## Análise de Correlação")
    if st.sidebar.button("Correlação Pearson entre PCL5 Total e PTCI Total"):
        st.session_state['pagina_atual'] = 'corr_pearson_pcl5_total_ptci_total'
    if st.sidebar.button("Correlação Pearson entre os Clusters do PCL5 e PTCI"):
        st.session_state['pagina_atual'] = 'corr_pearson_pcl5_clusters_ptci_clusters'
    if st.sidebar.button("Correlação Pearson entre os Itens do PCL5 e PTCI"):
        st.session_state['pagina_atual'] = 'corr_pearson_pcl5_itens_ptci_itens'
    if st.sidebar.button("Correlação Spearman entre PCL5 Total e PTCI Total"):
        st.session_state['pagina_atual'] = 'corr_spearman_pcl5_total_ptci_total'
    if st.sidebar.button("Correlação Spearman entre os Clusters do PCL5 e PTCI"):
        st.session_state['pagina_atual'] = 'corr_spearman_pcl5_clusters_ptci_clusters'
    if st.sidebar.button("Correlação Spearman entre os Itens do PCL5 e PTCI"):
        st.session_state['pagina_atual'] = 'corr_spearman_pcl5_itens_ptci_itens'
    if st.sidebar.button("Teste T Student entre PCL5 Total e PTCI Total"):
        st.session_state['pagina_atual'] = 'teste_t_pcl5_total_ptci_total'
    if st.sidebar.button("Teste T Student entre os Clusters do PCL5 e PTCI"):
        st.session_state['pagina_atual'] = 'teste_t_pcl5_clusters_ptci_clusters'


    # Exibição de Conteúdo Baseado na Página Atual
    if st.session_state['pagina_atual'] == 'home':
        mostrar_home()
    elif st.session_state['pagina_atual'] == 'configuracoes':
        mostrar_configuracao()
    elif st.session_state['pagina_atual'] == 'visualizacao_itens_clusters_pcl5':
        mostrar_visualizacao_itens_clusters_pcl5()
    elif st.session_state['pagina_atual'] == 'visualizacao_itens_clusters_ptci':
        mostrar_visualizacao_itens_clusters_ptci()
    elif st.session_state['pagina_atual'] == 'estatisticas_variaveis_categoricas':
        mostrar_estatisticas_variaveis_categoricas()
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
    elif st.session_state['pagina_atual'] == 'teste_ks_pcl5_total':
        mostrar_teste_ks_pcl5_total()
    elif st.session_state['pagina_atual'] == 'teste_ks_ptci_total':
        mostrar_teste_ks_ptci_total()
    elif st.session_state['pagina_atual'] == 'shapiro_wilk_pcl5_total':
        mostrar_shapiro_wilk_pcl5_total()
    elif st.session_state['pagina_atual'] == 'shapiro_wilk_ptci_total':
        mostrar_shapiro_wilk_ptci_total()
    elif st.session_state['pagina_atual'] == 'probabilidade_normal_pcl5':
        mostrar_probabilidade_normal_pcl5()
    elif st.session_state['pagina_atual'] == 'probabilidade_normal_ptci':
        mostrar_probabilidade_normal_ptci()
    elif st.session_state['pagina_atual'] == 'detrended_qq_pcl5':
        mostrar_detrended_qq_pcl5()
    elif st.session_state['pagina_atual'] == 'detrended_qq_ptci':
        mostrar_detrended_qq_ptci()
    elif st.session_state['pagina_atual'] == 'corr_pearson_pcl5_total_ptci_total':
        mostrar_corr_pearson_pcl5_total_ptci_total()
    elif st.session_state['pagina_atual'] == 'corr_pearson_pcl5_clusters_ptci_clusters':
        mostrar_corr_pearson_pcl5_clusters_ptci_clusters()
    elif st.session_state['pagina_atual'] == 'corr_pearson_pcl5_itens_ptci_itens':
        mostrar_corr_pearson_pcl5_itens_ptci_itens()
    elif st.session_state['pagina_atual'] == 'corr_spearman_pcl5_total_ptci_total':
        mostrar_corr_spearman_pcl5_total_ptci_total()
    elif st.session_state['pagina_atual'] == 'corr_spearman_pcl5_clusters_ptci_clusters':
        mostrar_corr_spearman_pcl5_clusters_ptci_clusters()
    elif st.session_state['pagina_atual'] == 'corr_spearman_pcl5_itens_ptci_itens':
        mostrar_corr_spearman_pcl5_itens_ptci_itens()
    elif st.session_state['pagina_atual'] == 'teste_t_pcl5_total_ptci_total':
        mostrar_teste_t_pcl5_total_ptci_total()
    elif st.session_state['pagina_atual'] == 'teste_t_pcl5_clusters_ptci_clusters':
        mostrar_teste_t_pcl5_clusters_ptci_clusters()
