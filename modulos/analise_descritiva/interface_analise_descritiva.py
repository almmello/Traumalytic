import streamlit as st
from .processo_analise_descritiva import (      
    processar_exibir_clusters_ptci,
    processar_exibir_clusters_pcl5,
    processar_estatisticas_idade,
    processar_estatisticas_escore_total_pcl5,
    processar_estatisticas_escore_total_ptci,
    processar_estatisticas_clusters_pcl5,
    processar_estatisticas_clusters_ptci,
    processar_calculo_distribuicao_por_sexo
)

def mostrar_analise_descritiva():
    st.title("Análise Descritiva")
    
    # Botão para calcular os clusters do PTCI e exibir os resultados.
    # Este botão aciona a função processar_exibir_clusters_ptci que processa e exibe os clusters PTCI.
    if st.button('Calcular Clusters PTCI'):
        processar_exibir_clusters_ptci()

    # Botão para calcular os clusters do PCL-5 e exibir os resultados.
    # Esta função processa e exibe os clusters do PCL-5.
    if st.button('Calcular Clusters PCL-5'):
        processar_exibir_clusters_pcl5()
    
    # Botão para calcular e exibir as estatísticas descritivas da idade.
    # Esta função calcula medidas como média, mediana, desvio padrão, etc., para a idade.
    if st.button('Calcular Estatísticas de Idade'):
        processar_estatisticas_idade()

    # Botão para calcular e exibir as estatísticas descritivas do escore total do PCL-5.
    # Esta função processa os escores totais do PCL-5 e calcula suas estatísticas descritivas.
    if st.button('Calcular Estatísticas do Escore Total PCL-5'):
        processar_estatisticas_escore_total_pcl5()

    # Botão para calcular e exibir as estatísticas descritivas do escore total do PTCI.
    # Esta função processa os escores totais do PTCI e calcula suas estatísticas descritivas.
    if st.button('Calcular Estatísticas do Escore Total PTCI'):
        processar_estatisticas_escore_total_ptci()

    # Botão para calcular e exibir as estatísticas descritivas dos clusters do PCL-5.
    # Esta função processa e exibe estatísticas descritivas para cada cluster do PCL-5.
    if st.button('Calcular Estatísticas dos Clusters PCL-5'):
        processar_estatisticas_clusters_pcl5()
        
    # Botão para calcular e exibir as estatísticas descritivas dos clusters do PTCI.
    # Esta função processa e exibe estatísticas descritivas para cada cluster do PTCI.
    if st.button('Calcular Estatísticas dos Clusters PTCI'):
        processar_estatisticas_clusters_ptci()

    # Botão para calcular e exibir a distribuição dos dados por sexo.
    # Esta função analisa a distribuição dos participantes do estudo por sexo.
    if st.button('Calcular Distribuição por Sexo'):
        processar_calculo_distribuicao_por_sexo()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_analise_descritiva()
