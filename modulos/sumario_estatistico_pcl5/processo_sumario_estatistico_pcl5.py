import streamlit as st
import os
from data_loader import DataLoader

from modulos.sumario_estatistico_pcl5.calculo_sumario_estatistico_pcl5 import (
    gerar_sumario_validade_pcl5,
    gerar_descritivos_estatisticos_pcl5,
)

from modulos.sumario_estatistico_pcl5.conteudo_sumario_estatistico_pcl5 import (
    explicar_descritivos_estatisticos_pcl5
)



from openai_processes import (
    carregar_conclusoes,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_sumario_estatistico_pcl5():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'sumario_estatistico_pcl5'
    nome_analise = 'Sumário Estatístico do PCL-5'
    instrucoes = "Analisando os resultados do Sumário Estatístico do PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    # Gerar as tabelas separadas
    sumario_validade = gerar_sumario_validade_pcl5()
    descritivos_estatisticos_pcl5 = gerar_descritivos_estatisticos_pcl5(st.session_state['data'])

    # Exibir as tabelas na tela
    st.write('Validade dos Casos para PCL-5:', sumario_validade)
    explicar_descritivos_estatisticos_pcl5()
    st.write('Descrição Estatística do PCL-5 Total:', descritivos_estatisticos_pcl5)

    # Concatenar as tabelas em formato de string para a geração da conclusão
    resultados_para_conclusao = f"{sumario_validade.to_string(index=False)}\n\n{descritivos_estatisticos_pcl5.to_string(index=False)}"
    
    # Gerar conclusões baseadas nos resultados concatenados
    carregar_conclusoes(analysis_id, nome_analise, resultados_para_conclusao, instrucoes)
