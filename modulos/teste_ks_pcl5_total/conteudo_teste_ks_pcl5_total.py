import streamlit as st

def explicar_teste_ks_pcl5_total():
    st.markdown("""
    Nesta seção, realizamos o Teste Kolmogorov-Smirnov com a Correção de Lilliefors para avaliar a normalidade do escore total do PCL-5. Este teste estatístico é usado para determinar se uma amostra segue uma distribuição normal, o que é essencial para a aplicação de certos métodos estatísticos. Os resultados incluem a estatística de teste, que indica a máxima diferença entre a função de distribuição acumulada empírica e a função de distribuição acumulada normal, e o valor de significância (p-valor), que sugere a probabilidade de observar a atual distribuição de dados, assumindo que a distribuição é normal.
    """)
analysis_id = 'teste_ks_pcl5_total'
nome_analise = 'Teste Kolmogorov-Smirnov para PCL-5 Total'
instrucoes = "Analisando os resultados da Teste Kolmogorov-Smirnov para PCL-5 Total, forneça uma conclusão detalhada e útil sobre as implicações desses dados."