import streamlit as st

from calculations import (
    criar_dataframe_para_teste_t,
    realizar_teste_t_student
)

# Importar a classe DataLoader do diretório pai
import sys
sys.path.append('..')  # Adiciona o diretório pai ao sys.path
from data_loader import DataLoader

def mostrar_teste_t_student():
    st.title("Teste t de Student")

    # Inicializar o DataLoader
    data_loader = DataLoader()

    # Carregar e armazenar os dados no início da sessão
    if 'data' not in st.session_state:
        st.session_state['data'] = data_loader.carregar_dados()

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



# Chamada da função principal
if __name__ == "__main__":
    mostrar_teste_t_student()
