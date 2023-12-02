import pandas as pd
from scipy.stats import shapiro
import matplotlib.pyplot as plt
from scipy.stats import probplot
import numpy as np


## Funções calcular_clusters_ptci e calcular_clusters_pcl5 aqui (definidas anteriormente)
def calcular_clusters_ptci(data):
    # Fórmulas para os clusters do PTCI
    clusters_ptci = {
        'Cluster_A': ['PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI09', 'PTCI12', 'PTCI14', 'PTCI16', 'PTCI17', 
                      'PTCI20', 'PTCI21', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI33', 'PTCI35', 'PTCI36'],
        'Cluster_B': ['PTCI07', 'PTCI08', 'PTCI10', 'PTCI11', 'PTCI18', 'PTCI23', 'PTCI27'],
        'Cluster_C': ['PTCI01', 'PTCI15', 'PTCI19', 'PTCI22', 'PTCI31']
    }
    
    for cluster, questions in clusters_ptci.items():
        data[cluster] = data[questions].sum(axis=1)
        data[cluster + '_media'] = data[cluster] / len(questions)

    return data


def calcular_clusters_pcl5(data):
    # Fórmulas para os clusters do PCL-5
    clusters_pcl5 = {
        'Cluster_B': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05'],
        'Cluster_C': ['PCL06', 'PCL07'],
        'Cluster_D': ['PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14'],
        'Cluster_E': ['PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
    }

    for cluster, questions in clusters_pcl5.items():
        data[cluster] = data[questions].sum(axis=1)
        data[cluster + '_media'] = data[cluster] / len(questions)

    return data

