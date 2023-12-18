import pandas as pd

## Funções calcular_clusters_ptci

def mostrar_apenas_clusters_ptci(data):

    # Colunas demográficas e PCL-5
    colunas_demograficas_e_ptci = ['ID', 'SEXO', 'IDADE', 'INSTRUCAO'] + [f'PTCI{i:02d}' for i in range(1, 37)]

    # Cria um novo DataFrame para armazenar os resultados
    clusters_data = data[colunas_demograficas_e_ptci].copy()

    return clusters_data


def calcular_clusters_ptci(data):
    # Fórmulas para os clusters do PCL-5
    clusters_ptci = {
        'Cluster_A': ['PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI09', 'PTCI12', 'PTCI14', 'PTCI16', 'PTCI17', 
                      'PTCI20', 'PTCI21', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI33', 'PTCI35', 'PTCI36'],
        'Cluster_B': ['PTCI07', 'PTCI08', 'PTCI10', 'PTCI11', 'PTCI18', 'PTCI23', 'PTCI27'],
        'Cluster_C': ['PTCI01', 'PTCI15', 'PTCI19', 'PTCI22', 'PTCI31'],
        'PTCI_Total': ['PTCI01', 'PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI07', 'PTCI08', 'PTCI09', 'PTCI10', 'PTCI11', 'PTCI12', 'PTCI14', 'PTCI15', 'PTCI16', 'PTCI17', 'PTCI18', 'PTCI19', 'PTCI20', 'PTCI21', 'PTCI22', 'PTCI23', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI27', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI31', 'PTCI33', 'PTCI35', 'PTCI36']
    }

    # Colunas demográficas
    colunas_demograficas = ['ID', 'SEXO', 'IDADE', 'INSTRUCAO']

    # Cria um novo DataFrame para armazenar os resultados
    clusters_demograficas_data = data[colunas_demograficas].copy()

    # Cria outro DataFrame apenas para os cálculos dos clusters
    clusters_ptci_data = pd.DataFrame(index=data.index)

    for cluster, questions in clusters_ptci.items():
        clusters_ptci_data[cluster] = data[questions].sum(axis=1)
        clusters_ptci_data[cluster + '_media'] = clusters_ptci_data[cluster] / len(questions)
    

    # Combinando os DataFrames
    resultado_final = pd.concat([clusters_demograficas_data, clusters_ptci_data], axis=1)

    return resultado_final

