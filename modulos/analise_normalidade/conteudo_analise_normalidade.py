import streamlit as st

def explicar_analise_normalidade():
    st.markdown("""
    ### Análise de Normalidade
    Esta seção foca na análise de normalidade das variáveis selecionadas, como escores totais de PCL-5 e PTCI e os clusters. A análise de normalidade é crucial para determinar os testes estatísticos apropriados nas etapas subsequentes da análise de dados.
    
    **Variáveis Disponíveis para Análise:**
    - **PCL5_total:** Escore total do PCL-5.
    - **PTCI_total:** Escore total do PTCI.
    - **Clusters A, B, C, D, E:** Clusters específicos do PCL-5 e PTCI.
    """)
