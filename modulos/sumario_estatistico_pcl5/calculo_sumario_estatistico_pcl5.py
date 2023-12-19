import pandas as pd
import streamlit as st
import numpy as np
from scipy import stats
from scipy.stats import trim_mean



def gerar_sumario_validade_pcl5():
    valid_count = st.session_state.get('valid_count', 0)
    missing_count = st.session_state.get('missing_count', 0)
    total_count = valid_count + missing_count

    sumario_validade = pd.DataFrame({
        'Valid - N': [valid_count],  # Mesmo número para PCL-5 e PTCI
        'Valid - Percent': [f"{valid_count / total_count * 100:.2f}%"],
        'Missing - N': [missing_count],  # Mesmo número para PCL-5 e PTCI
        'Missing - Percent': [f"{missing_count / total_count * 100:.2f}%"],
        'Total - N': [total_count],
        'Total - Percent': ['100.00%']  # Total sempre será 100%
    }, index=['PCL-5 Total'])

    return sumario_validade



def calcular_clusters_pcl5(data):
    # Fórmulas para os clusters do PCL-5
    clusters_pcl5 = {
        'PCL5_Total': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
    }

    for cluster, questions in clusters_pcl5.items():
        data[cluster] = data[questions].sum(axis=1)

    return data



def gerar_descritivos_estatisticos_pcl5(data):
    escore_col = 'PCL5_Total'
    calcular_clusters_pcl5(data)
     
    # Cálculo das estatísticas descritivas
    mean = data[escore_col].mean()
    std_err_mean = data[escore_col].sem()  # Std. Error of the mean
    ci_lower, ci_upper = stats.norm.interval(0.95, loc=mean, scale=std_err_mean)
    trimmed_mean_val = trim_mean(data[escore_col], 0.05)
    median_val = data[escore_col].median()
    variance = data[escore_col].var()
    std_dev = data[escore_col].std()
    min_val = data[escore_col].min()
    max_val = data[escore_col].max()
    range_val = max_val - min_val
    q1 = data[escore_col].quantile(0.25)
    q3 = data[escore_col].quantile(0.75)
    iqr = q3 - q1
    skewness = data[escore_col].skew()
    kurtosis = data[escore_col].kurt()
    
    N = len(data[escore_col])
    std_err_skew = np.sqrt(6.0 / N)
    std_err_kurt = np.sqrt(24.0 / N)
    
    descritivos = {
        'Statistic': [
            mean, ci_lower, ci_upper, trimmed_mean_val, median_val, 
            variance, std_dev, min_val, max_val, range_val, iqr, skewness, kurtosis
        ],
        'Std. Error': [
            std_err_mean, '', '', '', '', 
            '', '', '', '', '', '', std_err_skew, std_err_kurt
        ]
    }
    
    descritivos_df = pd.DataFrame(descritivos, index=[
        'Mean', '95% CI Lower Bound', '95% CI Upper Bound', '5% Trimmed Mean', 'Median', 
        'Variance', 'Std. Deviation', 'Minimum', 'Maximum', 'Range', 
        'Interquartile Range', 'Skewness', 'Kurtosis'
    ])
    
    return descritivos_df




