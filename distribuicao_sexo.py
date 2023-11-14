import streamlit as st
import pandas as pd
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
from calculations import calcular_distribuicao_por_sexo

def carregar_dados():
    # Carregar as variáveis de ambiente
    load_dotenv()

    # Pegar a chave de criptografia do arquivo .env
    chave_criptografia = os.getenv('FILE_ENCRYPTION_KEY')
    fernet = Fernet(chave_criptografia.encode())

    # Caminho do arquivo criptografado
    nome_arquivo_criptografado = 'Banco LEC PCL5 PTCI.xlsx.crp'

    # Descriptografar o arquivo
    with open(nome_arquivo_criptografado, 'rb') as arquivo_criptografado:
        dados_criptografados = arquivo_criptografado.read()
        dados_descriptografados = fernet.decrypt(dados_criptografados)

    # Carregar os dados descriptografados em um DataFrame do pandas
    data = pd.read_excel(pd.io.common.BytesIO(dados_descriptografados))
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
