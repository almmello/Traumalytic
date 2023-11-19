import pandas as pd
from scipy import stats
from scipy.stats import shapiro
import matplotlib.pyplot as plt
from scipy.stats import probplot
import numpy as np


# Funções Auxiliares
def calcular_clusters_ptci_e_retornar(data):
    clusters_ptci = {
        'Cluster_A': ['PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI09', 'PTCI12', 'PTCI14', 'PTCI16', 'PTCI17', 
                      'PTCI20', 'PTCI21', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI33', 'PTCI35', 'PTCI36'],
        'Cluster_B': ['PTCI07', 'PTCI08', 'PTCI10', 'PTCI11', 'PTCI18', 'PTCI23', 'PTCI27'],
        'Cluster_C': ['PTCI01', 'PTCI15', 'PTCI19', 'PTCI22', 'PTCI31']
    }

    ptci_clusters = pd.DataFrame()
    for cluster, questions in clusters_ptci.items():
        ptci_clusters[cluster] = data[questions].sum(axis=1)
    
    return ptci_clusters

def calcular_clusters_pcl5_e_retornar(data):
    clusters_pcl5 = {
        'Cluster_B': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05'],
        'Cluster_C': ['PCL06', 'PCL07'],
        'Cluster_D': ['PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14'],
        'Cluster_E': ['PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
    }

    pcl5_clusters = pd.DataFrame()
    for cluster, questions in clusters_pcl5.items():
        pcl5_clusters[cluster] = data[questions].sum(axis=1)
    
    return pcl5_clusters


# Funções Principais

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

def calcular_estatisticas(data, coluna):
    return data[coluna].agg(['mean', 'std', 'min', 'max'])

def calcular_escores_pcl5(data):
    # Calcula o escore total do PCL-5
    pcl5_columns = [col for col in data.columns if col.startswith('PCL')]
    data['PCL5_total'] = data[pcl5_columns].sum(axis=1)
    return calcular_estatisticas(data, 'PCL5_total')

def calcular_escores_ptci(data):
    # Calcula o escore total do PTCI
    ptci_columns = [col for col in data.columns if col.startswith('PTCI')]
    data['PTCI_total'] = data[ptci_columns].sum(axis=1)
    return calcular_estatisticas(data, 'PTCI_total')



def calcular_estatisticas_clusters_pcl5(data):
    pcl5_clusters = calcular_clusters_pcl5_e_retornar(data)
    estatisticas = {}
    for cluster in pcl5_clusters.columns:
        estatisticas[cluster] = calcular_estatisticas(pcl5_clusters, cluster)
    return estatisticas

def calcular_estatisticas_clusters_ptci(data):
    ptci_clusters = calcular_clusters_ptci_e_retornar(data)
    estatisticas = {}
    for cluster in ptci_clusters.columns:
        estatisticas[cluster] = calcular_estatisticas(ptci_clusters, cluster)
    return estatisticas


def calcular_medidas_tendencia_central(data, coluna):
    """
    Calcula as medidas de tendência central para uma coluna específica.
    """
    media = data[coluna].mean()
    mediana = data[coluna].median()
    moda = data[coluna].mode()[0]
    return {'Média': media, 'Mediana': mediana, 'Moda': moda}

def calcular_medidas_dispersao(data, coluna):
    """
    Calcula as medidas de dispersão para uma coluna específica.
    """
    desvio_padrao = data[coluna].std()
    variancia = data[coluna].var()
    amplitude = data[coluna].max() - data[coluna].min()
    return {'Desvio Padrão': desvio_padrao, 'Variância': variancia, 'Amplitude': amplitude}

def examinar_distribuicao(data, coluna):
    """
    Realiza o teste de Shapiro-Wilk para normalidade e cria um gráfico de probabilidade.
    """
    shapiro_test = shapiro(data[coluna])
    plt.figure()
    probplot(data[coluna], dist="norm", plot=plt)
    plt.title(f'Gráfico de Probabilidade para {coluna}')
    plt.show()
    return {'Shapiro-Wilk Test': shapiro_test}

# Função para calcular a frequência de variáveis categóricas
def calcular_frequencia_categoricas(data, coluna):
    """
    Calcula a frequência de valores em uma coluna categórica.
    """
    frequencia = data[coluna].value_counts(normalize=True) * 100
    return frequencia
