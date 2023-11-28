import streamlit as st
import pandas as pd
import os
from data_loader import DataLoader
from .calculo_analise_descritiva import (
    calcular_clusters_ptci, 
    calcular_clusters_pcl5, 
    calcular_estatisticas, 
    calcular_escores_pcl5, 
    calcular_escores_ptci,
    calcular_estatisticas_clusters_pcl5,
    calcular_estatisticas_clusters_ptci,
    calcular_medidas_tendencia_central,
    calcular_medidas_dispersao,
    calcular_frequencia_categoricas,
)

from .conclusao_analise_descritiva import gerar_conclusao_estatisticas_idade

# Função para carregar os dados uma única vez
def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_exibir_clusters_ptci():
    carregar_dados()
    st.session_state['ptci_clusters'] = calcular_clusters_ptci(st.session_state['data'])
    st.write(st.session_state['ptci_clusters'])

def processar_exibir_clusters_pcl5():
    carregar_dados()
    st.session_state['pcl5_clusters'] = calcular_clusters_pcl5(st.session_state['data'])
    st.write(st.session_state['pcl5_clusters'])

def processar_estatisticas_idade():
    carregar_dados()
    estatisticas_idade = calcular_estatisticas(st.session_state['data'], 'IDADE')
    st.write('Estatísticas de Idade:', estatisticas_idade)

def processar_estatisticas_idade():
    carregar_dados()
    estatisticas_idade = calcular_estatisticas(st.session_state['data'], 'IDADE')
    st.write('Estatísticas de Idade:', estatisticas_idade)

    conclusao = gerar_conclusao_estatisticas_idade(estatisticas_idade)
    st.subheader('Conclusão da Análise Descritiva:')
    st.markdown(conclusao)

    # Adicionar caixa de texto para comentários
    st.write("Faça comentários sobre a conclusão de forma que possa ser atualizada:")
    comentario = st.text_area("Comentários")

    # Botão para enviar comentários e atualizar a conclusão
    if st.button('Enviar Comentário'):
        nova_conclusao = processar_comentario_e_atualizar_conclusao(comentario)
        if nova_conclusao:
            st.subheader('Conclusão Atualizada:')
            st.markdown(nova_conclusao)

    # Botão para apagar o arquivo de conclusão
    if st.button('Apagar Conclusão'):
        os.remove('modulos/analise_descritiva/conclusoes_analise_descritiva/conclusao_estatistica_idade.txt')
        st.write('Conclusão apagada com sucesso.')


def processar_estatisticas_escore_total_pcl5():
    carregar_dados()
    estatisticas_pcl5_total = calcular_escores_pcl5(st.session_state['data'])
    st.write('Estatísticas do Escore Total PCL-5:', estatisticas_pcl5_total)

def processar_estatisticas_escore_total_ptci():
    carregar_dados()
    estatisticas_ptci_total = calcular_escores_ptci(st.session_state['data'])
    st.write('Estatísticas do Escore Total PTCI:', estatisticas_ptci_total)

def processar_estatisticas_clusters_pcl5():
    carregar_dados()
    estatisticas_clusters_pcl5 = calcular_estatisticas_clusters_pcl5(st.session_state['data'])
    st.write('Estatísticas dos Clusters PCL-5:', estatisticas_clusters_pcl5)

def processar_estatisticas_clusters_ptci():
    carregar_dados()
    estatisticas_clusters_ptci = calcular_estatisticas_clusters_ptci(st.session_state['data'])
    st.write('Estatísticas dos Clusters PTCI:', estatisticas_clusters_ptci)

def formatar_resultados(resultados):
    return pd.DataFrame(resultados, index=[0]).T.rename(columns={0: 'Valor'})

def processar_medidas_tendencia_central():
    carregar_dados()
    colunas_numericas = st.session_state['data'].select_dtypes(include='number').columns
    for coluna in colunas_numericas:
        resultados = calcular_medidas_tendencia_central(st.session_state['data'], coluna)
        st.subheader(f"Medidas de Tendência Central - {coluna}")
        st.table(formatar_resultados(resultados))

def processar_medidas_dispersao():
    carregar_dados()
    colunas_numericas = st.session_state['data'].select_dtypes(include='number').columns
    for coluna in colunas_numericas:
        resultados = calcular_medidas_dispersao(st.session_state['data'], coluna)
        st.subheader(f"Medidas de Dispersão - {coluna}")
        st.table(formatar_resultados(resultados))

def processar_frequencia_categoricas():
    carregar_dados()
    colunas_categoricas = st.session_state['data'].select_dtypes(include='object').columns
    for coluna in colunas_categoricas:
        resultados = calcular_frequencia_categoricas(st.session_state['data'], coluna)
        st.subheader(f"Frequência de Variáveis Categóricas - {coluna}")
        st.table(resultados)
