import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os
from data_loader import DataLoader
from fig_management import FigManagement
from openai_parser import OpenAIInterface

from modulos.normalidade_escore_total_pcl5.calculo_normalidade_escore_total_pcl5 import (
    #calcular_normalidade_escore_total_pcl5,
    testar_normalidade_pcl5,
    formatar_p_valor,
    criar_histograma,
    criar_grafico_qq,
    gerar_dados_normal,
    calcular_p_valor_normal,
    interpretar_resultados_a,
    interpretar_resultados_b,

)

from openai_interface import (
    carregar_conclusoes,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_normalidade_escore_total_pcl5():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'normalidade_escore_total_pcl5'
    nome_analise = 'Análise Normalidade do escore total do PCL-5'
    instrucoes = "Analisando os resultados da Análise Normalidade do escore total do PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    selected_var = "PCL5_total"

    # Realizar o teste de Shapiro-Wilk e obter os gráficos para os dados do usuário
    resultados_normalidade, data_escores_temp = testar_normalidade_pcl5(st.session_state['data'])
    st.session_state['data_escores'] = data_escores_temp
    p_valor = resultados_normalidade.get(selected_var, 'Variável não encontrada')
    st.write(f'Resultados do Teste de Normalidade para {selected_var} (p-valor): {formatar_p_valor(p_valor)}')

    # Gerar e mostrar os gráficos para os dados do usuário
    descricao_x_hist = f'Valores de {selected_var}'
    descricao_y_hist = 'Frequência'
    fig_hist = criar_histograma(st.session_state['data_escores'], selected_var, descricao_x_hist, descricao_y_hist)
    st.pyplot(fig_hist)
    plt.close(fig_hist)

    descricao_x_qq = 'Quantis Teóricos da Distribuição Normal'
    descricao_y_qq = f'Quantis Reais de {selected_var}'
    fig_qq = criar_grafico_qq(st.session_state['data_escores'], selected_var, descricao_x_qq, descricao_y_qq)
    st.pyplot(fig_qq)
    plt.close(fig_qq)

    # Exibir a parte A da interpretacao da análise
    interpretacao_a = interpretar_resultados_a(p_valor)
    st.write(interpretacao_a)

    # Gerar dados de exemplo para uma distribuição normal
    dados_exemplo_normal = gerar_dados_normal()

    # Calcular o p-valor para os dados de exemplo
    p_valor_exemplo = calcular_p_valor_normal(dados_exemplo_normal)
    st.write(f"P-valor para os dados de exemplo de distribuição normal: {formatar_p_valor(p_valor_exemplo)}")

    # Gerar e mostrar os gráficos de exemplo
    fig_hist_exemplo = criar_histograma(pd.DataFrame(dados_exemplo_normal, columns=['Normal']), 'Normal')
    st.pyplot(fig_hist_exemplo)
    plt.close(fig_hist_exemplo)

    # Exibir a parte B da Interpretação da análise
    interpretacao_b = interpretar_resultados_b(p_valor)
    st.write(interpretacao_b)
    st.write(f"Explicação do Gráfico Q-Q: O eixo X ({descricao_x_qq}) mostra os quantis teóricos, e o eixo Y ({descricao_y_qq}) os quantis reais dos dados.")

    fig_qq_exemplo = criar_grafico_qq(pd.DataFrame(dados_exemplo_normal, columns=['Normal']), 'Normal')
    st.pyplot(fig_qq_exemplo)
    plt.close(fig_qq_exemplo)# Fechar a figura

    fig_manager = FigManagement()
    openai_interface = OpenAIInterface()

    # Salvar e converter gráficos em base64
    caminho_histograma = fig_manager.salvar_grafico(fig_hist)
    imagem_base64_histograma = openai_interface.encode_image_to_base64(caminho_histograma)
    descricao_hist = openai_interface.descrever_imagem_base64(imagem_base64_histograma)
    if debug:
        print("Descrição Histograma:", descricao_hist)
    fig_manager.apagar_grafico(caminho_histograma)

    caminho_grafico_qq = fig_manager.salvar_grafico(fig_qq)
    imagem_base64_grafico_qq = openai_interface.encode_image_to_base64(caminho_grafico_qq)
    descricao_qq = openai_interface.descrever_imagem_base64(imagem_base64_grafico_qq)
    if debug:
        print("Descrição Gráfico Q-Q:", descricao_qq)
    fig_manager.apagar_grafico(caminho_grafico_qq)

    # Preparar o texto para geração de conclusões
    resultados_texto = f"Resultados do Teste de Normalidade para {selected_var} (p-valor): {formatar_p_valor(p_valor)}\n\n"
    resultados_texto += f"Descrição do Histograma: {descricao_hist}\n\n"
    resultados_texto += f"Descrição do Gráfico Q-Q: {descricao_qq}"

    if debug:
        print("Texto para Geração de Conclusões:", resultados_texto)

    # Gerar conclusões com base nos resultados e descrições
    carregar_conclusoes(analysis_id, nome_analise, resultados_texto, instrucoes)

