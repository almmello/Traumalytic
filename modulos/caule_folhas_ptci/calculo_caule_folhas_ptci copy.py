import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import stemgraphic
from data_loader import DataLoader


def calcular_caule_folhas_ptci(data):
    DataLoader.calculos_ptci(data)  # A função de preparação dos dados.
    
    # Filtrando os dados para remover valores menores ou iguais a 3
    escores_limpos = data['PTCI_Total'].dropna().astype(int)
    escores_filtrados = escores_limpos[escores_limpos > 3]

    # Gerando a exibição de caule-e-folhas com a biblioteca stemgraphic
    fig, ax = stemgraphic.stem_graphic(
        escores_filtrados,
        scale=10,  # A escala é definida como 10
        aggregation=False,  # Não agrupar dados similares
        leaf_order=1,  # Ordem da folha
        asc=False,  # Ordem decrescente
        box=True,
        # break_on=5,  # Força a quebra das folhas no número 5
    )
    
    # Configuração da figura para se assemelhar ao template fornecido
    ax.set_title('PTCI Total Stem-and-Leaf Plot')
    ax.set_ylabel('Stem')
    ax.set_xlabel('Leaf')

    # Retornando a figura para que possa ser exibida no Streamlit ou em qualquer outra plataforma
    return fig, ax

import pandas as pd

