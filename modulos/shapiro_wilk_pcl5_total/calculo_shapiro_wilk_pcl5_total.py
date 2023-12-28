import pandas as pd
import streamlit as st
from scipy.stats import shapiro
from data_loader import DataLoader

def calcular_shapiro_wilk_pcl5_total(data):
    DataLoader.calculos_pcl5(data)  # Preparação dos dados

    # Obter a contagem de linhas válidas do estado da sessão
    valid_count = len(data['PCL5_Total'].dropna())

    # Aplicar o teste de Shapiro-Wilk
    statistic, p_value = shapiro(data['PCL5_Total'])

    # Preparar a tabela de resultados
    resultados = pd.DataFrame({
        'Statistic': [statistic],
        'df': [valid_count],
        'Sig.': [p_value]
    })
    
    return resultados
