import pandas as pd
import streamlit as st


def calcular_clusters_pcl5(data):
    # Fórmulas para os clusters do PCL-5
    clusters_pcl5 = {
        'Cluster_B': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05'],
        'Cluster_C': ['PCL06', 'PCL07'],
        'Cluster_D': ['PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14'],
        'Cluster_E': ['PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20'],
        'PCL5_Total': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
    }

    for cluster, questions in clusters_pcl5.items():
        data[cluster] = data[questions].sum(axis=1)
        data[cluster + '_media'] = data[cluster] / len(questions)

    return data

def gerar_estatisticas_gerais_tept(data):
    ponto_de_corte = st.session_state['ponto_de_corte_tept']
    # Calcula os clusters e o escore total do PCL-5
    data = calcular_clusters_pcl5(data)
    
    # Aplica o ponto de corte
    data['TEPT_Diag'] = (data['PCL5_Total'] >= ponto_de_corte).astype(int)
    
    estatisticas_gerais = {
        'N': [data.shape[0]],
        'Valid': [data['TEPT_Diag'].notna().sum()],
        'Missing': [data['TEPT_Diag'].isna().sum()]
    }
    
    return pd.DataFrame(estatisticas_gerais)

def gerar_frequencias_tept(data):
    # Assume que 'TEPT_Diag' já foi calculado
    freq = data['TEPT_Diag'].value_counts(normalize=True)
    freq_df = freq.to_frame('Frequency')
    freq_df['Percent'] = (freq_df['Frequency'] * 100).round(1)
    freq_df['Valid Percent'] = (freq_df['Frequency'] / freq_df['Frequency'].sum() * 100).round(1)
    freq_df['Cumulative Percent'] = freq_df['Valid Percent'].cumsum().round(1)
    
    # Renomeia o índice
    freq_df.index = ['NO' if i == 0 else 'YES' for i in freq_df.index]
    freq_df.reset_index(inplace=True)
    freq_df.rename(columns={'index': 'PCL5 DIAGN_CUTOFF'}, inplace=True)
    
    return freq_df

