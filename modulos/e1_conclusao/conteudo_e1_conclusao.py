import streamlit as st

def explicar_e1_conclusao():
    st.markdown("""
    ### Conclusão da Etapa 1: Preparação dos Dados
    A Etapa 1 foca na preparação e limpeza dos dados para análise, estabelecendo uma base sólida para as análises subsequentes. Este módulo revisa as escolhas feitas para os conjuntos de dados A e B e avalia a adequação dessas escolhas para as análises estatísticas planejadas na Etapa 2.

    **Pontos Principais de Análise:**
    - Revisão das variáveis selecionadas para os conjuntos A e B.
    - Avaliação da importância de estudos estatísticos, incluindo Corte TEPT, Gráficos Histograma e Boxplot, e Exibição de Caule-e-Folhas.
    - Recomendações para otimizar as análises na Etapa 2, com base nas características dos dados preparados.
    
    A análise realizada aqui é crucial para assegurar que os dados estão prontos para análises mais complexas, incluindo descritivas, de normalidade e inferenciais, e para orientar a escolha dos métodos estatísticos mais adequados nas próximas etapas.
    """)

pref_analysis_id = 'e1_conclusao'
nome_analise = 'Conclusão Etapa 1'
etapa_analise = 1
instrucoes = "Analisando as variáveis escolhidas para a coleção A e B, gere uma conclusão que auxílie na escolha dos estudos estatísticos da Etapa 2. Analise a importancia dos seguinte estudos para as coleções escolhidas: Estudos Estatísticos, Corte TEPT, Gráfico Histograma, Gráfico Boxplot, Exibição de Caule-e-Folhas. Lembre-se que o objetivo deste processo de analise é encontrar correlações entre o conjunto A e B, portanto, quando você criar sua coclusão deve sempre ter este objetivo em mente. Adicione, em sua conclusão, uma lista com os estudos estatísticos que você recomenda para a coleção A e B."
