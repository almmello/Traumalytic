import streamlit as st

def explicar_corr_pearson_pcl5_itens_ptci_itens():
    st.markdown("""
    ### Estatísticas de Idade
    Nesta parte, são calculadas estatísticas descritivas (média, mediana, desvio padrão, etc.) relacionadas à idade dos participantes do estudo.
    """)

analysis_id = 'corr_pearson_pcl5_itens_ptci_itens'
nome_analise = 'Correlação Paramétrica entre os Itens do PCL5 e PTCI'
instrucoes = "Analisando os resultados da Correlação Paramétrica entre os Itens do PCL5 e PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Analise este gráfico de calor que ilustra a correlação paramétrica entre os escores totais do PCL-5 e do PTCI. O gráfico exibe uma matriz colorida onde cada cor e valor numérico correspondente indica o nível de correlação entre os escores totais dos dois instrumentos. Cores mais quentes representam uma correlação mais forte, e cores mais frias indicam uma correlação mais fraca ou negativa. Utilize as variações de cor e os valores numéricos para interpretar a relação entre a severidade dos sintomas de TEPT, avaliados pelo PCL-5, e as cognições pós-traumáticas, medidas pelo PTCI. Discuta o significado dessa correlação e suas possíveis implicações para entender como os sintomas de TEPT estão associados a padrões cognitivos específicos em indivíduos após experiências traumáticas, realçando a importância dessas descobertas para intervenções clínicas e direções de pesquisa futura no campo do trauma psicológico."
