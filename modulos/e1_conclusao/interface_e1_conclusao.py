import streamlit as st

# Importações absolutas baseadas na estrutura do projeto
from modulos.e1_conclusao.processo_e1_conclusao import (
    processar_e1_conclusao
)

from modulos.e1_conclusao.conteudo_e1_conclusao import (
    explicar_e1_conclusao
)

def mostrar_e1_conclusao():
    st.title("Conclusão Etapa 1")

    # Lista de variáveis necessárias
    variaveis_necessarias = ['cod_a', 'cod_b', 'data_a', 'data_b', 'data_resumo_a', 'data_resumo_b']
    variaveis_faltantes = [var for var in variaveis_necessarias if var not in st.session_state]

    # Verificar se todas as variáveis necessárias estão presentes
    if variaveis_faltantes:
        # Exibir as variáveis faltantes e solicitar a execução das etapas anteriores
        st.error("As seguintes variáveis de sessão estão faltando: " + ", ".join(variaveis_faltantes))
        st.markdown("Por favor, execute as etapas anteriores para gerar essas variáveis.")
    else:
        # Se todas as variáveis estiverem presentes, prosseguir com a conclusão da Etapa 1
        explicar_e1_conclusao()
        processar_e1_conclusao()

# Chamada da função principal
if __name__ == "__main__":
    mostrar_e1_conclusao()
