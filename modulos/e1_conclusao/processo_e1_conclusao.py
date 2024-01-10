import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_processes import (
    processar_conclusoes_texto,
    formatar_resultados_para_texto,
)

from modulos.e1_conclusao.conteudo_e1_conclusao import (
    pref_analysis_id,
    nome_analise,
    instrucoes,
    etapa_analise,
)



def processar_e1_conclusao():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")

    # Inicializar reset_counter, no estado da sessão, se não existir. 
    # O Contador serve para contar as conclusões e comentários.
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    # Cria um analysis_id com base no prefixo
    cod_a = st.session_state['cod_a']
    cod_b = st.session_state['cod_b']
    # Ordenar os códigos para garantir que a ordem não fará diferença
    cod_a_b = sorted([cod_a, cod_b])

    # Concatenar os códigos com um separador para formar o analysis_id
    # analysis_id = f"{pref_analysis_id}_{cod_a_b}"
    # Concatenar os códigos com um separador para formar o analysis_id
    analysis_id = f"{pref_analysis_id}_{'_'.join(cod_a_b)}"

    # Trasnformar as tabelas dos conjuntos de dados A e B (data_a e data_b) e também dos resumos (data_resumo_a	data_resumo_b) em um texto para o prompt
    data_a = st.session_state['data_a']
    data_b = st.session_state['data_b']
    data_resumo_a = st.session_state['data_resumo_a']
    data_resumo_b = st.session_state['data_resumo_b']
    data_a_texto = formatar_resultados_para_texto(data_a)
    data_b_texto = formatar_resultados_para_texto(data_b)
    data_resumo_a_texto = formatar_resultados_para_texto(data_resumo_a)
    data_resumo_b_texto = formatar_resultados_para_texto(data_resumo_b)

    texto_resultados = f"Conjunto A:\n{data_a_texto}\nConjunto B:\n{data_b_texto}\nContagem de linhas do Conjunto A:\n{data_resumo_a_texto}\nContagem de linhas do Conjunto B:\n{data_resumo_b_texto}"

    st.write('Conclusão Etapa 1')

    # Passando o texto concatenado para o método carregar_conclusoes
    processar_conclusoes_texto(analysis_id, etapa_analise, texto_resultados, nome_analise, instrucoes, debug)
