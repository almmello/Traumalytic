import streamlit as st

def explicar_corr_spearman_pcl5_total_ptci_total():
    st.markdown("""
    ### Correlação Spearman entre PCL5 Total e PTCI Total
    Nesta seção, é calculada a correlação de Spearman entre os escores totais do PCL-5 e do PTCI. A correlação de Spearman é uma medida não paramétrica de correlação de posto que avalia a força e direção da associação entre duas variáveis contínuas ou ordinais.
    """)

analysis_id = 'corr_spearman_pcl5_total_ptci_total'
nome_analise = 'Correlação Spearman entre PCL5 Total e PTCI Total'
instrucoes = "Por favor, analise os resultados da Correlação de Spearman entre os escores totais do PCL-5 e do PTCI. Forneça uma conclusão detalhada e útil sobre as implicações desses dados para compreender a relação entre a severidade dos sintomas de TEPT e as cognições pós-traumáticas."
prompt_plot = "Analise esta tabela que ilustra a correlação de Spearman entre os escores totais do PCL-5 e do PTCI. A tabela exibe os valores de correlação entre os escores, onde cada valor numérico indica o nível de associação entre os escores totais dos dois instrumentos. Valores de correlação próximos de 1 ou -1 indicam uma forte associação positiva ou negativa, respectivamente, enquanto valores próximos de 0 indicam ausência de associação. Interprete a magnitude da correlação e discuta suas possíveis implicações para compreender a conexão entre os sintomas de TEPT e os padrões cognitivos em indivíduos após experiências traumáticas, destacando a relevância dessas descobertas para intervenções clínicas e pesquisas futuras no campo do trauma psicológico."
