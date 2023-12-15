import pandas as pd
from scipy import stats
from scipy.stats import shapiro
import matplotlib.pyplot as plt
from scipy.stats import probplot
import numpy as np


def calcular_clusters_pcl5_e_retornar(data):
    clusters_pcl5 = {
        'Cluster_B': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05'],
        'Cluster_C': ['PCL06', 'PCL07'],
        'Cluster_D': ['PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14'],
        'Cluster_E': ['PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20'],
        'PCL5_total': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
    }

    pcl5_clusters = pd.DataFrame()
    for cluster, questions in clusters_pcl5.items():
        pcl5_clusters[cluster] = data[questions].sum(axis=1)
    
    return pcl5_clusters

def testar_normalidade_pcl5(data):
    # Calcular os escores dos clusters e o escore total para o PCL-5
    pcl5_clusters = calcular_clusters_pcl5_e_retornar(data)

    # Executar o teste de Shapiro-Wilk
    resultados_normalidade = {}
    for cluster, escores in pcl5_clusters.items():
        valid_data = escores.dropna()
        if len(valid_data) > 3:  # Shapiro-Wilk requer pelo menos 3 valores não-nulos
            stat, p = shapiro(valid_data)
            resultados_normalidade[cluster] = p
        else:
            resultados_normalidade[cluster] = 'Dados insuficientes para teste'

    return resultados_normalidade, pcl5_clusters

def formatar_p_valor(p_valor):
    return f"{p_valor:.2f}" if p_valor > 0.0001 else f"{p_valor:.2e}"

def criar_histograma(data, coluna, descricao_x='Valores', descricao_y='Frequência'):
    plt.figure()
    plt.hist(data[coluna].dropna(), bins=30, edgecolor='black')
    plt.title(f'Histograma de {coluna}')
    plt.xlabel(descricao_x)
    plt.ylabel(descricao_y)
    plt.grid(True)
    return plt.gcf()

def criar_grafico_qq(data, coluna, descricao_x='Quantis Teóricos', descricao_y='Quantis Reais'):
    plt.figure()
    probplot(data[coluna].dropna(), dist="norm", plot=plt)
    plt.title(f'Gráfico Q-Q para {coluna}')
    plt.xlabel(descricao_x)
    plt.ylabel(descricao_y)
    return plt.gcf()

# Gera uma amostra de dados seguindo uma distribuição normal.
def gerar_dados_normal(n=100, media=0, desvio_padrao=1):
    dados_normal = np.random.normal(loc=media, scale=desvio_padrao, size=n)
    return dados_normal

# Calcula o p-valor para uma amostra de dados, assumindo uma distribuição normal.
def calcular_p_valor_normal(dados):
    
    stat, p = shapiro(dados)
    return p

def interpretar_resultados_a(p_valor):
    p_valor_formatado = formatar_p_valor(p_valor)
    conclusao_a = "\n### Interpretação do Resultado\n"
    conclusao_a += f"Os dados {'não ' if p_valor < 0.05 else ''}parecem seguir uma distribuição normal, pois o resultado {p_valor_formatado} é {'menor' if p_valor < 0.05 else 'maior'} que 0.05.\n"
    conclusao_a += "\n### Análise do Histograma\n"
    conclusao_a += "Isso é corroborado pelo histograma, onde esperamos ver uma forma de sino para uma distribuição normal.\n"
    conclusao_a += "\n##### Exemplo de Histograma com uma distribuição normal\n"
    return conclusao_a

def interpretar_resultados_b(p_valor):
    conclusao_b = "\n### Análise do Gráfico QQ\n"
    conclusao_b += "Numa distribuição normal, o gráfico Q-Q deve mostrar os pontos alinhados com a linha reta. Desvios significativos da linha no gráfico Q-Q indicam desvios da normalidade."
    conclusao_b += "\n##### Exemplo de Gráfico Q-Q com uma distribuição normal\n"
    return conclusao_b

