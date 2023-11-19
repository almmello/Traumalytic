import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data_loader import DataLoader

from .calculo_analise_correlacao import calcular_correlacao, criar_dataframe_para_correlacao


# Correlações entre Escores Totais da PCL-5 e PTCI
def correlacao_escores_totais():
    st.subheader('Correlação entre Escores Totais da PCL-5 e PTCI')

    # Inicializar o DataLoader e carregar os dados
    data_loader = DataLoader()
    
    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = data_loader.carregar_dados()

    # Preparar DataFrame para correlação
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

# Correlações entre clusters da PCL-5 e PTCI
def correlacao_clusters():
    st.subheader('Correlação entre Escores Totais da PCL-5 e PTCI')

    # Inicializar o DataLoader e carregar os dados
    data_loader = DataLoader()
    
    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = data_loader.carregar_dados()

    # Preparar DataFrame para correlação
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
    matriz_correlacao_clusters = data_correlacao[[f'PCL5_{c}' for c in clusters_pcl5] + [f'PTCI_{c}' for c in clusters_ptci]].corr().round(2)
    sns.heatmap(matriz_correlacao_clusters, annot=True, cmap='coolwarm')
    st.pyplot(plt)

# Correlações entre Sintomas da PCL-5 e Itens do PTCI
def correlacao_sintomas_itens():
    st.subheader('Correlações entre Sintomas da PCL-5 e Itens do PTCI')

    # Inicializar o DataLoader e carregar os dados
    data_loader = DataLoader()

    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = data_loader.carregar_dados()

    # Preparar DataFrame para correlação
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

   
    # Ajuste os rótulos dos eixos para corresponder aos dados da matriz de correlação
    xticklabels = [f'PCL{j+1:02d}' for j in range(num_sintomas_pcl)]
    yticklabels = [f'PTCI{i+1:02d}' for i in range(num_itens_ptci)]

    # Crie o mapa de calor com os rótulos corretos
    plt.figure(figsize=(10, 12))  # Ajuste o tamanho conforme necessário
    sns.heatmap(matriz_correlacao, annot=False, cmap='coolwarm', xticklabels=xticklabels, yticklabels=yticklabels)
    plt.title('Mapa de Calor das Correlações entre Sintomas da PCL-5 e Itens do PTCI')
    plt.xlabel('Itens do PTCI')
    plt.ylabel('Sintomas da PCL-5')
    plt.tight_layout()  # Isso pode ajudar se partes do gráfico estiverem sendo cortadas
    st.pyplot(plt)