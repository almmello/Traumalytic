import streamlit as st

def explicar_teste_t_pcl5_total_ptci_total():
    st.markdown("""
    ### Teste T de Student entre PCL5 Total e PTCI Total
    Nesta seção, realizamos um Teste T de Student para comparar as médias dos escores totais do PCL-5 (Posttraumatic Stress Disorder Checklist) e do PTCI (Posttraumatic Cognitions Inventory). Este teste é usado para avaliar se as diferenças nas médias dos escores totais entre os dois grupos são estatisticamente significativas.
    """)

analysis_id = 'teste_t_pcl5_total_ptci_total'
nome_analise = 'Teste T Student entre PCL5 Total e PTCI Total'
instrucoes = "Analisando os resultados do Teste T de Student entre PCL5 Total e PTCI Total, forneça uma conclusão detalhada e útil sobre o que essas diferenças nas médias dos escores podem indicar. Discuta as implicações desses resultados para compreender a relação entre os sintomas de TEPT e as cognições pós-traumáticas."
prompt_plot = "Analise este gráfico de barras que ilustra as médias dos escores totais do PCL-5 e do PTCI, junto com os resultados do Teste T de Student. O gráfico apresenta as médias dos escores para cada instrumento, destacando a comparação entre eles. Utilize as informações sobre as médias e o resultado do Teste T (valor-p) para interpretar se as diferenças observadas são estatisticamente significativas. Discuta as possíveis implicações destas diferenças para entender a relação entre os sintomas de TEPT, avaliados pelo PCL-5, e as cognições pós-traumáticas, medidas pelo PTCI, realçando a importância dessas descobertas para intervenções clínicas e pesquisas futuras no campo do trauma psicológico."
