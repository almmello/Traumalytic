import streamlit as st

def explicar_probabilidade_normal_pcl5():
    st.markdown("""
    O Gráfico Q-Q é uma ferramenta analítica para avaliar se os escores do PCL-5 seguem uma distribuição normal. Neste gráfico, os quantis dos escores observados são plotados em relação aos quantis esperados de uma distribuição normal. Se os dados são normalmente distribuídos, os pontos devem se alinhar próximos à linha de referência diagonal. Desvios da linha sugerem uma distribuição assimétrica ou a presença de outliers. A conformidade com a linha diagonal fornece uma visualização clara da tendência central e da variabilidade dos dados, oferecendo insights sobre a normalidade dos escores de estresse pós-traumático na amostra.
    """)
analysis_id = 'probabilidade_normal_pcl5'
nome_analise = 'Gráfico de Probabilidade Normal do PCL-5'
instrucoes = "Analisando os resultados da Gráfico de Probabilidade Normal do PCL-5, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Descreva o Gráfico de Probabilidade Normal, também conhecido como Gráfico Q-Q, para os escores do PCL-5. Discuta como os pontos se alinham em relação à linha de referência, que representa uma distribuição normal. Indique se os pontos formam uma linha aproximadamente reta, o que sugeriria que os escores seguem uma distribuição normal. Observe quaisquer desvios significativos dos pontos da linha, que podem indicar assimetria ou a presença de outliers. Discuta as implicações de tais desvios em termos de normalidade dos dados e o que isso pode revelar sobre as características dos escores de estresse pós-traumático na amostra."