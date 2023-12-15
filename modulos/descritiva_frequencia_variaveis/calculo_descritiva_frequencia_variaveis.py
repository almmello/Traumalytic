

def calcular_descritiva_frequencia_variaveis(data, coluna):
    """
    Calcula a frequência de valores em uma coluna categórica.
    """
    frequencia = data[coluna].value_counts(normalize=True) * 100
    return frequencia
