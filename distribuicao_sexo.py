import streamlit as st
import pandas as pd
from calculations import calcular_distribuicao_por_sexo

def carregar_dados():
    # Carregar dados aqui
    data = pd.read_excel('Banco LEC PCL5 PTCI.xlsx')
    return data

def mostrar_distribuicao_sexo():
    st.title("Distribuição Porcentual por Sexo")

    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = carregar_dados()

    # Botão para calcular a distribuição por sexo
    if st.button('Calcular Distribuição por Sexo'):
        distribuicao_sexo = calcular_distribuicao_por_sexo(st.session_state['data'])
        st.write('Distribuição Porcentual por Sexo:', distribuicao_sexo)

# Chamada da função principal
if __name__ == "__main__":
    mostrar_distribuicao_sexo()
