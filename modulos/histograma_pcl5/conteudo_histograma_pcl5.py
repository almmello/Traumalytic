import streamlit as st

def explicar_histograma_pcl5():
    st.markdown("""
    Nesta seção, apresentamos um histograma que ilustra a distribuição de frequências dos escores totais do PCL-5. Este gráfico ajuda a visualizar a distribuição e a identificar padrões, como assimetria e picos nos dados dos escores do questionário.
    """)
analysis_id = 'histograma_pcl5'
nome_analise = 'Gráfico Histograma PCL-5'
instrucoes = "Analisando os resultados da Gráfico Histograma PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Descrição do histograma de frequência dos valores totais do PCL-5, representando a distribuição dos escores de trauma na amostra de dados. Explique a forma da distribuição e indique a tendência central, se visível."