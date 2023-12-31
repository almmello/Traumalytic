import pandas as pd
from data_loader import DataLoader

## Funções calcular_clusters_ptci e calcular_clusters_pcl5

def mostrar_apenas_clusters_pcl5(data):

    # Colunas demográficas e PCL-5
    colunas_demograficas_e_pcl5 = ['ID', 'SEXO', 'IDADE', 'INSTRUCAO'] + [f'PCL{i:02d}' for i in range(1, 21)]

    # Cria um novo DataFrame para armazenar os resultados
    clusters_data = data[colunas_demograficas_e_pcl5].copy()

    return clusters_data


def calcular_clusters_pcl5(data):
    # Fórmulas para os clusters do PCL-5
    clusters_pcl5 = {
        'PCL5_Cluster_B': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05'],
        'PCL5_Cluster_C': ['PCL06', 'PCL07'],
        'PCL5_Cluster_D': ['PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14'],
        'PCL5_Cluster_E': ['PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20'],
        'PCL5_total': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
    }

    # Colunas demográficas
    colunas_demograficas = ['ID', 'SEXO', 'IDADE', 'INSTRUCAO']

    # Cria um novo DataFrame para armazenar os resultados
    clusters_demograficas_data = data[colunas_demograficas].copy()

    # Cria outro DataFrame apenas para os cálculos dos clusters
    clusters_pcl5_data = pd.DataFrame(index=data.index)

    for cluster, questions in clusters_pcl5.items():
        clusters_pcl5_data[cluster] = data[questions].sum(axis=1)
        clusters_pcl5_data[cluster + '_media'] = clusters_pcl5_data[cluster] / len(questions)

    # Combinando os DataFrames
    resultado_final = pd.concat([clusters_demograficas_data, clusters_pcl5_data], axis=1)

    return resultado_final

