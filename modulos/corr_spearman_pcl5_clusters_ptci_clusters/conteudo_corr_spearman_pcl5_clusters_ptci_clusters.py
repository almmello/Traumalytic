import streamlit as st

def explicar_corr_spearman_pcl5_clusters_ptci_clusters():
    st.markdown("""
    ### Correlação Spearman entre os Clusters do PCL5 e PTCI
    Nesta seção, exploramos a correlação de Spearman entre diferentes clusters do PCL-5 (Posttraumatic Stress Disorder Checklist) e do PTCI (Posttraumatic Cognitions Inventory). A correlação de Spearman é utilizada para avaliar a força e direção da associação entre dois conjuntos de dados, sendo particularmente útil para dados não paramétricos.
    """)
analysis_id = 'corr_spearman_pcl5_clusters_ptci_clusters'
nome_analise = 'Correlação Spearman entre os Clusters do PCL5 e PTCI'
instrucoes = "Analisando os resultados da Correlação Spearman entre os Clusters do PCL5 e PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Analise este gráfico de calor que ilustra a correlação de Spearman entre os clusters dos instrumentos PCL-5 e PTCI. O gráfico apresenta uma matriz colorida, onde cada cor e valor numérico correspondente reflete o nível de correlação entre os diferentes clusters dos dois instrumentos. Cores mais quentes indicam uma correlação mais forte, enquanto cores mais frias representam uma correlação mais fraca ou negativa. Interprete as variações de cor e os valores numéricos para compreender como diferentes aspectos dos sintomas de TEPT, avaliados pelos clusters do PCL-5, estão relacionados com os padrões cognitivos pós-traumáticos, medidos pelos clusters do PTCI. Discuta o significado dessas correlações e suas possíveis implicações para intervenções clínicas e pesquisas futuras no campo do trauma psicológico."
