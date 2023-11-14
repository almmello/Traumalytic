from cryptography.fernet import Fernet
import os

def criptografar_arquivo(nome_arquivo):
    # Gerar uma chave de criptografia
    chave = Fernet.generate_key()
    fernet = Fernet(chave)

    # Ler o arquivo original
    with open(nome_arquivo, 'rb') as arquivo:
        dados_originais = arquivo.read()

    # Criptografar os dados do arquivo
    dados_criptografados = fernet.encrypt(dados_originais)

    # Salvar o arquivo criptografado
    nome_arquivo_criptografado = nome_arquivo + '.crp'
    with open(nome_arquivo_criptografado, 'wb') as arquivo_criptografado:
        arquivo_criptografado.write(dados_criptografados)

    return chave

# Nome do arquivo a ser criptografado
nome_arquivo = 'Banco LEC PCL5 PTCI.xlsx'

# Criptografar o arquivo
chave = criptografar_arquivo(nome_arquivo)

# Salvar a chave no arquivo .env
with open('.env', 'a') as env_file:
    env_file.write(f'\nFILE_ENCRYPTION_KEY={chave.decode()}')
