import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import stemgraphic
from data_loader import DataLoader
from collections import defaultdict


def calcular_caule_folhas_ptci(data):
    break_on_5=False
    DataLoader.calculos_ptci(data)  # A função de preparação dos dados.
    
    # Filtrando os dados para remover valores menores ou iguais a 3
    escores_limpos = data['PTCI_Total'].dropna().astype(int)
    escores_filtrados = escores_limpos[escores_limpos > 3]

    # Create a default dictionary to hold the leaves for each stem
    stem_dict = defaultdict(list)

    # Sort the data to make processing easier
    sorted_data = sorted(escores_filtrados)

    # Fill the default dictionary with leaves
    for number in sorted_data:
        stem, leaf = divmod(number, 10)
        stem_dict[stem].append(leaf)

    # Prepare the display data
    stem_list = []
    leaf_list = []
    frequency_list = []

    for stem, leaves in stem_dict.items():
        # Sort the leaves before turning them into a string
        sorted_leaves = sorted(leaves)

        if break_on_5:
            # Create breaks in the leaves at 5
            leaf_str1 = ' '.join(str(leaf) for leaf in sorted_leaves if leaf < 5)
            leaf_str2 = ' '.join(str(leaf) for leaf in sorted_leaves if leaf >= 5)
            
            # Append first half, if exists
            if leaf_str1:
                stem_list.append(stem)
                leaf_list.append(leaf_str1)
                frequency_list.append(leaf_str1.count(' ') + 1)  # Count the leaves
            
            # Append second half, if exists
            if leaf_str2:
                stem_list.append(stem)  # Same stem as it is a continuation
                leaf_list.append(leaf_str2)
                frequency_list.append(leaf_str2.count(' ') + 1)  # Count the leaves
        else:
            # No break; append all leaves as is
            leaves_str = ' '.join(str(leaf) for leaf in sorted_leaves)
            stem_list.append(stem)
            leaf_list.append(leaves_str)
            frequency_list.append(len(sorted_leaves))

    # Create a DataFrame for better visual representation
    df = pd.DataFrame({
        "Frequency": frequency_list,
        "Stem": stem_list,
        "Leaf": leaf_list
    })

    return df


