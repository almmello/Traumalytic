import streamlit as st
import os
from data_loader import DataLoader

from modulos.sumario_estatístico_pcl5_ptci.calculo_sumario_estatístico_pcl5_ptci import (
    gerar_sumario_validade,
    gerar_descritivos_estatisticos,
)

from modulos.sumario_estatístico_pcl5_ptci.conteudo_sumario_estatístico_pcl5_ptci import (
    explicar_descritivos_estatisticos_pcl5_ptci
)



from openai_interface import (
    carregar_conclusoes,
)

def carregar_dados():
    if 'data' not in st.session_state:
        data_loader = DataLoader()
        st.session_state['data'] = data_loader.carregar_dados()

def processar_sumario_estatístico_pcl5_ptci():
    APP_USER = os.getenv("ENV_USER")
    analysis_id = 'sumario_estatístico_pcl5_ptci'
    nome_analise = 'Sumário Estatístico do PCL-5 e PTCI'
    instrucoes = "Analisando os resultados do Sumário Estatístico do PCL-5 e PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."

    # Inicializar reset_counter no estado da sessão, se não existir
    if 'reset_counter' not in st.session_state:
        st.session_state['reset_counter'] = 0

    carregar_dados()

    # Gerar as tabelas separadas
    sumario_validade = gerar_sumario_validade()
    descritivos_estatisticos_pcl5 = gerar_descritivos_estatisticos(st.session_state['data'], 'PCL5')
    descritivos_estatisticos_ptci = gerar_descritivos_estatisticos(st.session_state['data'], 'PTCI')

    # Exibir as tabelas na tela
    st.write('Validade dos Casos para PCL-5 e PTCI:', sumario_validade)
    explicar_descritivos_estatisticos_pcl5_ptci()
    st.write('Descrição Estatística do PCL-5 Total:', descritivos_estatisticos_pcl5)
    st.write('Descrição Estatística do PTCI Total:', descritivos_estatisticos_ptci)

    # Concatenar as tabelas em formato de string para a geração da conclusão
    resultados_para_conclusao = f"{sumario_validade.to_string(index=False)}\n\n{descritivos_estatisticos_pcl5.to_string(index=False)}\n\n{descritivos_estatisticos_ptci.to_string(index=False)}"
    
    # Gerar conclusões baseadas nos resultados concatenados
    carregar_conclusoes(analysis_id, nome_analise, resultados_para_conclusao, instrucoes)
