import pandas as pd
from data_loader import DataLoader

def calcular_estatisticas(data, coluna):
    return data[coluna].agg(['count', 'min', 'max', 'mean', 'std', 'kurtosis','skew', 'quantile'])

def calcular_descritiva_estatisticas_clusters_ptci(data):
    # Usa a função para calcular os clusters e o escore total do PTCI
    DataLoader.calculos_ptci(data)

    # Lista para armazenar as estatísticas de cada coluna
    estatisticas = []
    colunas_para_analisar = ['PTCI_Cluster_A', 'PTCI_Cluster_B', 'PTCI_Cluster_C', 'PTCI_Total', 'PTCI_Cluster_A_media', 'PTCI_Cluster_B_media', 'PTCI_Cluster_C_media', 'PTCI_Total_media']
    for coluna in colunas_para_analisar:
        estatistica_coluna = calcular_estatisticas(data, coluna)
        estatistica_coluna['Coluna'] = coluna
        estatisticas.append(estatistica_coluna)

    # Converte a lista de estatísticas em um DataFrame
    df_estatisticas = pd.DataFrame(estatisticas)

    return df_estatisticas.set_index('Coluna')

