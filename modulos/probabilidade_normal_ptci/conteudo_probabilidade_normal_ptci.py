import streamlit as st

def explicar_probabilidade_normal_ptci():
    st.markdown("""
    Este gráfico é uma ferramenta estatística usada para avaliar se a distribuição das pontuações do Inventário de Cognições Pós-Traumáticas (PTCI) se aproxima de uma distribuição normal. É essencial para verificar a adequação dos escores a muitos testes estatísticos que assumem a normalidade dos dados. A linha diagonal representa a distribuição esperada para uma distribuição normal, enquanto os pontos representam as pontuações observadas. Quanto mais próximos os pontos estiverem da linha, mais normal é a distribuição. Desvios da linha podem indicar assimetria ou a presença de outliers.
    """)
