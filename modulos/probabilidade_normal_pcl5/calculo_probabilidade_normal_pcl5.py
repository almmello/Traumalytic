import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from data_loader import DataLoader
import pandas as pd

def criar_probabilidade_normal_pcl5(data):
    DataLoader.calculos_pcl5(data)  # Preparação dos dados

    # Filtrando os dados para remover valores menores que 3 e selecionando apenas a coluna 'PCL5_Total'
    escores_filtrados = data[data['PCL5_Total'] > 3]['PCL5_Total']

    # Criando o gráfico de probabilidade normal (Q-Q Plot)
    plt.figure(figsize=(10, 6))
    stats.probplot(escores_filtrados, dist="norm", plot=plt)

    plt.title('Gráfico de Probabilidade Normal dos Escores Totais do PCL-5')
    plt.ylabel('Valores Observados')
    plt.xlabel('Quantis Teóricos da Distribuição Normal')
    plt.grid(True)

    # Retornando o objeto da figura para posterior processamento e exibição
    return plt.gcf()