import pandas as pd

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