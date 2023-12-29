import pandas as pd

def formatar_resultados_para_texto(resultados):
    texto = ""
    for coluna, estatisticas in resultados.items():
        texto += f"Estatísticas para '{coluna}':\n"
        texto += estatisticas.to_string() + "\n\n"
    return texto


import pandas as pd
import numpy as np

def calcular_estatisticas_variaveis_categoricas(data, coluna):
    """
    Calcula estatísticas relevantes para uma coluna categórica, incluindo a contagem total
    e a contagem de valores nulos.
    """
    # Contando frequência incluindo NaN como uma categoria
    frequencia = data[coluna].value_counts(dropna=False)
    
    # Se NaN está presente, mover a contagem para "Valores Nulos"
    if np.nan in frequencia:
        frequencia_nulos = frequencia[np.nan]
        del frequencia[np.nan]
        frequencia['Valores Nulos'] = frequencia_nulos
    else:
        frequencia['Valores Nulos'] = 0

    # Calculando proporções
    total_valores = data[coluna].size
    proporcao = (frequencia / total_valores) * 100

    # Encontrando a moda (ignorando NaN)
    moda = data[coluna].dropna().mode()[0] if not data[coluna].mode().empty else 'N/A'

    estatisticas = pd.DataFrame({
        'Frequência': frequencia,
        'Proporção (%)': proporcao,
        'Moda': moda
    })

    # Adicionando linha para a contagem total
    estatisticas.loc['Total'] = [total_valores, "--", "--"]

    return estatisticas


