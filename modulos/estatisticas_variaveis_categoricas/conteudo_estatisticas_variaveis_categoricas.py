import streamlit as st

def explicar_estatisticas_variaveis_categoricas():
    st.markdown("""
    ### Análise Estatística de Variáveis Categóricas
    Nesta seção, são analisadas as variáveis categóricas do estudo, que incluem gênero (Feminino, Masculino) e níveis de educação (Ensino Médio Completo, Ensino Superior Incompleto, Ensino Superior Completo, Ensino Fundamental Incompleto, Ensino Médio Incompleto, Ensino Técnico Completo, Ensino Fundamental Completo, Especialização de Nível Superior). Serão exploradas as frequências e proporções dessas categorias entre os participantes, proporcionando uma visão geral da composição demográfica e educacional da amostra. Esta análise é fundamental para entender a distribuição das características dos participantes e pode revelar insights importantes sobre o grupo estudado.
    """)

analysis_id = 'estatisticas_variaveis_categoricas'

nome_analise = 'Estatísticas de Variáveis Categóricas'

instrucoes = "Analisando os resultados da Estatísticas de Variáveis Categóricas, forneça uma conclusão detalhada e útil sobre as implicações desses dados."