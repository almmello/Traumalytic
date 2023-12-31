import streamlit as st

def explicar_corr_pearson_pcl5_clusters_ptci_clusters():
    st.markdown("""
    ### Correlação Paramétrica entre Clusters do PCL-5 e PTCI
    Nesta seção, o aplicativo realiza uma análise de correlação paramétrica entre os clusters do PCL-5 (Posttraumatic Stress Disorder Checklist for DSM-5) e os clusters do PTCI (Inventário de Cognições Pós-Traumáticas). Utilizamos o Coeficiente de Correlação de Pearson para explorar a relação linear entre as variáveis desses dois instrumentos.
    
    O PCL-5 avalia os sintomas do Transtorno de Estresse Pós-Traumático (TEPT) e é dividido em quatro clusters: Intrusões (Cluster B), Evitação (Cluster C), Cognições e Humor (Cluster D) e Reatividade (Cluster E). Por outro lado, o PTCI avalia os pensamentos e crenças pós-traumáticas, divididos em três clusters: Cognições Negativas sobre o Self (Cluster A), Cognições Negativas sobre o Mundo (Cluster B) e Cognições de Autorresponsabilização (Cluster C).
    
    A correlação de Pearson é calculada para cada par de clusters correspondentes entre os dois instrumentos, fornecendo insights sobre como as cognições e os sintomas de TEPT estão inter-relacionados em indivíduos que passaram por experiências traumáticas. Esta análise pode auxiliar profissionais da saúde mental no entendimento das complexidades do TEPT e no desenvolvimento de intervenções mais eficazes.
    """)

analysis_id = 'corr_pearson_pcl5_clusters_ptci_clusters'
nome_analise = 'Correlação Paramétrica entre os Clusters do PCL5 e PTCI'
instrucoes = "Analisando os resultados da Correlação Paramétrica entre os Clusters do PCL5 e PTCI, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Analise este gráfico de calor que ilustra a correlação paramétrica entre os escores totais do PCL-5 e do PTCI. O gráfico exibe uma matriz colorida onde cada cor e valor numérico correspondente indica o nível de correlação entre os escores totais dos dois instrumentos. Cores mais quentes representam uma correlação mais forte, e cores mais frias indicam uma correlação mais fraca ou negativa. Utilize as variações de cor e os valores numéricos para interpretar a relação entre a severidade dos sintomas de TEPT, avaliados pelo PCL-5, e as cognições pós-traumáticas, medidas pelo PTCI. Discuta o significado dessa correlação e suas possíveis implicações para entender como os sintomas de TEPT estão associados a padrões cognitivos específicos em indivíduos após experiências traumáticas, realçando a importância dessas descobertas para intervenções clínicas e direções de pesquisa futura no campo do trauma psicológico."
