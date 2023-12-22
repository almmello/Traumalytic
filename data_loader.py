import os
import pandas as pd
import streamlit as st
import io
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import configs

class DataLoader:
    def __init__(self):
        load_dotenv()

        # Pegar a chave de criptografia do arquivo .env
        self.chave_criptografia = os.getenv('FILE_ENCRYPTION_KEY')
        self.fernet = Fernet(self.chave_criptografia.encode())

        # Caminho do arquivo criptografado
        self.nome_arquivo_criptografado = 'Banco LEC PCL5 PTCI.xlsx.crp'

    def load_state_from_config(self):
        for key, value in configs.initial_state.items():
            if key not in st.session_state:
                st.session_state[key] = value


    def load_filter_vars_from_state(self):
        self.min_age = st.session_state['min_age']
        self.max_age = st.session_state['max_age']
        self.remover_nulos_idade = st.session_state['remover_nulos_idade']
        self.remover_nulos_pcti = st.session_state['remover_nulos_pcti']
        self.remover_nulos_pcl5 = st.session_state['remover_nulos_pcl5']

    def load_data(self):
        try:
            with open(self.nome_arquivo_criptografado, 'rb') as arquivo_criptografado:
                dados_criptografados = arquivo_criptografado.read()
                dados_descriptografados = self.fernet.decrypt(dados_criptografados)
            return pd.read_excel(io.BytesIO(dados_descriptografados))
        except Exception as e:
            st.error(f"Erro ao carregar dados: {e}")
            return pd.DataFrame()

    def apply_filter(self, dados):
        dados_iniciais = dados.shape[0]

        if self.remover_nulos_idade:
            dados = dados[pd.to_numeric(dados['IDADE'], errors='coerce').notna()]

        if self.min_age is not None and self.max_age is not None:
            dados = dados[(dados['IDADE'] >= self.min_age) & (dados['IDADE'] <= self.max_age)]

        if self.remover_nulos_pcti:
            PTCI_COLS = [f'PTCI{i:02d}' for i in range(1, 37)]
            dados = dados.dropna(subset=PTCI_COLS, how='any')

        if self.remover_nulos_pcl5:
            PCL5_COLS = [f'PCL{i:02d}' for i in range(1, 21)]
            dados = dados.dropna(subset=PCL5_COLS, how='any')

        # Agora que todos os filtros foram aplicados, faça a contagem
        dados_finais = dados.shape[0]
        dados_missing = dados_iniciais - dados_finais

        # Atualiza o estado da sessão com as contagens finais
        st.session_state['valid_count'] = dados_finais
        st.session_state['missing_count'] = dados_missing



        return dados

    def carregar_dados(self):
        try:
            self.load_filter_vars_from_state()
            dados = self.load_data()
            dados_filtrados = self.apply_filter(dados)
            return dados_filtrados if not dados_filtrados.empty else pd.DataFrame(columns=dados.columns)
        except Exception as e:
            st.error(f"Erro ao carregar dados: {e}")
            return pd.DataFrame()
        

    def calculos_pcl5(data):
        # Fórmulas para os clusters do PCL-5
        clusters_pcl5 = {
            'Cluster_B': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05'],
            'Cluster_C': ['PCL06', 'PCL07'],
            'Cluster_D': ['PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14'],
            'Cluster_E': ['PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20'],
            'PCL5_Total': ['PCL01', 'PCL02', 'PCL03', 'PCL04', 'PCL05', 'PCL06', 'PCL07', 'PCL08', 'PCL09', 'PCL10', 'PCL11', 'PCL12', 'PCL13', 'PCL14', 'PCL15', 'PCL16', 'PCL17', 'PCL18', 'PCL19', 'PCL20']
        }

        for cluster, questions in clusters_pcl5.items():
            data[cluster] = data[questions].sum(axis=1)
            data[cluster + '_media'] = data[cluster] / len(questions)

        return data
    
    def calculos_ptci(data):
        # Fórmulas para os clusters do PTCI
        clusters_ptci = {
            'Cluster_A': ['PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI09', 'PTCI12', 'PTCI14', 'PTCI16', 'PTCI17', 
                        'PTCI20', 'PTCI21', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI33', 'PTCI35', 'PTCI36'],
            'Cluster_B': ['PTCI07', 'PTCI08', 'PTCI10', 'PTCI11', 'PTCI18', 'PTCI23', 'PTCI27'],
            'Cluster_C': ['PTCI01', 'PTCI15', 'PTCI19', 'PTCI22', 'PTCI31'],
            'PTCI_Total': ['PTCI01', 'PTCI02', 'PTCI03', 'PTCI04', 'PTCI05', 'PTCI06', 'PTCI07', 'PTCI08', 'PTCI09', 'PTCI10', 'PTCI11', 'PTCI12', 'PTCI14', 'PTCI15', 'PTCI16', 'PTCI17', 'PTCI18', 'PTCI19', 'PTCI20', 'PTCI21', 'PTCI22', 'PTCI23', 'PTCI24', 'PTCI25', 'PTCI26', 'PTCI27', 'PTCI28', 'PTCI29', 'PTCI30', 'PTCI31', 'PTCI33', 'PTCI35', 'PTCI36']
        }

        # Calcula a soma e média para cada cluster
        for cluster, questions in clusters_ptci.items():
            data[cluster] = data[questions].sum(axis=1)
            data[cluster + '_media'] = data[cluster] / len(questions)
        
        return data

