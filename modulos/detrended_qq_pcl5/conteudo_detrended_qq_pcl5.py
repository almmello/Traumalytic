import streamlit as st

def explicar_detrended_qq_pcl5():
    st.markdown("""
    Este gráfico é uma ferramenta visual utilizada para avaliar se os dados dos escores totais do PCL-5 seguem uma distribuição normal. O gráfico Q-Q Sem Tendência é uma variação do gráfico Q-Q tradicional, onde os efeitos de tendência linear são removidos. Isso permite uma avaliação mais precisa da normalidade dos dados. Pontos que se alinham ao longo da linha diagonal indicam uma distribuição normal, enquanto desvios significativos da linha podem sugerir assimetria ou a presença de outliers. Este gráfico é especialmente útil para identificar padrões específicos de desvios da normalidade.
    """)