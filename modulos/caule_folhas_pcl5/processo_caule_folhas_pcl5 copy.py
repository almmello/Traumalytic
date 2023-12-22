import streamlit as st
import os
from data_loader import DataLoader

from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
)

from modulos.caule_folhas_pcl5.calculo_caule_folhas_pcl5 import (
    calcular_caule_folhas_pcl5,
    criar_tabela_caule_folhas
)


def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_caule_folhas_pcl5():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'caule_folhas_pcl5'
    nome_analise = 'Exibição de Caule-e-Folhas do PCL5'
    instrucoes = "Analisando os resultados da Exibição de Caule-e-Folhas do PCL5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    fig_hist, ax = calcular_caule_folhas_pcl5(st.session_state['data'])
    st.write('Exibição de Caule-e-Folhas do PCL5:')
    st.pyplot(fig_hist)
    #st.text(str(ax))  # Isso imprimirá a representação de string do objeto Axes
    #st.text(f"Title: {ax.title.get_text()}")
    #st.text(f"X-axis label: {ax.xaxis.label.get_text()}")
    #st.text(f"Y-axis label: {ax.yaxis.label.get_text()}")

    # Uso da função
    #resultados_tabela = criar_tabela_caule_folhas(st.session_state['data'])

    # Exibir a tabela no Streamlit
    #st.write('Tabela de Caule-e-Folhas do PCL5:')
    #st.dataframe(resultados_tabela)


    # Verificar se já existe uma conclusão armazenada
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:

        # Processar a visão dos gráficos caso não existam conclusões anteriores
        prompt_hist = "Descrição do gráfico de caule-e-folhas dos valores totais do PCL-5, representando a distribuição dos escores de trauma na amostra de dados. Explique as características da distribuição evidenciadas pelo gráfico, incluindo a frequência de ocorrência dos escores em diferentes intervalos e quaisquer padrões ou tendências observáveis na distribuição dos dados."

        descricao_hist = processar_visao_imagem(fig_hist, prompt_hist)

        # Preparar o texto para geração de conclusões
        resultados_texto = f"Descrição do Diagrama: {descricao_hist}"

        if debug:
            print("Texto para Geração de Conclusões: ", resultados_texto)

        # Gerar conclusões com base nos resultados e descrições
        carregar_conclusoes(analysis_id, nome_analise, resultados_texto, instrucoes)
    else:
        # Carregar conclusões existentes sem gerar novas descrições
        carregar_conclusoes(analysis_id, nome_analise)
