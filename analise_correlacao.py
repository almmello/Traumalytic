import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from calculations import (
    calcular_correlacao,
    criar_dataframe_para_correlacao
)

def carregar_dados():
    # Carregar dados aqui
    data = pd.read_excel('Banco LEC PCL5 PTCI.xlsx')
    return data

def mostrar_analise_correlacao():
    st.title("Análise de Correlação")

    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = carregar_dados()


    # Botão para calcular a correlação entre os escores totais da PCL-5 e PTCI
    if st.button('Correlação entre escores totais da PCL-5 e PTCI'):
        data_correlacao = criar_dataframe_para_correlacao(st.session_state['data'])

        # Calcular correlação entre escores totais
        correlacao_total = calcular_correlacao(data_correlacao['PCL5_total'], data_correlacao['PTCI_total'])
        correlacao_df = pd.DataFrame({'Correlação': [correlacao_total]}, index=['PCL-5 Total vs PTCI Total'])

        # Exibir correlação em uma tabela
        st.table(correlacao_df.round(2))

        # Criar e exibir um gráfico (mapa de calor) para a correlação
        st.subheader('Mapa de Calor da Correlação')
        matriz_correlacao = data_correlacao[['PCL5_total', 'PTCI_total']].corr().round(2)
        sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm')
        st.pyplot(plt)


    # Botão para calcular as correlações entre clusters da PCL-5 e PTCI
    if st.button('Correlações entre clusters da PCL-5 e PTCI'):
        data_correlacao = criar_dataframe_para_correlacao(st.session_state['data'])

        # Preparando a matriz de correlação para clusters
        clusters_pcl5 = ['ClusterB', 'ClusterC', 'ClusterD', 'ClusterE']
        clusters_ptci = ['ClusterA', 'ClusterB', 'ClusterC']
        matriz_correlacao_clusters = np.zeros((len(clusters_ptci), len(clusters_pcl5)))

        # Preenchendo a matriz de correlação
        for i, cluster_ptci in enumerate(clusters_ptci):
            for j, cluster_pcl5 in enumerate(clusters_pcl5):
                matriz_correlacao_clusters[i, j] = calcular_correlacao(data_correlacao[f'PTCI_{cluster_ptci}'], data_correlacao[f'PCL5_{cluster_pcl5}'])

        # Criando a tabela em forma de matriz para clusters
        df_correlacao_clusters = pd.DataFrame(matriz_correlacao_clusters, 
                                              index=[f'PTCI {c}' for c in clusters_ptci], 
                                              columns=[f'PCL-5 {c}' for c in clusters_pcl5])

        # Exibir a tabela de correlação
        st.write('Tabela de Correlações entre Clusters da PCL-5 e PTCI')
        st.dataframe(df_correlacao_clusters.round(2))

        # Criar e exibir um gráfico (mapa de calor) para as correlações entre clusters
        st.subheader('Mapa de Calor das Correlações entre Clusters')
        matriz_correlacao_clusters = data_correlacao[[f'PCL5_{c}' for c in ['ClusterB', 'ClusterC', 'ClusterD', 'ClusterE']] + [f'PTCI_{c}' for c in ['ClusterA', 'ClusterB', 'ClusterC']]].corr().round(2)
        sns.heatmap(matriz_correlacao_clusters, annot=True, cmap='coolwarm')
        st.pyplot(plt)


    # Botão para calcular as correlações entre sintomas da PCL-5 e itens do PTCI
    if st.button('Correlações entre sintomas da PCL-5 e itens do PTCI'):
        data_correlacao = criar_dataframe_para_correlacao(st.session_state['data'])

        # Preparando a matriz de correlação
        num_sintomas_pcl = 20
        num_itens_ptci = 36
        matriz_correlacao = np.zeros((num_itens_ptci, num_sintomas_pcl))

        # Preenchendo a matriz de correlação
        for i in range(num_itens_ptci):
            for j in range(num_sintomas_pcl):
                matriz_correlacao[i, j] = calcular_correlacao(data_correlacao[f'PTCI{i+1:02d}'], data_correlacao[f'PCL{j+1:02d}'])

        # Criando a tabela em forma de matriz
        df_correlacao = pd.DataFrame(matriz_correlacao, 
                                     index=[f'PTCI{i:02d}' for i in range(1, num_itens_ptci + 1)], 
                                     columns=[f'PCL{j:02d}' for j in range(1, num_sintomas_pcl + 1)])

        # Exibir a tabela de correlação
        st.write('Tabela de Correlações entre Sintomas da PCL-5 e Itens do PTCI')
        st.dataframe(df_correlacao.round(2))

        # Preparando dados para o mapa de calor
        num_sintomas_pcl = 20
        num_itens_ptci = 36
        matriz_correlacao = np.zeros((num_sintomas_pcl, num_itens_ptci))

        # Calcular correlações e preencher a matriz
        for i in range(num_sintomas_pcl):
            for j in range(num_itens_ptci):
                matriz_correlacao[i, j] = calcular_correlacao(data_correlacao[f'PCL{i+1:02d}'], data_correlacao[f'PTCI{j+1:02d}'])

        # Criar e exibir um mapa de calor para as correlações
        plt.figure(figsize=(12, 10))
        sns.heatmap(matriz_correlacao, annot=False, cmap='coolwarm', 
                    xticklabels=[f'PTCI{j+1:02d}' for j in range(num_itens_ptci)], 
                    yticklabels=[f'PCL{i+1:02d}' for i in range(num_sintomas_pcl)])
        plt.title('Mapa de Calor das Correlações entre Sintomas da PCL-5 e Itens do PTCI')
        plt.xlabel('Itens do PTCI')
        plt.ylabel('Sintomas da PCL-5')
        st.pyplot(plt)


   
# Chamada da função principal
if __name__ == "__main__":
    mostrar_analise_correlacao()
