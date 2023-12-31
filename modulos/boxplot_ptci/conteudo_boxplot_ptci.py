import streamlit as st

def explicar_boxplot_ptci():
    st.markdown("""
    Esta seção apresenta um Box Plot que ilustra a distribuição das pontuações do PTCI entre os participantes do estudo. O Box Plot é uma ferramenta gráfica útil para visualizar a variação, a mediana e os outliers nas respostas ao PTCI. A análise inclui a identificação de elementos-chave como o quartil inferior, a mediana, o quartil superior e possíveis valores extremos, fornecendo uma visão abrangente da dispersão das pontuações de estresse pós-traumático.
    """)
analysis_id = 'boxplot_ptci'
nome_analise = 'Gráfico Boxplot do PTCI'
instrucoes = "Analisando os resultados da Gráfico Boxplot do PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Analise visualmente o Boxplot gerado para os escores do Inventário de Cognições Pós-Traumáticas (PTCI). Descreva os elementos principais do gráfico, como a localização da mediana, a distribuição dos quartis, a presença e significado de possíveis outliers e a simetria da distribuição dos escores. Discuta o que essas características indicam sobre a variabilidade e centralidade dos escores do PTCI na amostra de estudo. Avalie se a distribuição dos escores sugere normalidade ou inclinação (para a esquerda ou direita), e explore as possíveis implicações desses padrões na compreensão das experiências traumáticas dos participantes."