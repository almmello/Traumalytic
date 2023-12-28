import pandas as pd

def formatar_resultados_para_texto(resultados):
    texto = ""
    for coluna, estatisticas in resultados.items():
        texto += f"Estatísticas para '{coluna}':\n"
        texto += estatisticas.to_string() + "\n\n"
    return texto


def calcular_estatisticas_variaveis_categoricas(data, coluna):
    """
    Calcula estatísticas relevantes para uma coluna categórica.
    """
    frequencia = data[coluna].value_counts()
    proporcao = data[coluna].value_counts(normalize=True) * 100
    moda = data[coluna].mode()[0]

    estatisticas = pd.DataFrame({
        'Frequência': frequencia,
        'Proporção (%)': proporcao,
        'Moda': moda
    })

    return estatisticas

