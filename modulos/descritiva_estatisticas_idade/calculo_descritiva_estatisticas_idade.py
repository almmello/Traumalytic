
def calcular_estatisticas(data, coluna):
    return data[coluna].agg(['mean', 'std', 'min', 'max'])