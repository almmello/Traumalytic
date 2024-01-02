import streamlit as st

def explicar_teste_t_pcl5_clusters_ptci_clusters():
    st.markdown("""
    ### Teste T de Student entre os Clusters do PCL5 e PTCI
    Nesta seção, conduzimos um Teste T de Student para comparar as médias dos escores dos clusters do PCL-5 (Posttraumatic Stress Disorder Checklist) e do PTCI (Posttraumatic Cognitions Inventory). O Teste T é utilizado para avaliar se existem diferenças estatisticamente significativas nas médias dos escores de diferentes clusters, o que pode indicar padrões distintos entre os sintomas de TEPT e as cognições pós-traumáticas.
    """)

analysis_id = 'teste_t_pcl5_clusters_ptci_clusters'
nome_analise = 'Teste T Student entre os Clusters do PCL5 e PTCI'
instrucoes = "Analise os resultados do Teste T de Student entre os clusters do PCL5 e PTCI. Forneça uma conclusão detalhada e útil sobre o que essas diferenças nas médias dos escores podem indicar sobre a relação entre diferentes aspectos dos sintomas de TEPT e cognições pós-traumáticas."
prompt_plot = "Analise este gráfico de barras que ilustra as médias dos escores dos clusters do PCL-5 e do PTCI, acompanhadas pelos resultados do Teste T de Student. O gráfico mostra as médias de cada cluster, destacando comparações entre eles. Utilize as informações sobre as médias, as barras de erro e os resultados do Teste T (valor-p) para interpretar se as diferenças observadas são estatisticamente significativas. Discuta as possíveis implicações dessas diferenças para entender como diversos aspectos dos sintomas de TEPT e cognições pós-traumáticas estão relacionados, enfatizando a importância dessas descobertas para intervenções clínicas e pesquisas futuras no campo do trauma psicológico."
