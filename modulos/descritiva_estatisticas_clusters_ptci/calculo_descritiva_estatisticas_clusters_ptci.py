import pandas as pd

def calcular_clusters_ptci(data):
    # Fórmulas para os clusters do PTCI
    clusters_ptci = {
        'Cluster_A': ['PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI09', 'PTCI12', 'PTCI14', 'PTCI16', 'PTCI17', 
                      'PTCI20', 'PTCI21', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI33', 'PTCI35', 'PTCI36'],
        'Cluster_B': ['PTCI07', 'PTCI08', 'PTCI10', 'PTCI11', 'PTCI18', 'PTCI23', 'PTCI27'],
        'Cluster_C': ['PTCI01', 'PTCI15', 'PTCI19', 'PTCI22', 'PTCI31'],
        'PTCI_Total': ['PTCI01', 'PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI07', 'PTCI08', 'PTCI09', 'PTCI10', 'PTCI11', 'PTCI12', 'PTCI14', 'PTCI15', 'PTCI16', 'PTCI17', 'PTCI18', 'PTCI19', 'PTCI20', 'PTCI21', 'PTCI22', 'PTCI23', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI27', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI31', 'PTCI33', 'PTCI35', 'PTCI36']
    }

    # Calcula a soma e média para cada cluster
    for cluster, questions in clusters_ptci.items():
        data[cluster] = data[questions].sum(axis=1)
        data[cluster + '_media'] = data[cluster] / len(questions)
    
    return data

def calcular_estatisticas(data, coluna):
    return data[coluna].agg(['count', 'min', 'max', 'mean', 'std', 'kurtosis','skew', 'quantile'])

def calcular_descritiva_estatisticas_clusters_ptci(data):
    # Usa a função para calcular os clusters e o escore total do PTCI
    data = calcular_clusters_ptci(data)

    # Lista para armazenar as estatísticas de cada coluna
    estatisticas = []
    colunas_para_analisar = ['Cluster_A', 'Cluster_B', 'Cluster_C', 'PTCI_Total', 'Cluster_A_media', 'Cluster_B_media', 'Cluster_C_media', 'PTCI_Total_media']
    for coluna in colunas_para_analisar:
        estatistica_coluna = calcular_estatisticas(data, coluna)
        estatistica_coluna['Coluna'] = coluna
        estatisticas.append(estatistica_coluna)

    # Converte a lista de estatísticas em um DataFrame
    df_estatisticas = pd.DataFrame(estatisticas)

    return df_estatisticas.set_index('Coluna')

