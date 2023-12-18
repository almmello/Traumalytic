import streamlit as st

def mostrar_conteudo():
    st.title("Bem-vindo à Aplicação Traumalytic")
    
    st.markdown("""
    A aplicação Traumalytic é uma plataforma avançada projetada para a análise de dados relacionados ao trauma psicológico. Utilizando ferramentas de processamento de dados e análise estatística, a Traumalytic oferece insights valiosos para profissionais da saúde mental, focando especialmente na análise de respostas aos questionários PTCI e PCL-5.

    ### Funcionalidades:

    - **Análise Descritiva:** Medidas de tendência central, dispersão e exame das propriedades da distribuição dos dados.
    - **Análise de Normalidade:** Verifica a normalidade na distribuição dos dados.
    - **Análise de Correlação:** Utiliza o coeficiente de correlação de Pearson para explorar associações entre variáveis.
    - **Teste t de Student:** Para comparação de médias entre grupos.

    ### Testes Específicos:

    - **PTCI (Inventário de Cognições Pós-Traumáticas):** Avalia pensamentos e crenças após a exposição a eventos traumáticos. É uma ferramenta crucial para entender como os traumas afetam a cognição das pessoas.
    - **PCL-5 (Posttraumatic Stress Disorder Checklist for DSM-5):** Lista de verificação utilizada para avaliar os sintomas de TEPT (Transtorno de Estresse Pós-Traumático) de acordo com o DSM-5. É fundamental para identificar e mensurar a severidade dos sintomas relacionados ao TEPT.

    Esta aplicação é uma ferramenta essencial para pesquisadores e clínicos no campo da psicologia do trauma, permitindo uma compreensão mais profunda e um tratamento mais eficaz de condições relacionadas a traumas.
    """)


def explicar_filtro_idade():
    st.markdown("""
    ### Filtro de Faixa Etária
    Selecione a faixa etária dos participantes para focar em um grupo etário específico. Isso permite analisar os dados com base na idade dos respondentes.
    """)

def explicar_filtro_idade_nulos():
    st.markdown("""
    ### Filtro de Idades Nulas
    Ao marcar esta opção, você remove da análise os registros com idades incompletas ou ausentes nos questionários PTCI e PCL-5.
    """)

def explicar_filtro_pcti():
    st.markdown("""
    ### Filtro de Dados Nulos no PTCI
    Ao marcar esta opção, você remove da análise os registros com respostas incompletas ou ausentes no questionário PTCI. Isso garante a análise de dados mais completos e confiáveis.
    """)

def explicar_filtro_pcl5():
    st.markdown("""
    ### Filtro de Dados Nulos no PCL-5
    Similar ao filtro PTCI, esta opção exclui registros com dados incompletos ou ausentes no questionário PCL-5, proporcionando uma análise mais precisa dos sintomas relacionados ao TEPT.
    """)

def explicar_ponto_de_corte_tept():
    st.markdown("""
    ### Ponto de Corte para Diagnóstico de TEPT
    O ponto de corte é o valor limiar usado para determinar a possível presença de TEPT com base no escore total do PCL-5. Um escore acima desse ponto de corte indica que o número de sintomas relatados pode ser suficiente para um diagnóstico de TEPT, enquanto um escore abaixo sugere que os sintomas não atingem o limiar clínico para o diagnóstico.
    """)

