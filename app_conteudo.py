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



