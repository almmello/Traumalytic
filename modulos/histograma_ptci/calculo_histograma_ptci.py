import pandas as pd
import matplotlib.pyplot as plt

def calcular_ptci_total(data):
    # Fórmulas para os clusters do PTCI
    clusters_ptci = {
        'PTCI_Total': ['PTCI01', 'PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI07', 'PTCI08', 'PTCI09', 'PTCI10', 'PTCI11', 'PTCI12', 'PTCI14', 'PTCI15', 'PTCI16', 'PTCI17', 'PTCI18', 'PTCI19', 'PTCI20', 'PTCI21', 'PTCI22', 'PTCI23', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI27', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI31', 'PTCI33', 'PTCI35', 'PTCI36']
    }

    # Calcula a soma e média para cada cluster
    for cluster, questions in clusters_ptci.items():
        data[cluster] = data[questions].sum(axis=1)
  
    return data

def criar_histograma(data, coluna, descricao_x, descricao_y):
    ptci_clusters = calcular_ptci_total(data)
    plt.figure()
    plt.hist(ptci_clusters[coluna].dropna(), bins=30, edgecolor='black')
    plt.title(f'Histograma do {coluna}')
    plt.xlabel(descricao_x)
    plt.ylabel(descricao_y)
    plt.grid(True)
    return plt.gcf()



