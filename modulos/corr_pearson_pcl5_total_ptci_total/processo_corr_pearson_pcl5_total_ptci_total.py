import streamlit as st
import matplotlib.pyplot as plt
import os
from data_loader import DataLoader
from supabase_manager import SupabaseManager

from openai_interface import (
    carregar_conclusoes,
    processar_visao_imagem
)

from modulos.corr_pearson_pcl5_total_ptci_total.calculo_corr_pearson_pcl5_total_ptci_total import (
    criar_corr_pearson_pcl5_total_ptci_total
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_corr_pearson_pcl5_total_ptci_total():
    debug = True  # Defina como False para desativar os logs de depuração
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'corr_pearson_pcl5_total_ptci_total'
    nome_analise = 'Correlação Paramétrica entre PCL5 Total e PTCI Total'
    instrucoes = "Analisando os resultados da Correlação Paramétrica entre PCL5 Total e PTCI Total, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
    prompt_plot = "Analise este gráfico de calor que ilustra a correlação paramétrica entre os escores totais do PCL-5 e do PTCI. O gráfico exibe uma matriz colorida onde cada cor e valor numérico correspondente indica o nível de correlação entre os escores totais dos dois instrumentos. Cores mais quentes representam uma correlação mais forte, e cores mais frias indicam uma correlação mais fraca ou negativa. Utilize as variações de cor e os valores numéricos para interpretar a relação entre a severidade dos sintomas de TEPT, avaliados pelo PCL-5, e as cognições pós-traumáticas, medidas pelo PTCI. Discuta o significado dessa correlação e suas possíveis implicações para entender como os sintomas de TEPT estão associados a padrões cognitivos específicos em indivíduos após experiências traumáticas, realçando a importância dessas descobertas para intervenções clínicas e direções de pesquisa futura no campo do trauma psicológico."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    st.write('Correlação Paramétrica entre PCL5 Total e PTCI Total')

    # Gerar e mostrar os gráficos para os dados do usuário
    fig = criar_corr_pearson_pcl5_total_ptci_total(st.session_state['data'])
    st.pyplot(fig)



    # Verificar se já existe uma conclusão armazenada
    supabase_manager = SupabaseManager()
    existing_conclusions = supabase_manager.recuperar_conclusoes(analysis_id)

    if not existing_conclusions:

        # Processar a visão dos gráficos caso não existam conclusões anteriores
        descricao_plot = processar_visao_imagem(fig, prompt_plot)

        # Preparar o texto para geração de conclusões
        resultados_texto = f"Descrição do {nome_analise}: {descricao_plot}"

        if debug:
            print("---\n")         
            print("Texto para Geração de Conclusões: ", resultados_texto)
            print("---\n") 

        # Gerar conclusões com base nos resultados e descrições
        carregar_conclusoes(analysis_id, nome_analise, resultados_texto, instrucoes)
    else:
        # Carregar conclusões existentes sem gerar novas descrições
        carregar_conclusoes(analysis_id, nome_analise)
