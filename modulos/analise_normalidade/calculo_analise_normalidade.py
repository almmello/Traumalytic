import pandas as pd
from scipy import stats
from scipy.stats import shapiro
import matplotlib.pyplot as plt
from scipy.stats import probplot
import numpy as np


from modulos.analise_descritiva.calculo_analise_descritiva import (
    calcular_clusters_ptci_e_retornar,
    calcular_clusters_pcl5_e_retornar,
)


# Gera uma amostra de dados seguindo uma distribuição normal.
def gerar_dados_normal(n=100, media=0, desvio_padrao=1):
    dados_normal = np.random.normal(loc=media, scale=desvio_padrao, size=n)
    return dados_normal

# Calcula o p-valor para uma amostra de dados, assumindo uma distribuição normal.
def calcular_p_valor_normal(dados):
    
    stat, p = shapiro(dados)
    return p

def formatar_p_valor(p_valor):
    return f"{p_valor:.2f}" if p_valor > 0.0001 else f"{p_valor:.2e}"

def interpretar_resultados_a(p_valor):
    p_valor_formatado = formatar_p_valor(p_valor)
    conclusao_a = "\n### Conclusão\n"
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



def testar_normalidade(data):

    # Calcular os escores dos clusters e totais para PCL-5 e PTCI
    pcl5_clusters = calcular_clusters_pcl5_e_retornar(data)
    ptci_clusters = calcular_clusters_ptci_e_retornar(data)

    data_escores = pd.DataFrame()
    data_escores['PCL5_total'] = pcl5_clusters.sum(axis=1)
    data_escores['PTCI_total'] = ptci_clusters.sum(axis=1)

    for cluster in pcl5_clusters.columns:
        data_escores[cluster] = pcl5_clusters[cluster]

    for cluster in ptci_clusters.columns:
        data_escores[cluster] = ptci_clusters[cluster]

    # Executar o teste de Shapiro-Wilk
    resultados = {}
    for var in data_escores.columns:
        valid_data = data_escores[var].dropna()
        if len(valid_data) > 3:  # Shapiro-Wilk requer pelo menos 3 valores não-nulos
            stat, p = shapiro(valid_data)
            resultados[var] = p
        else:
            resultados[var] = 'Dados insuficientes para teste'

    return resultados, data_escores


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





