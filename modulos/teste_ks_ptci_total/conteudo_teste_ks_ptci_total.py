import streamlit as st

def explicar_teste_ks_ptci_total():
    st.markdown("""
    Nesta seção, realizamos o Teste Kolmogorov-Smirnov com a Correção de Lilliefors para avaliar a normalidade do escore total do PTCI. Este teste estatístico é usado para determinar se uma amostra segue uma distribuição normal, o que é essencial para a aplicação de certos métodos estatísticos. Os resultados incluem a estatística de teste, que indica a máxima diferença entre a função de distribuição acumulada empírica e a função de distribuição acumulada normal, e o valor de significância (p-valor), que sugere a probabilidade de observar a atual distribuição de dados, assumindo que a distribuição é normal.
    """)
