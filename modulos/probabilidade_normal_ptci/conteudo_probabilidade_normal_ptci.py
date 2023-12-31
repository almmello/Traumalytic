import streamlit as st

def explicar_probabilidade_normal_ptci():
    st.markdown("""
    Este gráfico é uma ferramenta estatística usada para avaliar se a distribuição das pontuações do Inventário de Cognições Pós-Traumáticas (PTCI) se aproxima de uma distribuição normal. É essencial para verificar a adequação dos escores a muitos testes estatísticos que assumem a normalidade dos dados. A linha diagonal representa a distribuição esperada para uma distribuição normal, enquanto os pontos representam as pontuações observadas. Quanto mais próximos os pontos estiverem da linha, mais normal é a distribuição. Desvios da linha podem indicar assimetria ou a presença de outliers.
    """)
analysis_id = 'probabilidade_normal_ptci'
nome_analise = 'Gráfico de Probabilidade Normal do PTCI'
instrucoes = "Analisando os resultados da Gráfico de Probabilidade Normal do PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Analise o Gráfico de Probabilidade Normal para os escores do Inventário de Cognições Pós-Traumáticas (PTCI). Comente sobre a aderência dos pontos à linha reta teórica que representa uma distribuição normal. Identifique se os pontos seguem uma linha reta ou se há desvios significativos, o que indicaria a presença de assimetria ou outliers nos dados. Reflita sobre o que a forma do gráfico sugere acerca da distribuição dos escores de cognições pós-traumáticas e considere as possíveis interpretações psicológicas desses achados em relação à experiência de trauma nos participantes."