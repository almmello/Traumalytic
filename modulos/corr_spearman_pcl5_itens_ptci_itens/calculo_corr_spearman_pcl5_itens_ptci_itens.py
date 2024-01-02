import plotly.graph_objects as go
import pandas as pd
import scipy.stats as stats
import numpy as np
import streamlit as st

from data_loader import DataLoader

def criar_corr_spearman_pcl5_itens_ptci_itens(data):
    # Utilize as funções de cálculo de clusters para adicionar os clusters ao dataframe
    DataLoader.calculos_pcl5(data)  # Preparação dos dados
    DataLoader.calculos_ptci(data)  # Preparação dos dados

    # Defina os itens de PCL-5 e PTCI
    vertical_axe = ['PTCI01', 'PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI07', 'PTCI08', 'PTCI09', 'PTCI10', 'PTCI11', 'PTCI12', 'PTCI13', 'PTCI14', 'PTCI15', 'PTCI16', 'PTCI17', 'PTCI18', 'PTCI19', 'PTCI20', 'PTCI21', 'PTCI22', 'PTCI23', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI27', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI31', 'PTCI32', 'PTCI33', 'PTCI34', 'PTCI35', 'PTCI36']
    horizontal_axe = ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']

    # Preparar o DataFrame para o mapa de calor
    heatmap_data = pd.DataFrame(index=vertical_axe, columns=horizontal_axe)
    p_values_data = pd.DataFrame(index=vertical_axe, columns=horizontal_axe)

    # Calcular a correlação entre os itens de PCL-5 e PTCI usando Spearman
    for v_column in vertical_axe:
        for h_column in horizontal_axe:
            correlacao, p_value = stats.spearmanr(data[v_column], data[h_column])
            heatmap_data.loc[v_column, h_column] = correlacao
            p_values_data.loc[v_column, h_column] = p_value

    # Converter os dados para um formato compatível com o Plotly
    heatmap_data_plotly = heatmap_data.values
    p_values_data_plotly = p_values_data.values

    # Criar o texto para anotações
    annotations = np.vectorize(lambda correlacao, p_value: f"{correlacao:.3f}<br>Sig: {p_value:.3f}<br>N: {len(data)}")(
        heatmap_data_plotly, p_values_data_plotly)

    # Criar o gráfico base
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data_plotly,
        x=horizontal_axe,
        y=vertical_axe,
        colorscale='bluered',
        text=annotations,
        texttemplate="%{text}"
    ))

    # Adicionar títulos e ajustar layout
    fig.update_layout(
        title='Mapa de Calor de Correlação Spearman entre Itens do PCL-5 e PTCI',
        xaxis=dict(title='PCL-5', side='bottom'),
        yaxis=dict(title='PTCI', autorange='reversed'),
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        xaxis_nticks=len(horizontal_axe),
        yaxis_nticks=len(vertical_axe),
        autosize=False,
        width=900,
        height=900,
        margin=dict(l=100, r=100, b=100, t=100)
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Obter o tamanho da amostra para o 'N'
    n = len(data)

    # Criar uma tabela com os resultados do mapa de calor
    resultados = pd.DataFrame(index=vertical_axe, columns=horizontal_axe)
    for v in vertical_axe:
        for h in horizontal_axe:
            correlacao = heatmap_data.loc[v, h]
            p_value = p_values_data.loc[v, h]
            resultados.loc[v, h] = f"r={correlacao:.3f}\nSig={p_value:.3f}\nN={n}"
    
    return resultados
