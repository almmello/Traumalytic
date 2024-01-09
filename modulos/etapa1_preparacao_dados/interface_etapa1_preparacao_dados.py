import streamlit as st
import pandas as pd
from data_loader import DataLoader

from modulos.etapa1_preparacao_dados.processo_etapa1_preparacao_dados import (
    mostrar_tabela_linhas,
)

def mostrar_etapa1_preparacao_dados():
    
    # Verificar se é necessário resetar o estado
    if st.session_state.get('reset_state', False):
        data_loader = DataLoader()
        data_loader.reset_state()
        st.session_state['reset_state'] = False

    data_loader = DataLoader()
    st.title("Preparação dos Dados")


    data_loader.carregar_dados()
    # Carregar mapeamento de conjuntos
    conjuntos_dict = data_loader.carregar_conjuntos()
    conjuntos_nomes = list(conjuntos_dict.keys())

    # Escolha do conjunto
    conjunto_selecionada_nome = st.selectbox("Selecione um Conjunto", [''] + conjuntos_nomes)

    if conjunto_selecionada_nome:
        conjunto_selecionada_codigo = conjuntos_dict[conjunto_selecionada_nome]

        # Exibir opções de filtro relevantes para o conjunto selecionada
        data_loader.mostrar_opcoes_filtro(conjunto_selecionada_codigo)

        # Aplicar filtro e carregar dados
        if st.button('Aplicar Filtro'):
            # Atualizar as variáveis de filtro
            data_loader.atualizar_filtros()
            dados_filtrados = data_loader.gerar_conjunto(conjunto_selecionada_codigo)
            st.write(dados_filtrados)

            mostrar_tabela_linhas()

        # Botão para resetar a sessão
            
    if st.button('Resetar'):
        st.session_state['reset_state'] = True
        st.rerun()


if __name__ == "__main__":
    mostrar_etapa1_preparacao_dados()

