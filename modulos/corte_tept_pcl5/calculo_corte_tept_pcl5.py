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

def gerar_estatisticas_gerais_tept():
    # Usa o estado da sessão para obter o número de itens válidos e faltantes
    valid_count = st.session_state.get('valid_count', 0)
    missing_count = st.session_state.get('missing_count', 0)

    estatisticas_gerais = {
        'N': [valid_count + missing_count],
        'Valid': [valid_count],
        'Missing': [missing_count]
    }
    
    estatisticas_df = pd.DataFrame(estatisticas_gerais, index=['Count'])

    return estatisticas_df



def gerar_frequencias_tept(data):
    ponto_de_corte = st.session_state.get('ponto_de_corte_tept')
    calcular_clusters_pcl5(data)
    data['TEPT_Diag'] = (data['PCL5_Total'] >= ponto_de_corte).astype(int)
    
    valid_total = st.session_state['valid_count']
    missing_system = st.session_state['missing_count']
    total = valid_total + missing_system
    
    freq = {
        'NO': valid_total - data['TEPT_Diag'].sum(),
        'YES': data['TEPT_Diag'].sum()
    }
    
    percent = {key: "{:.2f}".format(val / total * 100) for key, val in freq.items()}
    valid_percent = {key: "{:.2f}".format(val / valid_total * 100) for key, val in freq.items()}
    
    freq_table = pd.DataFrame({
        'PCL5 DIAGN_CUTOFF': ['Valid - NO', 'Valid - YES', 'Valid - Total', 'Missing', 'Total'],
        'Frequency': [freq['NO'], freq['YES'], valid_total, missing_system, total],
        'Percent': [percent['NO'], percent['YES'], "{:.2f}".format((freq['NO'] + freq['YES']) / total * 100), "{:.2f}".format(missing_system / total * 100), '100.00'],
        'Valid Percent': [valid_percent['NO'], valid_percent['YES'], '', '', ''],
        'Cumulative Percent': ['', '', '', '', '']
    })
    
    freq_table.at[0, 'Cumulative Percent'] = valid_percent['NO']
    freq_table.at[1, 'Cumulative Percent'] = '100.00'
    
    return freq_table




