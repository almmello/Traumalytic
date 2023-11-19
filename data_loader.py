import streamlit as st
import os
import pandas as pd
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import io

class DataLoader:
    def __init__(self):
        load_dotenv()

        # Pegar a chave de criptografia do arquivo .env
        self.chave_criptografia = os.getenv('FILE_ENCRYPTION_KEY')
        self.fernet = Fernet(self.chave_criptografia.encode())

        # Caminho do arquivo criptografado
        self.nome_arquivo_criptografado = 'Banco LEC PCL5 PTCI.xlsx.crp'

   
    def carregar_dados(self):
        try:
            # Descriptografar o arquivo e carregar em um DataFrame
            with open(self.nome_arquivo_criptografado, 'rb') as arquivo_criptografado:
                dados_criptografados = arquivo_criptografado.read()
                dados_descriptografados = self.fernet.decrypt(dados_criptografados)
            dados = pd.read_excel(io.BytesIO(dados_descriptografados))

            # Remover linhas com 'IDADE' nula ou não numérica
            dados = dados[pd.to_numeric(dados['IDADE'], errors='coerce').notna()]

            # Aplicar filtro de idade, se definido
            min_age = st.session_state.get('min_age', None)
            max_age = st.session_state.get('max_age', None)
            if min_age is not None and max_age is not None:
                dados = dados[(dados['IDADE'] >= min_age) & (dados['IDADE'] <= max_age)]

            # Verificar se o DataFrame está vazio após a filtragem
            if dados.empty:
                return pd.DataFrame(columns=dados.columns)  # Retorna um DataFrame vazio com as mesmas colunas

            return dados

        except Exception as e:
            st.error(f"Erro ao carregar dados: {e}")
            return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro