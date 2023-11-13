import pandas as pd
from scipy import stats
from scipy.stats import shapiro
import matplotlib.pyplot as plt
from scipy.stats import probplot
import numpy as np

# Gera uma amostra de dados seguindo uma distribuição normal.
def gerar_dados_normal(n=100, media=0, desvio_padrao=1):
    dados_normal = np.random.normal(loc=media, scale=desvio_padrao, size=n)
    return dados_normal

def calcular_estatisticas(data, coluna):
    return data[coluna].agg(['mean', 'std', 'min', 'max'])

# Funções calcular_clusters_ptci e calcular_clusters_pcl5 aqui (definidas anteriormente)
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


def calcular_distribuicao_por_sexo(data):
    distribuicao = data['SEXO'].value_counts(normalize=True) * 100
    return distribuicao


"""
    Calcula os escores totais e de clusters da PCL-5 e PTCI, e realiza o teste de Shapiro-Wilk.
    Retorna um dicionário com os p-valores para cada variável.
"""

def testar_normalidade(data):
    """
    Calcula os escores totais e de clusters da PCL-5 e PTCI, realiza o teste de Shapiro-Wilk e retorna um DataFrame com os escores.
    """
    # Calcular os escores dos clusters e totais para PCL-5 e PTCI
    pcl5_clusters = calcular_clusters_pcl5_e_retornar(data)
    ptci_clusters = calcular_clusters_ptci_e_retornar(data)

    data_escores = pd.DataFrame()
    data_escores['PCL5_total'] = pcl5_clusters.sum(axis=1)
    data_escores['PTCI_total'] = ptci_clusters.sum(axis=1)

    for cluster in pcl5_clusters.columns:
        data_escores[cluster] = pcl5_clusters[cluster]

    for cluster in ptci_clusters.columns:
        data_escores[cluster] = ptci_clusters[cluster]

    # Executar o teste de Shapiro-Wilk
    resultados = {}
    for var in data_escores.columns:
        valid_data = data_escores[var].dropna()
        if len(valid_data) > 3:  # Shapiro-Wilk requer pelo menos 3 valores não-nulos
            stat, p = shapiro(valid_data)
            resultados[var] = p
        else:
            resultados[var] = 'Dados insuficientes para teste'

    return resultados, data_escores


def criar_histograma(data, coluna, descricao_x='Valores', descricao_y='Frequência'):
    plt.figure()
    plt.hist(data[coluna].dropna(), bins=30, edgecolor='black')
    plt.title(f'Histograma de {coluna}')
    plt.xlabel(descricao_x)
    plt.ylabel(descricao_y)
    plt.grid(True)
    return plt.gcf()

def criar_grafico_qq(data, coluna, descricao_x='Quantis Teóricos', descricao_y='Quantis Reais'):
    plt.figure()
    probplot(data[coluna].dropna(), dist="norm", plot=plt)
    plt.title(f'Gráfico Q-Q para {coluna}')
    plt.xlabel(descricao_x)
    plt.ylabel(descricao_y)
    return plt.gcf()

# Calcula o p-valor para uma amostra de dados, assumindo uma distribuição normal.
def calcular_p_valor_normal(dados):
    
    stat, p = shapiro(dados)
    return p

# Calcula o coeficiente de correlação de Pearson entre duas séries.
def calcular_correlacao(serie1, serie2):
    correlacao = serie1.corr(serie2, method='pearson')
    return correlacao


def criar_dataframe_para_correlacao(data_original):
    data_correlacao = pd.DataFrame()

    # Adicionando colunas de PCL-5 e PTCI
    for i in range(1, 21):
        data_correlacao[f'PCL{i:02d}'] = data_original[f'PCL{i:02d}']
    for i in range(1, 37):
        data_correlacao[f'PTCI{i:02d}'] = data_original[f'PTCI{i:02d}']

    # Cálculos conforme as fórmulas fornecidas
    # PCL-5
    data_correlacao['PCL5_total'] = data_correlacao[[f'PCL{i:02d}' for i in range(1, 21)]].sum(axis=1)
    data_correlacao['PCL5_ClusterB'] = data_correlacao[[f'PCL{i:02d}' for i in [1, 2, 3, 4, 5]]].sum(axis=1)
    data_correlacao['PCL5_ClusterC'] = data_correlacao[[f'PCL{i:02d}' for i in [6, 7]]].sum(axis=1)
    data_correlacao['PCL5_ClusterD'] = data_correlacao[[f'PCL{i:02d}' for i in [8, 9, 10, 11, 12, 13, 14]]].sum(axis=1)
    data_correlacao['PCL5_ClusterE'] = data_correlacao[[f'PCL{i:02d}' for i in [15, 16, 17, 18, 19, 20]]].sum(axis=1)

    # PTCI
    data_correlacao['PTCI_total'] = data_correlacao[[f'PTCI{i:02d}' for i in range(1, 37)]].sum(axis=1)
    data_correlacao['PTCI_ClusterA'] = data_correlacao[[f'PTCI{i:02d}' for i in [2, 3, 4, 5, 6, 9, 12, 14, 16, 17, 20, 21, 24, 25, 26, 28, 29, 30, 33, 35, 36]]].sum(axis=1)
    data_correlacao['PTCI_ClusterB'] = data_correlacao[[f'PTCI{i:02d}' for i in [7, 8, 10, 11, 18, 23, 27]]].sum(axis=1)
    data_correlacao['PTCI_ClusterC'] = data_correlacao[[f'PTCI{i:02d}' for i in [1, 15, 19, 22, 31]]].sum(axis=1)

    return data_correlacao


def criar_dataframe_para_teste_t(data_original):
    """
    Cria um DataFrame com as colunas necessárias para o teste t de Student.

    :param data_original: DataFrame original com os dados.
    :return: DataFrame modificado com as colunas necessárias.
    """
    data_teste_t = pd.DataFrame()

    if 'SEXO' in data_original.columns:
        data_teste_t['SEXO'] = data_original['SEXO']

    if all([f'PTCI{i:02d}' in data_original.columns for i in range(1, 37)]):
        # Adicionando o escore total do PTCI
        data_teste_t['PTCI_total'] = data_original[[f'PTCI{i:02d}' for i in range(1, 37)]].sum(axis=1)

        # Adicionando os escores dos clusters do PTCI
        # Assegure-se de ajustar essas linhas para corresponder às suas fórmulas específicas de clusters
        data_teste_t['PTCI_ClusterA'] = data_original[[f'PTCI{i:02d}' for i in [2, 3, 4, 5, 6, 9, 12, 14, 16, 17, 20, 21, 24, 25, 26, 28, 29, 30, 33, 35, 36]]].sum(axis=1)
        data_teste_t['PTCI_ClusterB'] = data_original[[f'PTCI{i:02d}' for i in [7, 8, 10, 11, 18, 23, 27]]].sum(axis=1)
        data_teste_t['PTCI_ClusterC'] = data_original[[f'PTCI{i:02d}' for i in [1, 15, 19, 22, 31]]].sum(axis=1)

    return data_teste_t



def realizar_teste_t_student(data, grupo1, grupo2, coluna):
    """
    Realiza o teste t de Student entre dois grupos para uma dada coluna.

    :param data: DataFrame com os dados.
    :param grupo1: Condição para o primeiro grupo (exemplo: data['SEXO'] == 'Feminino').
    :param grupo2: Condição para o segundo grupo (exemplo: data['SEXO'] == 'Masculino').
    :param coluna: Nome da coluna para a qual o teste será realizado.
    :return: Uma tupla contendo a estatística t e o p-valor.
    """
    grupo1_data = data[grupo1][coluna]
    grupo2_data = data[grupo2][coluna]

    t_stat, p_valor = stats.ttest_ind(grupo1_data, grupo2_data, nan_policy='omit')
    return t_stat, p_valor