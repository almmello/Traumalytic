import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as stats
import numpy as np

from data_loader import DataLoader

def criar_corr_spearman_pcl5_clusters_ptci_clusters(data):
    # Utilize as funções de cálculo de clusters para adicionar os clusters ao dataframe
    DataLoader.calculos_pcl5(data)  # Preparação dos dados
    DataLoader.calculos_ptci(data)  # Preparação dos dados
   
    # Defina os clusters de PCL-5 e PTCI
    vertical_axe = ['PCL5_Total', 'PCL5_Cluster_B', 'PCL5_Cluster_C', 'PCL5_Cluster_D', 'PCL5_Cluster_E', 'PTCI_Total', 'PTCI_Cluster_A', 'PTCI_Cluster_B', 'PTCI_Cluster_C']
    horizontal_axe = ['PCL5_Total', 'PCL5_Cluster_B', 'PCL5_Cluster_C', 'PCL5_Cluster_D', 'PCL5_Cluster_E', 'PTCI_Total', 'PTCI_Cluster_A', 'PTCI_Cluster_B', 'PTCI_Cluster_C']
    
    # Preparar o DataFrame para o mapa de calor
    heatmap_data = pd.DataFrame(index=vertical_axe, columns=horizontal_axe)
    p_values_data = pd.DataFrame(index=vertical_axe, columns=horizontal_axe)
    
    # Calcular a correlação entre os clusters de PCL-5 e PTCI usando Spearman
    for v_column in vertical_axe:
        for h_column in horizontal_axe:
            correlacao, p_value = stats.spearmanr(data[v_column], data[h_column])
            heatmap_data.loc[v_column, h_column] = correlacao
            p_values_data.loc[v_column, h_column] = p_value
    
    # Criar o mapa de calor
    fig, ax = plt.subplots(figsize=(12, 10))  # Ajuste o tamanho da figura conforme necessário
    
    # Anotações com correlação, p-value e N
    n = len(data)
    annotations = heatmap_data.map(lambda x: f"{x:.3f}") + "\n" + \
                  p_values_data.map(lambda x: f"Sig: {x:.3f}") + "\n" + \
                  np.vectorize(lambda x: f"N: {n}")(heatmap_data)
    
    sns.heatmap(heatmap_data.astype(float), annot=annotations.values, fmt="", cmap='coolwarm', cbar=True, ax=ax, linewidths=0.5)  # Ajuste linewidths conforme necessário
    ax.set_title('Mapa de Calor de Correlação Spearman entre Clusters de PCL-5 e PTCI')
    plt.yticks(rotation=0)
    
    return fig
