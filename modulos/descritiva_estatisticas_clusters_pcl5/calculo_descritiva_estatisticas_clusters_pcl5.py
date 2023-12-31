import pandas as pd
from data_loader import DataLoader

def calcular_estatisticas(data, coluna):
    return data[coluna].agg(['count', 'min', 'max', 'mean', 'std', 'kurtosis','skew', 'quantile'])

def calcular_descritiva_estatisticas_clusters_pcl5(data):
    # Usa a função para calcular os clusters e o escore total do PCL5
    DataLoader.calculos_pcl5(data)

    # Lista para armazenar as estatísticas de cada coluna
    estatisticas = []
    colunas_para_analisar = ['PCL5_Cluster_B', 'PCL5_Cluster_C', 'PCL5_Cluster_D', 'PCL5_Cluster_E', 'PCL5_Total', 'PCL5_Cluster_B_media', 'PCL5_Cluster_C_media', 'PCL5_Cluster_D_media', 'PCL5_Cluster_E_media', 'PCL5_Total_media']
    
    for coluna in colunas_para_analisar:
        estatistica_coluna = calcular_estatisticas(data, coluna)
        estatistica_coluna['Coluna'] = coluna
        estatisticas.append(estatistica_coluna)

    # Converte a lista de estatísticas em um DataFrame
    df_estatisticas = pd.DataFrame(estatisticas)

    return df_estatisticas.set_index('Coluna')