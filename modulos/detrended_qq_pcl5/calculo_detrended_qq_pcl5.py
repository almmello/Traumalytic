import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from data_loader import DataLoader
import pandas as pd

def criar_detrended_qq_pcl5(data):
    DataLoader.calculos_pcl5(data)  # Preparação dos dados

    # Filtrando os dados para remover valores menores que 3 e selecionando apenas a coluna 'PCL5_Total'
    escores_filtrados = data[data['PCL5_Total'] >= 3]['PCL5_Total']

    # Calculando os resíduos da tendência linear
    z = (escores_filtrados - np.mean(escores_filtrados)) / np.std(escores_filtrados)
    (osm, osr), (slope, intercept, r) = stats.probplot(z, dist='norm', plot=None)
    trend = (slope * osm + intercept)
    detrended = osr - trend

    # Criando o gráfico de probabilidade normal (Q-Q Plot) detrended
    plt.figure(figsize=(10, 6))
    plt.scatter(osm, detrended, edgecolor='k')
    plt.axhline(y=0, color='grey', linestyle='dashed')

    plt.title('Detrended Normal Q-Q Plot of PCL5 Total')
    plt.ylabel('Desvios da Normal')
    plt.xlabel('Valores Observados')
    plt.grid(True)

    # Retornando o objeto da figura para posterior processamento e exibição
    return plt.gcf()
