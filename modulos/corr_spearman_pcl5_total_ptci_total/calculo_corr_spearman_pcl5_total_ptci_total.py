import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as stats

def criar_corr_spearman_pcl5_total_ptci_total(data):
    data_correlacao = pd.DataFrame()

    # Adicionando colunas de PCL-5 e PTCI
    for i in range(1, 21):
        data_correlacao[f'PCL{i:02d}'] = data[f'PCL{i:02d}']
    for i in range(1, 37):
        data_correlacao[f'PTCI{i:02d}'] = data[f'PTCI{i:02d}']

    # Cálculos dos escores totais
    data_correlacao['PCL5_Total'] = data_correlacao[[f'PCL{i:02d}' for i in range(1, 21)]].sum(axis=1)
    data_correlacao['PTCI_Total'] = data_correlacao[[f'PTCI{i:02d}' for i in range(1, 37)]].sum(axis=1)

    # Calculando a correlação de Spearman
    correlacao, p_value = stats.spearmanr(data_correlacao['PCL5_Total'], data_correlacao['PTCI_Total'])
    n = len(data_correlacao)

    # Criando um DataFrame para o mapa de calor
    df_heatmap = pd.DataFrame({
        'PCL5_Total': [1, correlacao],  # Inserir um valor neutro para a segunda célula
        'PTCI_Total': [correlacao, 1]  # Inserir um valor neutro para a primeira célula
    }, index=['PCL5_Total', 'PTCI_Total'])

    # Formatando os valores para o mapa de calor
    labels = [["1", f"{correlacao:.3f}\nSig: {p_value:.3f}\nN: {n}"], [f"{correlacao:.3f}\nSig: {p_value:.3f}\nN: {n}", "1"]]

    # Criando o mapa de calor
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df_heatmap, annot=labels, fmt="", cmap='coolwarm', cbar=True, ax=ax)
    ax.set_title('Mapa de Calor de Correlação Spearman entre PCL5 Total e PTCI Total')
    plt.yticks(rotation=0)
    return fig
