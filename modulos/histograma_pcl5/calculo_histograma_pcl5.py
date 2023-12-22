import pandas as pd
import matplotlib.pyplot as plt
from data_loader import DataLoader

def criar_histograma(data, coluna, descricao_x, descricao_y):
    DataLoader.calculos_pcl5(data)  # A função de preparação dos dados.

    plt.figure()
    plt.hist(data[coluna].dropna(), bins=30, edgecolor='black')
    plt.title(f'Histograma de {coluna}')
    plt.xlabel(descricao_x)
    plt.ylabel(descricao_y)
    plt.grid(True)
    return plt.gcf()



