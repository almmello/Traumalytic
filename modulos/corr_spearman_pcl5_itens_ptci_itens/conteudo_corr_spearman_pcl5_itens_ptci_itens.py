import streamlit as st

def explicar_corr_spearman_pcl5_itens_ptci_itens():
    st.markdown("""
    ### Correlação Spearman entre os Itens do PCL5 e PTCI
    Nesta seção, exploramos a correlação de Spearman entre os itens individuais do PCL-5 e do PTCI. A correlação de Spearman é uma medida não paramétrica usada para avaliar a força e direção da associação entre duas variáveis, sendo particularmente útil para dados que não seguem uma distribuição normal ou quando a relação entre as variáveis não é linear.
    """)

analysis_id = 'corr_spearman_pcl5_itens_ptci_itens'
nome_analise = 'Correlação Spearman entre os Itens do PCL5 e PTCI'
instrucoes = "Analisando os resultados da Correlação Spearman entre os Itens do PCL5 e PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
