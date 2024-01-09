import streamlit as st
import pandas as pd
from data_loader import DataLoader

from modulos.e1_preparacao_dados_b.conteudo_e1_preparacao_dados_b import (
    analysis_id,
    nome_analise,
    grandeza_def,
)

def mostrar_tabela_linhas():
    linhas_info = {
        'Descrição': ['Linhas Iniciais', 'Linhas Após Filtragem', 'Linhas Removidas'],
        'Quantidade': [
            st.session_state.get(f'qtd_linhas_iniciais_{grandeza_def}', 'N/A'),
            st.session_state.get(f'qtd_linhas_finais_{grandeza_def}', 'N/A'),
            st.session_state.get(f'qtd_linhas_removidas_{grandeza_def}', 'N/A')
        ]
    }
    df_linhas = pd.DataFrame(linhas_info)
    st.table(df_linhas)
    # Guardar o DataFrame de linhas no estado da sessão para a grandeza A
    st.session_state[f'data_resumo_{grandeza_def}'] = df_linhas

def processar_e1_preparacao_dados_b():
    debug = True  # Defina como False para desativar os logs de depuração

    data_loader = DataLoader()
    st.write(nome_analise)


    data_loader.carregar_dados()
    # Carregar mapeamento de grandezas
    grandezas_dict = data_loader.carregar_grandezas()
    grandezas_nomes = list(grandezas_dict.keys())

    # Escolha da grandeza
    selectbox_key = f"select_grandeza_{grandeza_def}"
    grandeza_selecionada_nome = st.selectbox("Selecione uma Grandeza", [''] + grandezas_nomes, key=selectbox_key)

    if grandeza_selecionada_nome:
        grandeza_selecionada_codigo = grandezas_dict[grandeza_selecionada_nome]

        # Exibir opções de filtro relevantes para a grandeza selecionada
        data_loader.mostrar_opcoes_filtro(grandeza_selecionada_codigo, grandeza_def)	

        # Aplicar filtro e carregar dados
        button_key = f"btn_aplicar_filtro_{grandeza_def}"
        if st.button('Aplicar Filtro', key=button_key):
            # Atualizar as variáveis de filtro
            data_loader.atualizar_filtros(grandeza_def)
            dados_filtrados = data_loader.gerar_grandeza(grandeza_selecionada_codigo)
            st.write(dados_filtrados)

            mostrar_tabela_linhas()

            # Guardar o DataFrame da grandeza no estado da sessão para a grandeza
            st.session_state[f'data_{grandeza_def}'] = dados_filtrados

    data_loader.debug_log_estado()