import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
from data_loader import DataLoader

def criar_teste_t_pcl5_total_ptci_total(data):
    DataLoader.calculos_pcl5(data)
    DataLoader.calculos_ptci(data)

    # Realizando o teste T de Student
    t_statistic, p_value = stats.ttest_ind(data['PCL5_Total'], data['PTCI_Total'])

    # Preparar dados para o gráfico
    medias = [data['PCL5_Total'].mean(), data['PTCI_Total'].mean()]
    desvios = [data['PCL5_Total'].std(), data['PTCI_Total'].std()]
    grupos = ['PCL5 Total', 'PTCI Total']

    # Criando o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(grupos, medias, yerr=desvios, capsize=10, color=['blue', 'green'])
    ax.set_ylabel('Média dos Escores')
    ax.set_title(f'Teste T entre PCL5 Total e PTCI Total\nT-Statistic: {t_statistic:.2f}, P-Value: {p_value:.6f}')

    # Adicionar linha horizontal para facilitar a comparação
    ax.axhline(y=medias[0], color='blue', linestyle='--')
    ax.axhline(y=medias[1], color='green', linestyle='--')

    # Preparar DataFrame com os resultados
    resultados_df = pd.DataFrame({
        'Grupo': ['PCL5 Total', 'PTCI Total'],
        'Média': medias,
        'Desvio Padrão': desvios,
        'N': [len(data['PCL5_Total']), len(data['PTCI_Total'])]
    })
    resultados_df.loc['Teste T'] = ['T-Statistic', t_statistic, 'P-Value', p_value]

    return fig, resultados_df
