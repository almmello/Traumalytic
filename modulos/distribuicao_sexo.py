import streamlit as st

from calculations import calcular_distribuicao_por_sexo

# Importar a classe DataLoader do diretório pai
import sys
sys.path.append('..')  # Adiciona o diretório pai ao sys.path
from data_loader import DataLoader

def mostrar_distribuicao_sexo():
    st.title("Distribuição Porcentual por Sexo")

    # Inicializar o DataLoader
    data_loader = DataLoader()

    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = data_loader.carregar_dados()

    # Botão para calcular a distribuição por sexo
    if st.button('Calcular Distribuição por Sexo'):
        distribuicao_sexo = calcular_distribuicao_por_sexo(st.session_state['data'])
        st.write('Distribuição Porcentual por Sexo:', distribuicao_sexo)

# Chamada da função principal
if __name__ == "__main__":
    mostrar_distribuicao_sexo()
