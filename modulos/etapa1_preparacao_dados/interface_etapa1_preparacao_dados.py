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
    # Carregar mapeamento de grandezas
    grandezas_dict = data_loader.carregar_grandezas()
    grandezas_nomes = list(grandezas_dict.keys())

    # Escolha da grandeza
    grandeza_selecionada_nome = st.selectbox("Selecione uma Grandeza", [''] + grandezas_nomes)

    if grandeza_selecionada_nome:
        grandeza_selecionada_codigo = grandezas_dict[grandeza_selecionada_nome]

        # Exibir opções de filtro relevantes para a grandeza selecionada
        data_loader.mostrar_opcoes_filtro(grandeza_selecionada_codigo)

        # Aplicar filtro e carregar dados
        if st.button('Aplicar Filtro'):
            # Atualizar as variáveis de filtro
            data_loader.atualizar_filtros()
            dados_filtrados = data_loader.gerar_grandeza(grandeza_selecionada_codigo)
            st.write(dados_filtrados)

            mostrar_tabela_linhas()

        # Botão para resetar a sessão
            
    if st.button('Resetar'):
        st.session_state['reset_state'] = True
        st.rerun()


if __name__ == "__main__":
    mostrar_etapa1_preparacao_dados()

