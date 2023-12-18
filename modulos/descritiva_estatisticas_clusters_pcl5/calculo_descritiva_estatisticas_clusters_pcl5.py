import pandas as pd

def calcular_clusters_pcl5(data):
    # Fórmulas para os clusters do PCL-5
    clusters_pcl5 = {
        'Cluster_B': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05'],
        'Cluster_C': ['PCL06', 'PCL07'],
        'Cluster_D': ['PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14'],
        'Cluster_E': ['PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20'],
        'PCL5_Total': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
    }

    for cluster, questions in clusters_pcl5.items():
        data[cluster] = data[questions].sum(axis=1)
        data[cluster + '_media'] = data[cluster] / len(questions)

    return data

def calcular_estatisticas(data, coluna):
    return data[coluna].agg(['min', 'max', 'mean', 'std', 'count', 'kurtosis','skew', 'quantile'])

def calcular_descritiva_estatisticas_clusters_pcl5(data):
    # Usa a função para calcular os clusters e o escore total do PCL5
    data = calcular_clusters_pcl5(data)

    # Lista para armazenar as estatísticas de cada coluna
    estatisticas = []
    colunas_para_analisar = ['Cluster_B', 'Cluster_C', 'Cluster_D', 'Cluster_E', 'PCL5_Total', 'Cluster_B_media', 'Cluster_C_media', 'Cluster_D_media', 'Cluster_E_media', 'PCL5_Total_media']
    
    for coluna in colunas_para_analisar:
        estatistica_coluna = calcular_estatisticas(data, coluna)
        estatistica_coluna['Coluna'] = coluna
        estatisticas.append(estatistica_coluna)

    # Converte a lista de estatísticas em um DataFrame
    df_estatisticas = pd.DataFrame(estatisticas)

    return df_estatisticas.set_index('Coluna')