import pandas as pd

def calcular_clusters_pcl5_e_retornar(data):
    clusters_pcl5 = {
        'Cluster_B': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05'],
        'Cluster_C': ['PCL06', 'PCL07'],
        'Cluster_D': ['PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14'],
        'Cluster_E': ['PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20'],
        'PCL5_total': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
    }

    pcl5_clusters = pd.DataFrame()
    for cluster, questions in clusters_pcl5.items():
        pcl5_clusters[cluster] = data[questions].sum(axis=1)
    
    return pcl5_clusters

def calcular_estatisticas(data, coluna):
    return data[coluna].agg(['mean', 'std', 'min', 'max'])

def calcular_descritiva_estatisticas_clusters_pcl5(data):
    pcl5_clusters = calcular_clusters_pcl5_e_retornar(data)
    estatisticas = {}
    for cluster in pcl5_clusters.columns:
        estatisticas[cluster] = calcular_estatisticas(pcl5_clusters, cluster)
    return estatisticas