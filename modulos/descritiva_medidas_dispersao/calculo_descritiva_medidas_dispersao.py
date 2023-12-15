def calcular_descritiva_medidas_dispersao(data, coluna):
    """
    Calcula as medidas de dispersão para uma coluna específica.
    """
    desvio_padrao = data[coluna].std()
    variancia = data[coluna].var()
    amplitude = data[coluna].max() - data[coluna].min()
    return {'Desvio Padrão': desvio_padrao, 'Variância': variancia, 'Amplitude': amplitude}
