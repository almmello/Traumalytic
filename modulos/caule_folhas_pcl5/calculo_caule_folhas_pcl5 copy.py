import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import stemgraphic
from data_loader import DataLoader


def calcular_caule_folhas_pcl5(data):
    DataLoader.calculos_pcl5(data)  # A função de preparação dos dados.
    
    # Filtrando os dados para remover valores menores ou iguais a 3
    escores_limpos = data['PCL5_Total'].dropna().astype(int)
    escores_filtrados = escores_limpos[escores_limpos > 3]

    # Gerando a exibição de caule-e-folhas com a biblioteca stemgraphic
    fig, ax = stemgraphic.stem_graphic(
        escores_filtrados,
        scale=10,  # A escala é definida como 10
        aggregation=False,  # Não agrupar dados similares
        leaf_order=1,  # Ordem da folha
        asc=False,  # Ordem decrescente
        break_on=5,  # Força a quebra das folhas no número 5
    )
    
    # Configuração da figura para se assemelhar ao template fornecido
    ax.set_title('PCL5total Stem-and-Leaf Plot')
    ax.set_ylabel('Stem')
    ax.set_xlabel('Leaf')

    # Retornando a figura para que possa ser exibida no Streamlit ou em qualquer outra plataforma
    return fig, ax

# Exemplo de uso da função
# data = DataLoader.load_data('caminho_para_seu_arquivo.csv')
# fig = calcular_caule_folhas_pcl5(data)
# fig.show()  # ou st.pyplot(fig) se estiver usando Streamlit

import pandas as pd

def criar_tabela_caule_folhas(data):
    # Preparação dos dados, excluindo valores menores ou iguais a 3
    DataLoader.calculos_pcl5(data)
    escores_limpos = data['PCL5_Total'].dropna().astype(int)
    escores_filtrados = escores_limpos[escores_limpos > 3]

    # Dividindo os dados em caules e folhas
    caules = escores_filtrados // 10
    folhas = escores_filtrados % 10

    # Criando um DataFrame para armazenar os caules e folhas
    df_caule_folhas = pd.DataFrame({'Stem': caules, 'Leaf': folhas})

    # Agrupando os dados por caule e concatenando as folhas em uma string
    tabela_caule_folhas = df_caule_folhas.groupby('Stem')['Leaf'].apply(lambda x: ''.join(x.astype(str))).reset_index()

    return tabela_caule_folhas



