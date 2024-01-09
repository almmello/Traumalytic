import streamlit as st
import pandas as pd
from data_loader import DataLoader

def processar_app_config():
    data_loader = DataLoader()
    # Verificar se o estado da sessão contém alguma variável
    if st.session_state:
        st.subheader("Variáveis de Estado Atuais")

        # Criar uma lista para armazenar os dados das variáveis de estado
        dados_estado = []

        # Iterar sobre cada variável de estado e adicionar à lista
        for chave, valor in st.session_state.items():
            dados_estado.append({"Variável": chave, "Valor": valor})

        # Converter a lista em um DataFrame
        estado_df = pd.DataFrame(dados_estado)

        # Ordenar o DataFrame pela coluna 'Variável' em ordem alfabética
        estado_df = estado_df.sort_values(by='Variável')

        # Exibir o DataFrame no Streamlit
        st.dataframe(estado_df)

        # Botão para resetar as variáveis de estado
    if st.button("Resetar Variáveis de Estado", key="btn_reset_estado"):
        data_loader.reset_state()
        st.rerun()

    else:
        st.write("Não há variáveis de estado definidas atualmente.")
