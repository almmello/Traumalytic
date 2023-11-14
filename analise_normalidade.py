import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from calculations import (
    testar_normalidade,
    criar_histograma,
    criar_grafico_qq,
    gerar_dados_normal,
    calcular_p_valor_normal
)

def carregar_dados():
    # Carregar dados aqui
    data = pd.read_excel('Banco LEC PCL5 PTCI.xlsx')
    return data

def formatar_p_valor(p_valor):
    return f"{p_valor:.2f}" if p_valor > 0.0001 else f"{p_valor:.2e}"

def interpretar_resultados_a(p_valor):
    p_valor_formatado = formatar_p_valor(p_valor)
    conclusao_a = "\n### Conclusão\n"
    conclusao_a += f"Os dados {'não ' if p_valor < 0.05 else ''}parecem seguir uma distribuição normal, pois o resultado {p_valor_formatado} é {'menor' if p_valor < 0.05 else 'maior'} que 0.05.\n"
    conclusao_a += "\n### Análise do Histograma\n"
    conclusao_a += "Isso é corroborado pelo histograma, onde esperamos ver uma forma de sino para uma distribuição normal.\n"
    conclusao_a += "\n##### Exemplo de Histograma com uma distribuição normal\n"
    return conclusao_a

def interpretar_resultados_b(p_valor):
    conclusao_b = "\n### Análise do Gráfico QQ\n"
    conclusao_b += "Numa distribuição normal, o gráfico Q-Q deve mostrar os pontos alinhados com a linha reta. Desvios significativos da linha no gráfico Q-Q indicam desvios da normalidade."
    conclusao_b += "\n##### Exemplo de Gráfico Q-Q com uma distribuição normal\n"
    return conclusao_b

def mostrar_analise_normalidade():
    st.title("Análise de Normalidade")

    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = carregar_dados()

    # Seleção da variável de interesse
    st.write("Escolha a Variável para Análise")
    selected_var = st.selectbox("Selecione uma Variável", ['PCL5_total', 'PTCI_total', 'Cluster_A', 'Cluster_B', 'Cluster_C', 'Cluster_D', 'Cluster_E'])

    # Botão para iniciar a análise
    if st.button('Analisar'):
        if selected_var:
            # Realizar o teste de Shapiro-Wilk e obter os gráficos para os dados do usuário
            resultados_normalidade, data_escores_temp = testar_normalidade(st.session_state['data'])
            st.session_state['data_escores'] = data_escores_temp
            p_valor = resultados_normalidade.get(selected_var, 'Variável não encontrada')
            st.write(f'Resultados do Teste de Normalidade para {selected_var} (p-valor): {formatar_p_valor(p_valor)}')

            # Gerar e mostrar os gráficos para os dados do usuário
            descricao_x_hist = f'Valores de {selected_var}'
            descricao_y_hist = 'Frequência'
            fig_hist = criar_histograma(st.session_state['data_escores'], selected_var, descricao_x_hist, descricao_y_hist)
            st.pyplot(fig_hist)
            plt.close(fig_hist)

            descricao_x_qq = 'Quantis Teóricos da Distribuição Normal'
            descricao_y_qq = f'Quantis Reais de {selected_var}'
            fig_qq = criar_grafico_qq(st.session_state['data_escores'], selected_var, descricao_x_qq, descricao_y_qq)
            st.pyplot(fig_qq)
            plt.close(fig_qq)

            # Exibir a parte A da conclusão da análise
            conclusao_a = interpretar_resultados_a(p_valor)
            st.write(conclusao_a)

            # Gerar dados de exemplo para uma distribuição normal
            dados_exemplo_normal = gerar_dados_normal()

            # Calcular o p-valor para os dados de exemplo
            p_valor_exemplo = calcular_p_valor_normal(dados_exemplo_normal)
            st.write(f"P-valor para os dados de exemplo de distribuição normal: {formatar_p_valor(p_valor_exemplo)}")

            # Gerar e mostrar os gráficos de exemplo
            fig_hist_exemplo = criar_histograma(pd.DataFrame(dados_exemplo_normal, columns=['Normal']), 'Normal')
            st.pyplot(fig_hist_exemplo)
            plt.close(fig_hist_exemplo)

            # Exibir a parte B da conclusão da análise
            conclusao_b = interpretar_resultados_b(p_valor)
            st.write(conclusao_b)
            st.write(f"Explicação do Gráfico Q-Q: O eixo X ({descricao_x_qq}) mostra os quantis teóricos, e o eixo Y ({descricao_y_qq}) os quantis reais dos dados.")

            fig_qq_exemplo = criar_grafico_qq(pd.DataFrame(dados_exemplo_normal, columns=['Normal']), 'Normal')
            st.pyplot(fig_qq_exemplo)
            plt.close(fig_qq_exemplo)# Fechar a figura






# Chamada da função principal
if __name__ == "__main__":
    mostrar_analise_normalidade()
