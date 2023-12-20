import pandas as pd
import streamlit as st
from statsmodels.stats.diagnostic import kstest_normal

def calcular_pcl5_total(data):
    # Fórmulas para os clusters do PCL-5
    clusters_pcl5 = {
        'PCL5_Total': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
    }

    for cluster, questions in clusters_pcl5.items():
        data[cluster] = data[questions].sum(axis=1)

    return data


def calcular_teste_ks_pcl5_total(data):
    # Obter a contagem de linhas válidas do estado da sessão
    valid_count = st.session_state.get('valid_count', 0)

    # Suponha que `data` é o seu DataFrame e que já foi previamente carregado e filtrado
    data = calcular_pcl5_total(data)
  
    # Aplicar o teste Kolmogorov-Smirnov com a correção de Lilliefors
    statistic, p_value = kstest_normal(data['PCL5_Total'], dist='norm')[0:2]

    # Preparar a tabela de resultados
    resultados = pd.DataFrame({
        'Statistic': [statistic],
        'df': [valid_count],
        'Sig.': [p_value]
    })
    
    return resultados

