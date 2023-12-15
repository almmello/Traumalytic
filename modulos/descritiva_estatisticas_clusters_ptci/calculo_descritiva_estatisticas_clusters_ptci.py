import pandas as pd

def calcular_clusters_ptci_e_retornar(data):
    # Define os clusters
    clusters_ptci = {
        'Cluster_A': ['PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI09', 'PTCI12', 'PTCI14', 'PTCI16', 'PTCI17', 
                      'PTCI20', 'PTCI21', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI33', 'PTCI35', 'PTCI36'],
        'Cluster_B': ['PTCI07', 'PTCI08', 'PTCI10', 'PTCI11', 'PTCI18', 'PTCI23', 'PTCI27'],
        'Cluster_C': ['PTCI01', 'PTCI15', 'PTCI19', 'PTCI22', 'PTCI31']
    }

    # Calcula as somas e médias dos clusters
    ptci_clusters = pd.DataFrame()
    for cluster, questions in clusters_ptci.items():
        ptci_clusters[f'{cluster}_Sum'] = data[questions].sum(axis=1)
        ptci_clusters[f'{cluster}_Mean'] = data[questions].mean(axis=1)

    # Calcula o escore total do PTCI
    ptci_clusters['PTCI_Total'] = ptci_clusters[['Cluster_A_Mean', 'Cluster_B_Mean', 'Cluster_C_Mean']].sum(axis=1)

    return ptci_clusters


def calcular_estatisticas(data, coluna):
    return data[coluna].agg(['mean', 'std', 'min', 'max'])


def calcular_descritiva_estatisticas_clusters_ptci(data):
    ptci_clusters = calcular_clusters_ptci_e_retornar(data)
    estatisticas = {}
    for cluster in ptci_clusters.columns:
        estatisticas[cluster] = calcular_estatisticas(ptci_clusters, cluster)
    return estatisticas
