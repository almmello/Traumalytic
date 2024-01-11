import streamlit as st
import pandas as pd

import configs

# Importações absolutas baseadas na estrutura do projeto
from modulos.e1_conclusao.processo_e1_conclusao import (
    processar_e1_conclusao,
    explicar_e1_conclusao
)

def mostrar_e1_conclusao():
    st.title("Conclusão Etapa 1")

    # Lista de variáveis necessárias
    variaveis_necessarias = ['cod_a', 'cod_b', 'data_a', 'data_b', 'data_resumo_a', 'data_resumo_b']
    variaveis_faltantes = []

    for var in variaveis_necessarias:
        if var in st.session_state:
            # Para DataFrames, verificar se estão vazios
            if isinstance(st.session_state[var], pd.DataFrame):
                if st.session_state[var].empty:
                    variaveis_faltantes.append(var)
            # Para outras variáveis, verificar se estão no estado inicial
            elif st.session_state[var] == configs.initial_state.get(var, None):
                variaveis_faltantes.append(var)
        else:
            variaveis_faltantes.append(var)

    # Verificar se todas as variáveis necessárias estão presentes e não estão em seu estado inicial
    if variaveis_faltantes:
        # Exibir as variáveis faltantes e solicitar a execução das etapas anteriores
        st.error("As seguintes variáveis de sessão estão faltando ou estão em seu estado inicial: " + ", ".join(variaveis_faltantes))
        st.markdown("Por favor, execute as etapas anteriores para gerar essas variáveis.")
    else:
        # Se todas as variáveis estiverem presentes, prosseguir com a conclusão da Etapa 1
        explicar_e1_conclusao()
        processar_e1_conclusao()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_e1_conclusao()
