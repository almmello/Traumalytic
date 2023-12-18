import streamlit as st

def explicar_visualizacao_itens_pcl5():
    st.markdown("""
    Esta seção apresenta as respostas individuais aos itens do Posttraumatic Stress Disorder Checklist for DSM-5 (PCL-5), juntamente com informações demográficas dos participantes. Este módulo permite uma análise detalhada das respostas a cada item do questionário PCL-5, que é utilizado para avaliar os sintomas de TEPT. A visualização inclui dados demográficos e respostas a todas as 20 questões do PCL-5.
    """)


def explicar_visualizacao_clusters_pcl5():
    st.markdown("""
    ### Análise dos Clusters do PCL-5
    Esta seção exibe os resultados dos cálculos dos clusters do Posttraumatic Stress Disorder Checklist for DSM-5 (PCL-5). Os clusters representam diferentes aspectos dos sintomas de TEPT:
    
    - Cluster B: Intrusões (PCL01 a PCL05)
    - Cluster C: Evitação (PCL06 e PCL07)
    - Cluster D: Cognições e Humor Negativos (PCL08 a PCL14)
    - Cluster E: Hiperativação (PCL15 a PCL20)

    Além dos clusters, são apresentadas as médias para cada cluster e o escore total do PCL-5. As informações demográficas dos participantes também são incluídas, proporcionando um contexto mais rico para a análise dos sintomas de TEPT.
    """)
