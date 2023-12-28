import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from data_loader import DataLoader
import pandas as pd

def criar_probabilidade_normal_ptci(data):
    DataLoader.calculos_ptci(data)  # Preparação dos dados

    # Supondo que 'PTCI_Total' seja a coluna com os escores totais do PTCI
    escores_filtrados = data[data['PTCI_Total'] > 3]['PTCI_Total']

    # Criando o gráfico de probabilidade normal
    plt.figure(figsize=(10, 6))
    stats.probplot(escores_filtrados, dist="norm", plot=plt)

    plt.title('Gráfico de Probabilidade Normal dos Escores Totais do PTCI')
    plt.ylabel('Valores Observados')
    plt.xlabel('Quantis Teóricos da Distribuição Normal')
    plt.grid(True)

    # Retornando o objeto da figura para posterior processamento e exibição
    return plt.gcf()
