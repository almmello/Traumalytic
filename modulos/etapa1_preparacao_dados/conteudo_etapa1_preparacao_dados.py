import streamlit as st

def explicar_etapa1_preparacao_dados():
    st.markdown("""
    ### Etapa 1: Preparação dos Dados

    Nesta etapa, ocorre o processo de carregamento, limpeza e filtragem dos dados. 
    As principais ações realizadas são:

    - **Carregamento dos Dados**: Os dados são carregados a partir de um arquivo fonte. 
      Este processo inclui a descriptografia dos dados, quando necessário.

    - **Limpeza dos Dados**: Etapa crucial onde os dados são limpos para remover 
      inconsistências, valores nulos ou dados corrompidos que podem afetar a análise.

    - **Filtragem dos Dados**: Após a limpeza, os dados são filtrados com base em 
      critérios definidos pelo usuário, como faixa etária, sexo e nível de instrução. 
      Esta etapa é importante para focar a análise em um subconjunto específico de dados.

    O objetivo dessa etapa é assegurar que os dados estejam prontos e em formato adequado 
    para as análises subsequentes.
    """)

