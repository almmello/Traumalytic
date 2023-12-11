import streamlit as st
from .processo_analise_descritiva import (
    processar_exibir_clusters_ptci,
    processar_exibir_clusters_pcl5,
    processar_estatisticas_idade,
    processar_estatisticas_escore_total_pcl5,
    processar_estatisticas_escore_total_ptci,
    processar_estatisticas_clusters_pcl5,
    processar_estatisticas_clusters_ptci,
    processar_medidas_tendencia_central,
    processar_medidas_dispersao,
    processar_frequencia_categoricas,

)

from .conteudo_analise_descritiva import (
    explicar_clusters_ptci,
    explicar_clusters_pcl5,
    explicar_estatisticas_idade,
    explicar_estatisticas_escore_total_pcl5,
    explicar_estatisticas_escore_total_ptci,
    explicar_estatisticas_clusters_pcl5,
    explicar_estatisticas_clusters_ptci,
    explicar_medidas_tendencia_central,
    explicar_medidas_dispersao,
    explicar_frequencia_categoricas,
)

def mostrar_analise_descritiva():
    st.title("Análise Descritiva")

    explicar_clusters_ptci()
    if st.button('Calcular Clusters PTCI'):
        processar_exibir_clusters_ptci()

    explicar_clusters_pcl5()
    if st.button('Calcular Clusters PCL-5'):
        processar_exibir_clusters_pcl5()

    explicar_estatisticas_idade()
    if st.button('Calcular Estatísticas de Idade'):
        processar_estatisticas_idade()

    explicar_estatisticas_escore_total_pcl5()
    if st.button('Calcular Estatísticas do Escore Total PCL-5'):
        processar_estatisticas_escore_total_pcl5()

    explicar_estatisticas_escore_total_ptci()
    if st.button('Calcular Estatísticas do Escore Total PTCI'):
        processar_estatisticas_escore_total_ptci()

    explicar_estatisticas_clusters_pcl5()
    if st.button('Calcular Estatísticas dos Clusters PCL-5'):
        processar_estatisticas_clusters_pcl5()

    explicar_estatisticas_clusters_ptci()
    if st.button('Calcular Estatísticas dos Clusters PTCI'):
        processar_estatisticas_clusters_ptci()

    # Seção para Medidas de Tendência Central
    explicar_medidas_tendencia_central()
    if st.button('Calcular Medidas de Tendência Central'):
        processar_medidas_tendencia_central()

    # Seção para Medidas de Dispersão
    explicar_medidas_dispersao()
    if st.button('Calcular Medidas de Dispersão'):
        processar_medidas_dispersao()

    # Seção para Frequência de Variáveis Categóricas
    explicar_frequencia_categoricas()
    if st.button('Calcular Frequência de Variáveis Categóricas'):
        processar_frequencia_categoricas()
    

# Chamada da função principal
if __name__ == "__main__":
    mostrar_analise_descritiva()


