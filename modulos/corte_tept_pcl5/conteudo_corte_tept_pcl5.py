import streamlit as st

def explicar_estatisticas_gerais_tept():
    st.markdown("""
    ### Estatísticas Gerais de TEPT
    Esta parte da análise fornece um resumo numérico dos casos analisados. O número total de participantes (`N`), o número de respostas válidas (`Valid`) e o número de respostas faltantes (`Missing`) são contabilizados para dar uma visão geral da completude dos dados referentes aos sintomas de TEPT com base no PCL-5.
    """)

def explicar_frequencias_tept():
    st.markdown("""
    ### Frequências de Diagnóstico de TEPT
    Após a aplicação do ponto de corte no PCL-5, esta análise detalha a frequência e a porcentagem dos participantes que possuem ou não sintomas que sugerem TEPT. Inclui a porcentagem válida dos diagnósticos e a porcentagem cumulativa, permitindo avaliar a distribuição dos sintomas de TEPT dentro da amostra estudada.
    """)


