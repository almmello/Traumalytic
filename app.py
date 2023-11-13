import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from calculations import (
    calcular_clusters_ptci, 
    calcular_clusters_pcl5, 
    calcular_estatisticas, 
    calcular_escores_pcl5, 
    calcular_escores_ptci,
    calcular_clusters_ptci_e_retornar,
    calcular_clusters_pcl5_e_retornar,
    calcular_estatisticas_clusters_pcl5,
    calcular_estatisticas_clusters_ptci,
    calcular_distribuicao_por_sexo,
    testar_normalidade,
    criar_histograma,
    criar_grafico_qq,
    gerar_dados_normal,
    calcular_p_valor_normal,
    calcular_correlacao,
    criar_dataframe_para_correlacao,
    criar_dataframe_para_teste_t,
    realizar_teste_t_student
)

def carregar_dados():
    # Carregar dados aqui
    data = pd.read_excel('Banco LEC PCL5 PTCI.xlsx')
    return data

def formatar_p_valor(p_valor):
    return f"{p_valor:.2f}" if p_valor > 0.0001 else f"{p_valor:.2e}"

# Fornece uma interpretação humana e técnica dos resultados do teste de normalidade e dos gráficos.
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

def main():

    st.title("Análise de Dados PTCI e PCL-5")

    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = carregar_dados()

    # Inicializar variável de sessão para armazenar 'data_escores'
    if 'data_escores' not in st.session_state:
        st.session_state['data_escores'] = pd.DataFrame()


    if st.button('Calcular Clusters PTCI'):
        st.session_state['data'] = calcular_clusters_ptci(st.session_state['data'])
        st.write(st.session_state['data'])

    if st.button('Calcular Clusters PCL-5'):
        st.session_state['data'] = calcular_clusters_pcl5(st.session_state['data'])
        st.write(st.session_state['data'])


    if st.button('Calcular Estatísticas de Idade'):
        estatisticas_idade = calcular_estatisticas(st.session_state['data'], 'IDADE')
        st.write('Estatísticas de Idade:', estatisticas_idade)


    if st.button('Calcular Estatísticas do Escore Total PCL-5'):
        estatisticas_pcl5_total = calcular_escores_pcl5(st.session_state['data'])
        st.write('Estatísticas do Escore Total PCL-5:', estatisticas_pcl5_total)


    if st.button('Calcular Estatísticas do Escore Total PTCI'):
        estatisticas_ptci_total = calcular_escores_ptci(st.session_state['data'])
        st.write('Estatísticas do Escore Total PTCI:', estatisticas_ptci_total)

    if st.button('Exibir Clusters PTCI'):
        ptci_clusters = calcular_clusters_ptci_e_retornar(st.session_state['data'])
        st.write(ptci_clusters)

    if st.button('Exibir Clusters PCL-5'):
        pcl5_clusters = calcular_clusters_pcl5_e_retornar(st.session_state['data'])
        st.write(pcl5_clusters)

    if st.button('Calcular Estatísticas dos Clusters PCL-5'):
        estatisticas_clusters_pcl5 = calcular_estatisticas_clusters_pcl5(st.session_state['data'])
        st.write('Estatísticas dos Clusters PCL-5:', estatisticas_clusters_pcl5)

    if st.button('Calcular Estatísticas dos Clusters PTCI'):
        estatisticas_clusters_ptci = calcular_estatisticas_clusters_ptci(st.session_state['data'])
        st.write('Estatísticas dos Clusters PTCI:', estatisticas_clusters_ptci)

    if st.button('Calcular Distribuição por Sexo'):
        distribuicao_sexo = calcular_distribuicao_por_sexo(st.session_state['data'])
        st.write('Distribuição Porcentual por Sexo:', distribuicao_sexo)



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
            st.write(f"Explicação do Histograma: O eixo X ({descricao_x_hist}) representa os valores e o eixo Y ({descricao_y_hist}) a frequência.")

            # Gerar dados de exemplo para uma distribuição normal
            dados_exemplo_normal = gerar_dados_normal()

            # Calcular o p-valor para os dados de exemplo
            p_valor_exemplo = calcular_p_valor_normal(dados_exemplo_normal)
            st.write(f"P-valor para os dados de exemplo de distribuição normal: {formatar_p_valor(p_valor_exemplo)} (menor que 0.05)")
         
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


    # Botão para calcular a correlação entre os escores totais da PCL-5 e PTCI
    if st.button('Correlação entre escores totais da PCL-5 e PTCI'):
        data_correlacao = criar_dataframe_para_correlacao(st.session_state['data'])

        # Calcular correlação entre escores totais
        correlacao_total = calcular_correlacao(data_correlacao['PCL5_total'], data_correlacao['PTCI_total'])
        correlacao_df = pd.DataFrame({'Correlação': [correlacao_total]}, index=['PCL-5 Total vs PTCI Total'])

        # Exibir correlação em uma tabela
        st.table(correlacao_df.round(2))

        # Criar e exibir um gráfico (mapa de calor) para a correlação
        st.subheader('Mapa de Calor da Correlação')
        matriz_correlacao = data_correlacao[['PCL5_total', 'PTCI_total']].corr().round(2)
        sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm')
        st.pyplot(plt)


    # Botão para calcular as correlações entre clusters da PCL-5 e PTCI
    if st.button('Correlações entre clusters da PCL-5 e PTCI'):
        data_correlacao = criar_dataframe_para_correlacao(st.session_state['data'])

        # Preparando a matriz de correlação para clusters
        clusters_pcl5 = ['ClusterB', 'ClusterC', 'ClusterD', 'ClusterE']
        clusters_ptci = ['ClusterA', 'ClusterB', 'ClusterC']
        matriz_correlacao_clusters = np.zeros((len(clusters_ptci), len(clusters_pcl5)))

        # Preenchendo a matriz de correlação
        for i, cluster_ptci in enumerate(clusters_ptci):
            for j, cluster_pcl5 in enumerate(clusters_pcl5):
                matriz_correlacao_clusters[i, j] = calcular_correlacao(data_correlacao[f'PTCI_{cluster_ptci}'], data_correlacao[f'PCL5_{cluster_pcl5}'])

        # Criando a tabela em forma de matriz para clusters
        df_correlacao_clusters = pd.DataFrame(matriz_correlacao_clusters, 
                                              index=[f'PTCI {c}' for c in clusters_ptci], 
                                              columns=[f'PCL-5 {c}' for c in clusters_pcl5])

        # Exibir a tabela de correlação
        st.write('Tabela de Correlações entre Clusters da PCL-5 e PTCI')
        st.dataframe(df_correlacao_clusters.round(2))

        # Criar e exibir um gráfico (mapa de calor) para as correlações entre clusters
        st.subheader('Mapa de Calor das Correlações entre Clusters')
        matriz_correlacao_clusters = data_correlacao[[f'PCL5_{c}' for c in ['ClusterB', 'ClusterC', 'ClusterD', 'ClusterE']] + [f'PTCI_{c}' for c in ['ClusterA', 'ClusterB', 'ClusterC']]].corr().round(2)
        sns.heatmap(matriz_correlacao_clusters, annot=True, cmap='coolwarm')
        st.pyplot(plt)


    # Botão para calcular as correlações entre sintomas da PCL-5 e itens do PTCI
    if st.button('Correlações entre sintomas da PCL-5 e itens do PTCI'):
        data_correlacao = criar_dataframe_para_correlacao(st.session_state['data'])

        # Preparando a matriz de correlação
        num_sintomas_pcl = 20
        num_itens_ptci = 36
        matriz_correlacao = np.zeros((num_itens_ptci, num_sintomas_pcl))

        # Preenchendo a matriz de correlação
        for i in range(num_itens_ptci):
            for j in range(num_sintomas_pcl):
                matriz_correlacao[i, j] = calcular_correlacao(data_correlacao[f'PTCI{i+1:02d}'], data_correlacao[f'PCL{j+1:02d}'])

        # Criando a tabela em forma de matriz
        df_correlacao = pd.DataFrame(matriz_correlacao, 
                                     index=[f'PTCI{i:02d}' for i in range(1, num_itens_ptci + 1)], 
                                     columns=[f'PCL{j:02d}' for j in range(1, num_sintomas_pcl + 1)])

        # Exibir a tabela de correlação
        st.write('Tabela de Correlações entre Sintomas da PCL-5 e Itens do PTCI')
        st.dataframe(df_correlacao.round(2))

        # Preparando dados para o mapa de calor
        num_sintomas_pcl = 20
        num_itens_ptci = 36
        matriz_correlacao = np.zeros((num_sintomas_pcl, num_itens_ptci))

        # Calcular correlações e preencher a matriz
        for i in range(num_sintomas_pcl):
            for j in range(num_itens_ptci):
                matriz_correlacao[i, j] = calcular_correlacao(data_correlacao[f'PCL{i+1:02d}'], data_correlacao[f'PTCI{j+1:02d}'])

        # Criar e exibir um mapa de calor para as correlações
        plt.figure(figsize=(12, 10))
        sns.heatmap(matriz_correlacao, annot=False, cmap='coolwarm', 
                    xticklabels=[f'PTCI{j+1:02d}' for j in range(num_itens_ptci)], 
                    yticklabels=[f'PCL{i+1:02d}' for i in range(num_sintomas_pcl)])
        plt.title('Mapa de Calor das Correlações entre Sintomas da PCL-5 e Itens do PTCI')
        plt.xlabel('Itens do PTCI')
        plt.ylabel('Sintomas da PCL-5')
        st.pyplot(plt)


    # Botão para visualizar o DataFrame limpo
    if st.button('Visualizar DataFrame para Teste t'):
        data_teste_t = criar_dataframe_para_teste_t(st.session_state['data'])

        if not data_teste_t.empty:
            st.write("DataFrame:")
            st.dataframe(data_teste_t)
        else:
            st.error("DataFrame vazio.")




    if st.button('Teste t de Student - Sexo vs Escore Total do PTCI'):
        data_teste_t = criar_dataframe_para_teste_t(st.session_state['data'])

        if 'SEXO' in data_teste_t.columns and 'PTCI_total' in data_teste_t.columns:
            # Realizando o teste t de Student
            t_stat, p_valor = realizar_teste_t_student(data_teste_t, data_teste_t['SEXO'] == 'feminino', data_teste_t['SEXO'] == 'masculino', 'PTCI_total')

            # Exibindo os resultados com interpretação detalhada
            st.write(f"Resultado do Teste t de Student:\nT-Statistic: {t_stat:.2f}, P-valor: {p_valor:.2e}")
            if p_valor < 0.05:
                st.write("Interpretação: Há diferenças estatisticamente significativas nos escores totais do PTCI entre os grupos feminino e masculino. Isso sugere que o sexo pode influenciar os escores do PTCI.")
            else:
                st.write("Interpretação: Não há diferenças estatisticamente significativas nos escores totais do PTCI entre os grupos feminino e masculino. Isso indica que o sexo pode não ter um impacto significativo nos escores do PTCI.")


    if st.button('Teste t de Student - Sexo vs Clusters do PTCI'):
        data_teste_t = criar_dataframe_para_teste_t(st.session_state['data'])

        if 'SEXO' in data_teste_t.columns and all(col in data_teste_t.columns for col in ['PTCI_ClusterA', 'PTCI_ClusterB', 'PTCI_ClusterC']):
            # Realizando o teste t de Student separadamente para cada sexo e cluster
            for cluster in ['ClusterA', 'ClusterB', 'ClusterC']:
                # Teste para o grupo feminino
                t_stat_feminino, p_valor_feminino = realizar_teste_t_student(data_teste_t, data_teste_t['SEXO'] == 'feminino', data_teste_t['SEXO'] != 'feminino', f'PTCI_{cluster}')
                # Exibindo os resultados com interpretação detalhada para feminino
                st.write(f"Resultado do Teste t de Student para PTCI {cluster} (Feminino):\nT-Statistic: {t_stat_feminino:.2f}, P-valor: {p_valor_feminino:.2e}")
                st.write(f"Interpretação para {cluster} (Feminino): {'Diferenças significativas' if p_valor_feminino < 0.05 else 'Não há diferenças significativas'}")
                
                # Teste para o grupo masculino
                t_stat_masculino, p_valor_masculino = realizar_teste_t_student(data_teste_t, data_teste_t['SEXO'] == 'masculino', data_teste_t['SEXO'] != 'masculino', f'PTCI_{cluster}')
                # Exibindo os resultados com interpretação detalhada para masculino
                st.write(f"Resultado do Teste t de Student para PTCI {cluster} (Masculino):\nT-Statistic: {t_stat_masculino:.2f}, P-valor: {p_valor_masculino:.2e}")
                st.write(f"Interpretação para {cluster} (Masculino): {'Diferenças significativas' if p_valor_masculino < 0.05 else 'Não há diferenças significativas'}")
                
                # Espaçamento para melhor legibilidade
                st.write("---")
        else:
            st.error("Os dados necessários ('SEXO', 'PTCI_ClusterA', 'PTCI_ClusterB', 'PTCI_ClusterC') não estão disponíveis no DataFrame.")


if __name__ == "__main__":
    main()
