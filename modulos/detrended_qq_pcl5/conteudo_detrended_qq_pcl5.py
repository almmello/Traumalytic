import streamlit as st

def explicar_detrended_qq_pcl5():
    st.markdown("""
    Nesta seção, apresentamos o Gráfico de Probabilidade Normal (Q-Q) Sem Tendência para os dados do PCL-5. Este gráfico é uma ferramenta estatística utilizada para avaliar se a distribuição dos dados segue uma distribuição normal. 

    No gráfico Q-Q, os pontos representam a distribuição dos escores do PCL-5 em comparação com uma distribuição normal teórica. Se os pontos seguirem uma linha reta, isso indica que os dados estão distribuídos normalmente. Desvios da linha reta sugerem que os dados podem ter uma distribuição diferente, como serem inclinados para a esquerda ou para a direita, ou terem caudas pesadas. 

    A análise do gráfico Q-Q Sem Tendência é crucial para validar suposições de normalidade em testes estatísticos subsequentes e para entender melhor as características dos dados do PCL-5, o que é fundamental para a interpretação correta dos resultados e para a aplicação adequada de técnicas estatísticas.
    """)
analysis_id = 'detrended_qq_pcl5'
nome_analise = 'Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PCL-5'
instrucoes = "Analisando os resultados da Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Descreva o Gráfico de Probabilidade Normal (Q-Q) Sem Tendência para os escores do PCL-5. Este gráfico é utilizado para avaliar a normalidade dos dados, removendo tendências lineares para uma análise mais precisa. Observe como os pontos no gráfico se alinham em relação à linha diagonal, que representa a distribuição normal ideal. Avalie se os pontos seguem uma linha reta, o que indicaria que os escores estão distribuídos normalmente. Identifique qualquer desvio significativo dos pontos em relação à linha, como padrões de agrupamento ou dispersão, e discuta o que esses desvios podem revelar sobre a distribuição dos escores de estresse pós-traumático na amostra. Destaque a presença de assimetria ou outliers e suas implicações para a interpretação dos dados do PCL-5."