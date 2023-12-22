import pandas as pd
import matplotlib.pyplot as plt
from data_loader import DataLoader

def criar_boxplot_pcl5(data):
    DataLoader.calculos_pcl5(data)  # Preparação dos dados

    # Filtrando os dados para remover valores menores que 3
    escores_filtrados = data[data['PCL5_Total'] > 3]

    plt.figure(figsize=(10, 6))
    boxplot = plt.boxplot(escores_filtrados['PCL5_Total'], vert=True, patch_artist=True)  # Boxplot vertical
    plt.title('Boxplot dos Escores Totais do PCL-5')
    plt.ylabel('Escore do PCL-5')
    plt.grid(True)

    # Definindo a cor da barra do boxplot
    cor_barra = 'lightgray'
    for patch in boxplot['boxes']:
        patch.set_facecolor(cor_barra)

    # Definindo cor dos elementos para preto
    plt.setp(boxplot['whiskers'], color='black')
    plt.setp(boxplot['caps'], color='black')
    plt.setp(boxplot['medians'], color='black')

    # Adicionando os valores dos pontos importantes de forma mais clara
    whiskers = [item.get_ydata() for item in boxplot['whiskers']]
    caps = [item.get_ydata() for item in boxplot['caps']]
    fliers = [item.get_ydata() for item in boxplot['fliers']]
    medians = [item.get_ydata() for item in boxplot['medians']]

    plt.text(1.1, whiskers[0][0], f'Q1: {whiskers[0][0]:.2f}', verticalalignment='center', size='small', color='black')
    plt.text(1.1, whiskers[1][0], f'Q3: {whiskers[1][0]:.2f}', verticalalignment='center', size='small', color='black')
    plt.text(1.1, medians[0][0], f'Mediana: {medians[0][0]:.2f}', verticalalignment='center', size='small', color='black')
    plt.text(1.1, caps[0][0], f'Min: {caps[0][0]:.2f}', verticalalignment='center', size='small', color='black')
    plt.text(1.1, caps[1][1], f'Max: {caps[1][1]:.2f}', verticalalignment='center', size='small', color='black')

    # Ajustando posição dos outliers para evitar sobreposição de textos
    if boxplot['fliers']:
        flier_data = boxplot['fliers'][0].get_ydata()
        for outlier in flier_data:
            plt.text(1.02, outlier, f'{outlier:.2f}', verticalalignment='center', size='small', color='black')

    # Retornando o objeto da figura para posterior processamento e exibição
    return plt.gcf()
