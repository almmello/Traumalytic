import streamlit as st
import pandas as pd

def mostrar_tabela_linhas():
    linhas_info = {
        'Descrição': ['Linhas Iniciais', 'Linhas Após Filtragem', 'Linhas Removidas'],
        'Quantidade': [
            st.session_state.get('qtd_linhas_iniciais', 'N/A'),
            st.session_state.get('qtd_linhas_finais', 'N/A'),
            st.session_state.get('qtd_linhas_removidas', 'N/A')
        ]
    }
    st.table(pd.DataFrame(linhas_info))