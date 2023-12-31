import streamlit as st

def explicar_corr_pearson_pcl5_total_ptci_total():
    st.markdown("""
    Nesta seção, focamos na análise de correlação paramétrica entre os escores totais do PCL-5 (Posttraumatic Stress Disorder Checklist for DSM-5) e do PTCI (Inventário de Cognições Pós-Traumáticas). A ferramenta principal utilizada aqui é o Coeficiente de Correlação de Pearson, que mede a força e a direção da relação linear entre os escores totais de ambos os instrumentos.

    O PCL-5 é uma ferramenta de avaliação para sintomas do Transtorno de Estresse Pós-Traumático (TEPT), enquanto o PTCI mede as cognições pós-traumáticas. Ao correlacionar os escores totais desses dois instrumentos, buscamos entender como os sintomas gerais de TEPT, representados pelo PCL-5, estão associados às cognições e crenças pós-traumáticas avaliadas pelo PTCI.

    Esta análise é crucial para aprofundar nosso entendimento sobre a relação entre os sintomas de TEPT e os padrões cognitivos pós-trauma. Tal compreensão é fundamental para o desenvolvimento de estratégias de intervenção e tratamento mais eficazes para indivíduos afetados por experiências traumáticas.
    """)

analysis_id = 'corr_pearson_pcl5_total_ptci_total'
nome_analise = 'Correlação Paramétrica entre PCL5 Total e PTCI Total'
instrucoes = "Analisando os resultados da Correlação Paramétrica entre PCL5 Total e PTCI Total, forneça uma conclusão detalhada e útil sobre as implicações desses dados."
prompt_plot = "Analise este gráfico de calor que ilustra a correlação paramétrica entre os escores totais do PCL-5 e do PTCI. O gráfico exibe uma matriz colorida onde cada cor e valor numérico correspondente indica o nível de correlação entre os escores totais dos dois instrumentos. Cores mais quentes representam uma correlação mais forte, e cores mais frias indicam uma correlação mais fraca ou negativa. Utilize as variações de cor e os valores numéricos para interpretar a relação entre a severidade dos sintomas de TEPT, avaliados pelo PCL-5, e as cognições pós-traumáticas, medidas pelo PTCI. Discuta o significado dessa correlação e suas possíveis implicações para entender como os sintomas de TEPT estão associados a padrões cognitivos específicos em indivíduos após experiências traumáticas, realçando a importância dessas descobertas para intervenções clínicas e direções de pesquisa futura no campo do trauma psicológico."