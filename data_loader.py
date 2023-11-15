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
        # Descriptografar o arquivo
        with open(self.nome_arquivo_criptografado, 'rb') as arquivo_criptografado:
            dados_criptografados = arquivo_criptografado.read()
            dados_descriptografados = self.fernet.decrypt(dados_criptografados)

        # Carregar os dados descriptografados em um DataFrame do pandas
        return pd.read_excel(io.BytesIO(dados_descriptografados))
