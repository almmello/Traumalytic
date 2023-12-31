import streamlit as st

def explicar_shapiro_wilk_ptci_total():
    st.markdown("""
    O Teste de Shapiro-Wilk é um método estatístico que avalia a aderência dos escores totais do Inventário de Cognições Pós-Traumáticas (PTCI) à distribuição normal. Este teste é essencial para determinar a adequação de técnicas estatísticas paramétricas, que pressupõem a normalidade dos dados. Um p-valor menor que o limiar (comumente 0,05) indicaria uma distribuição não normal dos escores do PTCI, potencialmente afetando as inferências estatísticas e a interpretação dos padrões de cognição pós-traumática na amostra estudada.
    """)

analysis_id = 'shapiro_wilk_ptci_total'
nome_analise = 'Teste de Shapiro-Wilk para PTCI Total'
instrucoes = "Analisando os resultados da Teste de Shapiro-Wilk para PTCI Total, forneça uma conclusão detalhada e útil sobre as implicações desses dados."