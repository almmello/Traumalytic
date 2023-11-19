import pandas as pd
from scipy import stats
from scipy.stats import shapiro
import matplotlib.pyplot as plt
from scipy.stats import probplot
import numpy as np


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