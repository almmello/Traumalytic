import streamlit as st
import pandas as pd
from data_loader import DataLoader

from modulos.e1_preparacao_dados_a.conteudo_e1_preparacao_dados_a import (
    analysis_id,
    nome_analise,
    conjunto_def,
)

def mostrar_tabela_linhas():
    linhas_info = {
        'Descrição': ['Linhas Iniciais', 'Linhas Após Filtragem', 'Linhas Removidas'],
        'Quantidade': [
            st.session_state.get(f'qtd_linhas_iniciais_{conjunto_def}', 'N/A'),
            st.session_state.get(f'qtd_linhas_finais_{conjunto_def}', 'N/A'),
            st.session_state.get(f'qtd_linhas_removidas_{conjunto_def}', 'N/A')
        ]
    }
    df_linhas = pd.DataFrame(linhas_info)
    st.table(df_linhas)
    # Guardar o DataFrame de linhas no estado da sessão para o conjunto A
    st.session_state[f'data_resumo_{conjunto_def}'] = df_linhas

def processar_e1_preparacao_dados_a():
    debug = True  # Defina como False para desativar os logs de depuração

    data_loader = DataLoader()
    st.write(nome_analise)


    data_loader.carregar_dados()
    # Carregar mapeamento de conjuntos
    conjuntos_dict = data_loader.carregar_conjuntos()
    conjuntos_nomes = list(conjuntos_dict.keys())

    # Escolha do conjunto
    selectbox_key = f"select_conjunto_{analysis_id}_{conjunto_def}"
    conjunto_selecionada_nome = st.selectbox("Selecione um Conjunto", [''] + conjuntos_nomes, key=selectbox_key)

    if conjunto_selecionada_nome:
        conjunto_selecionada_codigo = conjuntos_dict[conjunto_selecionada_nome]

        # Exibir opções de filtro relevantes para o conjunto selecionada
        data_loader.mostrar_opcoes_filtro(conjunto_selecionada_codigo, conjunto_def)	

        # Aplicar filtro e carregar dados
        button_key = f"btn_aplicar_filtro_{analysis_id}_{conjunto_def}"
        if st.button('Aplicar Filtro', key=button_key):
            # Atualizar as variáveis de filtro
            data_loader.atualizar_filtros(conjunto_def)
            dados_filtrados = data_loader.gerar_conjunto(conjunto_selecionada_codigo)
            st.write(dados_filtrados)

            mostrar_tabela_linhas()

            # Guardar o DataFrame do conjunto no estado da sessão
            st.session_state[f'data_{conjunto_def}'] = dados_filtrados

            # Guardar o Código do conjunto no estado da sessão
            st.session_state[f'cod_{conjunto_def}'] = conjunto_selecionada_codigo

    data_loader.debug_log_estado()
            