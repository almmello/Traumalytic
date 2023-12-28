import pandas as pd
import streamlit as st
from scipy.stats import shapiro
from data_loader import DataLoader

def calcular_shapiro_wilk_ptci_total(data):
    DataLoader.calculos_ptci(data)  # Preparação dos dados

    # Obter a contagem de linhas válidas do estado da sessão
    valid_count = len(data['PTCI_Total'].dropna())

    # Aplicar o teste de Shapiro-Wilk
    statistic, p_value = shapiro(data['PTCI_Total'])

    # Preparar a tabela de resultados
    resultados = pd.DataFrame({
        'Statistic': [statistic],
        'df': [valid_count],
        'Sig.': [p_value]
    })
    
    return resultados
