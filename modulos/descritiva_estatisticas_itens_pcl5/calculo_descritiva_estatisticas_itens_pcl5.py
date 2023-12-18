import pandas as pd

def calcular_descritiva_estatisticas_itens_pcl5(data):
    if data.empty:
        return pd.DataFrame()

    # Lista de colunas do PCL-5 com a nomenclatura correta
    pcl5_cols = [f'PCL{i:02d}' for i in range(1, 21)]

    # Calculando as estatísticas descritivas
    descritivas = data[pcl5_cols].describe().transpose()
    descritivas = descritivas.rename(columns={
        'count': 'N',
        'min': 'Minimum',
        'max': 'Maximum',
        'mean': 'Mean',
        'std': 'Std. Deviation'
    })

    # Reordenando as colunas para corresponder à saída desejada
    descritivas = descritivas[['N', 'Minimum', 'Maximum', 'Mean', 'Std. Deviation']]
    return descritivas


def formatar_resultados_para_conclusao(resultados):
    if resultados.empty:
        return "Nenhum dado para análise."

    # Formatação de cada linha do DataFrame em uma string
    linhas_formatadas = []
    for index, row in resultados.iterrows():
        linha = f"{index}: N={row['N']}, Mínimo={row['Minimum']}, Máximo={row['Maximum']}, Média={row['Mean']:.2f}, Desvio Padrão={row['Std. Deviation']:.2f}"
        linhas_formatadas.append(linha)

    # Unindo todas as linhas em uma única string
    texto_formatado = "\n".join(linhas_formatadas)
    return texto_formatado
