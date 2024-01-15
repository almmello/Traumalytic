import os
import pandas as pd
import streamlit as st
import io
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import configs
import logging

# Obter um logger para o módulo atual
logger = logging.getLogger(__name__)

def limpar_e_carregar_csv(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            conteudo = file.read().replace('\x00', '')
        logger.debug("Conteúdo do CSV após limpeza: %s", conteudo[:500])  # Mostra os primeiros 500 caracteres
        return pd.read_csv(io.StringIO(conteudo), delimiter=';', quotechar='"')
    except Exception as e:
        logging.exception("Erro ao ler e limpar CSV")
        raise e


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


    def reset_state(self):
        logger.debug("Efetuando reset do estado da sessão")
        state_vars_to_reset = [
            'min_age_selecionada',
            'max_age_selecionada',
            'sexo_selecionado',
            'instrucao_selecionada',
            'cod_a',
            'data_a',
            'data_resumo_a',
            'qtd_linhas_finais_a',
            'qtd_linhas_iniciais_a',
            'qtd_linhas_removidas_a',
            'cod_b',
            'data_b',
            'data_resumo_b',
            'qtd_linhas_finais_b',
            'qtd_linhas_iniciais_b',
            'qtd_linhas_removidas_b',            
        ]
        for var in state_vars_to_reset:
            st.session_state[var] = configs.initial_state.get(var, None)

            
    def debug_log_estado(self):
        # Verificar se o estado da sessão contém alguma variável
        if st.session_state:
            logger.debug("Variáveis de Estado Atuais")

            # Criar uma lista para armazenar os dados das variáveis de estado
            dados_estado = []

            # Iterar sobre cada variável de estado e adicionar à lista
            for chave, valor in st.session_state.items():
                dados_estado.append({"Variável": chave, "Valor": valor})

            # Converter a lista em um DataFrame
            estado_df = pd.DataFrame(dados_estado)

            # Ordenar o DataFrame pela coluna 'Variável' em ordem alfabética
            estado_df.sort_values(by='Variável', inplace=True)

            # Imprimir o DataFrame no log de depuração
            logger.debug(f"DataFrame de estado: \n{estado_df}")
        else:
            logger.debug("Não há variáveis de estado definidas atualmente.")


    def load_data(self):
        try:
            with open(self.nome_arquivo_criptografado, 'rb') as arquivo_criptografado:
                dados_criptografados = arquivo_criptografado.read()
                dados_descriptografados = self.fernet.decrypt(dados_criptografados)
            return pd.read_excel(io.BytesIO(dados_descriptografados))
        except Exception as e:
            st.error(f"Erro ao load_data: {e}")
            return pd.DataFrame()

    def carregar_dados(self):
        try:
            logger.debug("Iniciando carregar_dados")
            self.load_filter_vars_from_state()
            logger.debug("Variáveis de filtro carregadas")

            dados = self.load_data()
            logger.debug("Dados carregados: %s", dados.head())

            self.dados_originais = dados  # Salvar os dados originais para referência

        except Exception as e:
            logging.error("Erro ao carregar dados: %s", e)
            st.error(f"Erro ao carregar dados: {e}")
            return pd.DataFrame()



    def gerar_conjunto(self, conjunto_codigo):
        try:
            logger.debug(f"Iniciando a função gerar_conjunto para o código: {conjunto_codigo}")

            # Carregar o mapeamento de conjuntos
            data_map = limpar_e_carregar_csv('data_map.csv')
            logger.debug("Mapeamento de conjuntos carregado com sucesso")

            # Verificar se o conjunto está no mapeamento
            if conjunto_codigo not in data_map['Código'].values:
                raise ValueError(f"Conjunto '{conjunto_codigo}' não encontrada no mapeamento")

            # Obter o output para o conjunto
            output = data_map[data_map['Código'] == conjunto_codigo].iloc[0]
            logger.debug(f"Output encontrado para {conjunto_codigo}: {output}")

            # Processar o output do conjunto
            output_df = self.processar_output_conjunto(output, data_map)

            logger.debug("Conjunto gerada com sucesso: %s", output_df.head())
            return output_df

        except Exception as e:
            logging.exception("Erro ao gerar conjunto: %s", e)
            raise e

    def processar_output_conjunto(self, output, data_map):
        try:
            output_cols = eval(output['Output'])
            output_df = pd.DataFrame()

            for col in output_cols:
                logger.debug(f"Processando coluna: {col}")
                logger.debug(f"Colunas nos dados filtrados: {self.dados_filtrados.columns.tolist()}")

                if col in self.dados_filtrados.columns:
                    logger.debug(f"Coluna {col} encontrada nos dados filtrados")
                    output_df[col] = self.dados_filtrados[col]
                else:

                    logger.debug(f"Coluna {col} não encontrada nos dados filtrados, buscando receita de cálculo")
                    linha_calculo = data_map[data_map['Código'] == col.lower()].iloc[0]
                    logger.debug(f"DataFrame após filtrar data_map: {linha_calculo}")


                    colunas_calculo = eval(linha_calculo['Cálculo'])
                    logger.debug(f"Colunas para cálculo: {colunas_calculo}")

                    for calc_col in colunas_calculo:
                        if calc_col not in self.dados_filtrados.columns:
                            raise ValueError(f"Coluna '{calc_col}' necessária para o cálculo de '{col}' não encontrada")

                    logger.debug("Conjunto gerada com sucesso: %s", output_df.head())


                    output_df[col] = self.dados_filtrados[colunas_calculo].sum(axis=1)

            return output_df

        except SyntaxError as e:
            logging.error(f"Erro ao avaliar string de output: {e}")
            raise
        except Exception as e:
            logging.error(f"Erro ao processar receita do conjunto: {e}")
            raise

    def carregar_conjuntos(self):
        # Substitua este caminho pelo caminho correto do seu arquivo CSV
        data_map = pd.read_csv('data_map.csv', delimiter=';')
        return dict(zip(data_map['Nome'], data_map['Código']))

    def mostrar_opcoes_filtro(self, conjunto_codigo, conjunto_def):
        # Gerar chaves únicas para widgets
        slider_key = f"slider_idade_{conjunto_codigo}_{conjunto_def}"
        multiselect_sexo_key = f"multiselect_sexo_{conjunto_codigo}_{conjunto_def}"
        multiselect_instrucao_key = f"multiselect_instrucao_{conjunto_codigo}_{conjunto_def}"

        # Contar o número de linhas antes da aplicação dos filtros
        self.qtd_dados_iniciais = self.dados_originais.shape[0]
        chave_qtd_linhas = f'qtd_linhas_iniciais_{conjunto_def}'
        st.session_state[chave_qtd_linhas] = self.qtd_dados_iniciais

        # Carregar o mapeamento de conjuntos para obter o output
        data_map = pd.read_csv('data_map.csv', delimiter=';')
        output_cols = eval(data_map[data_map['Código'] == conjunto_codigo]['Output'].iloc[0])

        # Inicializar lista de colunas de origem
        colunas_origem = []

        # Identificar as colunas de origem
        for col in output_cols:
            if col in self.dados_originais.columns:
                colunas_origem.append(col)
            else:
                # Para colunas calculadas, buscar a receita de cálculo e adicionar as colunas de origem
                receita_calculo = data_map[data_map['Código'] == col.lower()].iloc[0]
                colunas_calculo = eval(receita_calculo['Cálculo'])
                colunas_origem.extend(colunas_calculo)

        # Remover duplicatas na lista de colunas de origem
        colunas_origem = list(set(colunas_origem))

        # Filtra os dados para remover nulos nas colunas relevantes
        self.dados_filtrados = self.dados_originais.dropna(subset=colunas_origem)

        # Opçãos de filtro
        minimo_encontrado = self.dados_filtrados['IDADE'].min()
        maximo_encontrado = self.dados_filtrados['IDADE'].max()

        opcoes_unicas_sexo = ['Nulos'] + self.dados_filtrados['SEXO'].dropna().unique().tolist()
        opcoes_unicas_instrucao = ['Nulos'] + self.dados_filtrados['INSTRUCAO'].dropna().unique().tolist()

        if conjunto_def == 'a':

            # Opção de filtro por idade
            min_age, max_age = st.slider("Selecione a faixa etária:", 
                                        float(minimo_encontrado), 
                                        float(maximo_encontrado), 
                                        (float(st.session_state['min_age']), float(st.session_state['max_age'])), 
                                        1.0, key=slider_key)
            st.session_state['min_age_selecionada'] = min_age
            st.session_state['max_age_selecionada'] = max_age

            # Opção de filtro por sexo com multiselect
            sexo_selecionado = st.multiselect("Selecione as opções de sexo", 
                                            opcoes_unicas_sexo, 
                                            default=opcoes_unicas_sexo, 
                                            key=multiselect_sexo_key)
            st.session_state['sexo_selecionado'] = sexo_selecionado

            # Filtro de instrução com multiselect
            instrucao_selecionada = st.multiselect("Selecione os níveis de instrução", 
                                                opcoes_unicas_instrucao, 
                                                default=opcoes_unicas_instrucao, 
                                                key=multiselect_instrucao_key)
            st.session_state['instrucao_selecionada'] = instrucao_selecionada

        elif conjunto_def == 'b':
            # Comportamento para o conjunto_def 'b': apenas exibir os valores dos filtros definidos para 'a'

            st.markdown("### Filtros aplicados:")
            st.markdown(f"- Faixa etária: {st.session_state['min_age']} até {st.session_state['max_age']}")
            st.markdown(f"- Sexo: {', '.join(st.session_state['sexo_selecionado'])}")
            st.markdown(f"- Nível de instrução: {', '.join(st.session_state['instrucao_selecionada'])}")

    
    def atualizar_filtros(self, conjunto_def):
        
        # Aplicar filtro de idade
        if 'min_age' in st.session_state and 'max_age' in st.session_state:
            self.dados_filtrados = self.dados_filtrados[
                (self.dados_filtrados['IDADE'] >= st.session_state['min_age_selecionada']) &
                (self.dados_filtrados['IDADE'] <= st.session_state['max_age_selecionada'])
            ]

        # Aplicar filtro de sexo
        if 'sexo_selecionado' in st.session_state:
            opcoes_sexo = st.session_state['sexo_selecionado']
            if 'Nulos' in opcoes_sexo:
                self.dados_filtrados = self.dados_filtrados[
                    self.dados_filtrados['SEXO'].fillna('Nulos').isin(opcoes_sexo)
                ]
            elif opcoes_sexo:
                self.dados_filtrados = self.dados_filtrados[
                    self.dados_filtrados['SEXO'].isin(opcoes_sexo)
                ]

        # Aplicar filtro de instrução
        if 'instrucao_selecionada' in st.session_state:
            opcoes_instrucao = st.session_state['instrucao_selecionada']
            if 'Nulos' in opcoes_instrucao:
                self.dados_filtrados = self.dados_filtrados[
                    self.dados_filtrados['INSTRUCAO'].fillna('Nulos').isin(opcoes_instrucao)
                ]
            elif opcoes_instrucao:
                self.dados_filtrados = self.dados_filtrados[
                    self.dados_filtrados['INSTRUCAO'].isin(opcoes_instrucao)
                ]

        # Contar o número de linhas após a aplicação dos filtros
        qtd_dados_finais = self.dados_filtrados.shape[0]
        qtd_dados_removidos = self.qtd_dados_iniciais - qtd_dados_finais

        # Atualizar o estado da sessão com as contagens, diferenciando entre os conjuntos 'a' e 'b'
        chave_qtd_linhas_finais = f'qtd_linhas_finais_{conjunto_def}'
        chave_qtd_linhas_removidas = f'qtd_linhas_removidas_{conjunto_def}'

        st.session_state[chave_qtd_linhas_finais] = qtd_dados_finais
        st.session_state[chave_qtd_linhas_removidas] = qtd_dados_removidos




