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

            # Filtro para PTCI
            if st.session_state.get('remover_nulos_pcti', False):
                PTCI_COLS = ['PTCI01', 'PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI07', 'PTCI08', 'PTCI09', 'PTCI10', 
                             'PTCI11', 'PTCI12', 'PTCI13', 'PTCI14', 'PTCI15', 'PTCI16', 'PTCI17', 'PTCI18', 'PTCI19', 'PTCI20', 
                             'PTCI21', 'PTCI22', 'PTCI23', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI27', 'PTCI28', 'PTCI29', 'PTCI30', 
                             'PTCI31', 'PTCI32', 'PTCI33', 'PTCI34', 'PTCI35', 'PTCI36']
                dados = dados.dropna(subset=PTCI_COLS, how='any')

            # Filtro para PCL-5
            if st.session_state.get('remover_nulos_pcl5', False):
                PCL5_COLS = ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 
                             'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
                dados = dados.dropna(subset=PCL5_COLS, how='any')

            if dados.empty:
                return pd.DataFrame(columns=dados.columns)

            return dados

        except Exception as e:
            st.error(f"Erro ao carregar dados: {e}")
            return pd.DataFrame()