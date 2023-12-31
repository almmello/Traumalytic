import streamlit as st

def explicar_histograma_ptci():
    st.markdown("""
    Nesta seção, apresentamos um histograma que ilustra a distribuição de frequências dos escores totais do PTCI. Este gráfico ajuda a visualizar a distribuição e a identificar padrões, como assimetria e picos nos dados dos escores do questionário.
""")

analysis_id = 'histograma_ptci'
nome_analise = 'Gráfico Histograma PTCI'
instrucoes = "Analisando os resultados da Gráfico Histograma PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Descrição do histograma de frequência dos valores totais do PTCI, representando a distribuição dos escores de trauma na amostra de dados. Explique a forma da distribuição e indique a tendência central, se visível."