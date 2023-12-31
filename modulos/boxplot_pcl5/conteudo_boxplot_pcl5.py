import streamlit as st

def explicar_boxplot_pcl5():
    st.markdown("""
    Esta seção apresenta um Box Plot que ilustra a distribuição das pontuações do PCL-5 (Posttraumatic Stress Disorder Checklist for DSM-5) entre os participantes do estudo. O Box Plot é uma ferramenta gráfica útil para visualizar a variação, a mediana e os outliers nas respostas ao PCL-5. A análise inclui a identificação de elementos-chave como o quartil inferior, a mediana, o quartil superior e possíveis valores extremos, fornecendo uma visão abrangente da dispersão das pontuações de estresse pós-traumático.
    """)

analysis_id = 'boxplot_pcl5'
nome_analise = 'Gráfico Boxplot do PCL-5'
instrucoes = "Analisando os resultados da Gráfico Boxplot do PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Descreva os elementos-chave do gráfico, incluindo a posição da mediana, a amplitude dos quartis, a presença de outliers e a simetria da distribuição. Discuta o que essas características visuais podem sugerir sobre a variabilidade e a tendência central dos escores do PCL-5 na amostra estudada. Avalie se a distribuição parece ser normal, inclinada para a esquerda ou para a direita, e quais implicações isso pode ter para a interpretação dos resultados em um contexto de estresse pós-traumático."

