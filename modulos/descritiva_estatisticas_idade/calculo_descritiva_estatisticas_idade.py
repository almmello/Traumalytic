
def calcular_estatisticas(data, colunas):
    estatisticas = data[colunas].agg(['min', 'max', 'mean', 'std', 'count', 'kurtosis', 'skew', 'quantile'])
    return estatisticas
