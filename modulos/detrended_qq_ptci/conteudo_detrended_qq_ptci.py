import streamlit as st

def explicar_detrended_qq_ptci():
    st.markdown("""
    Nesta seção, apresentamos o Gráfico de Probabilidade Normal (Q-Q) Sem Tendência para os dados do PTCI (Inventário de Cognições Pós-Traumáticas). Este gráfico é uma ferramenta estatística utilizada para avaliar se a distribuição dos dados segue uma distribuição normal. 

    No gráfico Q-Q, os pontos representam a distribuição dos escores do PTCI em comparação com uma distribuição normal teórica. Se os pontos seguirem uma linha reta, isso indica que os dados estão distribuídos normalmente. Desvios da linha reta sugerem que os dados podem ter uma distribuição diferente, como serem inclinados para a esquerda ou para a direita, ou terem caudas pesadas. 

    A análise do gráfico Q-Q Sem Tendência é crucial para validar suposições de normalidade em testes estatísticos subsequentes e para entender melhor as características dos dados do PTCI, o que é fundamental para a interpretação correta dos resultados e para a aplicação adequada de técnicas estatísticas.
    """)
analysis_id = 'detrended_qq_ptci'
nome_analise = 'Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PTCI'
instrucoes = "Analisando os resultados da Gráfico de Probabilidade Normal (Q-Q) Sem Tendência do PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Descreva o Gráfico de Probabilidade Normal (Q-Q) Sem Tendência para os escores do PTCI. Este gráfico visualiza a adequação da distribuição dos escores do PTCI a uma distribuição normal teórica, removendo tendências lineares para focar na normalidade dos dados. Observe como os pontos se distribuem em relação à linha diagonal, que representa a distribuição normal ideal. Avalie se os pontos seguem uma trajetória linear, sugerindo uma distribuição normal dos escores. Identifique quaisquer padrões anormais ou desvios dos pontos da linha, tais como agrupamentos ou dispersões, e discuta suas possíveis implicações. Especial atenção deve ser dada à presença de assimetria ou outliers, e como isso pode afetar a interpretação dos resultados do PTCI em um contexto de cognições pós-traumáticas."