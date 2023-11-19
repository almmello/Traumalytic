import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from .calculo_analise_normalidade import (
    gerar_dados_normal,
    calcular_p_valor_normal,
    formatar_p_valor,
    interpretar_resultados_a,
    interpretar_resultados_b,
    testar_normalidade,
    criar_histograma,
    criar_grafico_qq
)

# Importar a classe DataLoader do diretório pai
import sys
sys.path.append('..')  # Adiciona o diretório pai ao sys.path
from data_loader import DataLoader

def realizar_teste_normalidade(selected_var):

    # Inicializar o DataLoader
    data_loader = DataLoader()

    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = data_loader.carregar_dados()


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
    realizar_teste_normalidade()
