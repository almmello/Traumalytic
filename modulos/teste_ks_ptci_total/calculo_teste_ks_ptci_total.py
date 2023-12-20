import pandas as pd
import streamlit as st
from statsmodels.stats.diagnostic import kstest_normal

def calcular_ptci_total(data):
    # Fórmulas para os clusters do PTCI
    clusters_ptci = {
        'PTCI_Total': ['PTCI01', 'PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI07', 'PTCI08', 'PTCI09', 'PTCI10', 'PTCI11', 'PTCI12', 'PTCI14', 'PTCI15', 'PTCI16', 'PTCI17', 'PTCI18', 'PTCI19', 'PTCI20', 'PTCI21', 'PTCI22', 'PTCI23', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI27', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI31', 'PTCI33', 'PTCI35', 'PTCI36']
    }

    # Calcula a soma e média para cada cluster
    for cluster, questions in clusters_ptci.items():
        data[cluster] = data[questions].sum(axis=1)
  
    return data


def calcular_teste_ks_ptci_total(data):
    # Obter a contagem de linhas válidas do estado da sessão
    valid_count = st.session_state.get('valid_count', 0)

    # Suponha que `data` é o seu DataFrame e que já foi previamente carregado e filtrado
    data = calcular_ptci_total(data)

    # Aplicar o teste Kolmogorov-Smirnov com a correção de Lilliefors
    statistic, p_value = kstest_normal(data['PTCI_Total'], dist='norm')[0:2]

    # Preparar a tabela de resultados
    resultados = pd.DataFrame({
        'Statistic': [statistic],
        'df': [valid_count],
        'Sig.': [p_value]
    })
    
    return resultados

