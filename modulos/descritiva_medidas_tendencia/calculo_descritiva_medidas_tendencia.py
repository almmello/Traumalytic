def calcular_descritiva_medidas_tendencia(data, coluna):
    """
    Calcula as medidas de tendência central para uma coluna específica.
    """
    media = data[coluna].mean()
    mediana = data[coluna].median()
    moda = data[coluna].mode()[0]
    return {'Média': media, 'Mediana': mediana, 'Moda': moda}