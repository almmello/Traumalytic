import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
from data_loader import DataLoader

def criar_teste_t_pcl5_clusters_ptci_clusters(data):
    DataLoader.calculos_pcl5(data)  # Preparação dos dados para PCL-5
    DataLoader.calculos_ptci(data)  # Preparação dos dados para PTCI

    clusters = ['PCL5_Total', 'PCL5_Cluster_B', 'PCL5_Cluster_C', 'PCL5_Cluster_D', 'PCL5_Cluster_E', 'PTCI_Total', 'PTCI_Cluster_A', 'PTCI_Cluster_B', 'PTCI_Cluster_C']

    # Preparar dados para o gráfico e resultados
    medias_pcl5 = []
    medias_ptci = []
    desvios_pcl5 = []
    desvios_ptci = []
    t_statistics = []
    p_values = []
    ns = []

    for cluster in clusters:
        # Realizando o teste T de Student para cada cluster
        t_statistic, p_value = stats.ttest_ind(data[cluster], data[cluster], equal_var=False)
        
        medias_pcl5.append(data[cluster].mean())
        medias_ptci.append(data[cluster].mean())
        desvios_pcl5.append(data[cluster].std())
        desvios_ptci.append(data[cluster].std())
        t_statistics.append(t_statistic)
        p_values.append(p_value)
        ns.append(len(data[cluster]))

    # Criando DataFrame com os resultados
    resultados_df = pd.DataFrame({
        'Cluster': clusters,
        'Média PCL5': medias_pcl5,
        'Desvio Padrão PCL5': desvios_pcl5,
        'Média PTCI': medias_ptci,
        'Desvio Padrão PTCI': desvios_ptci,
        'T-Statistic': t_statistics,
        'P-Value': p_values,
        'N': ns
    })

    # Criando o gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    x = range(len(clusters))
    ax.bar(x, medias_pcl5, yerr=desvios_pcl5, capsize=5, label='PCL5', alpha=0.5)
    ax.bar(x, medias_ptci, yerr=desvios_ptci, capsize=5, label='PTCI', alpha=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(clusters, rotation=45)
    ax.set_ylabel('Médias dos Escores')
    ax.set_title('Teste T entre Clusters do PCL5 e PTCI')
    ax.legend()

    return fig, resultados_df
