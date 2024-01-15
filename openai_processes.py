# Importações necessárias
from openai_parser import OpenAIInterface
from supabase_manager import SupabaseManager
from fig_management import FigManagement
import streamlit as st
import os
import logging

# Obter um logger para o módulo atual
logger = logging.getLogger(__name__)

# Ajustar o nível do logger para DEBUG
logger.setLevel(logging.DEBUG)

def carregar_conclusoes(analysis_id, etapa_analise, nome_analise, resultados=None, instrucoes=None):

    supabase_manager = SupabaseManager()
    conclusoes_existentes = supabase_manager.recuperar_conclusoes(analysis_id)

    # Filtrar conclusões que não são do tipo "resultado"
    conclusoes_existentes = [conclusion for conclusion in conclusoes_existentes if conclusion['type'] != 'resultado']

    # Verificar se existem conclusões anteriores
    if not conclusoes_existentes:
        # Gerar e inserir a primeira conclusão se não existir
        nova_conclusao = gerar_conclusao(analysis_id, etapa_analise, instrucoes, resultados)
        st.subheader(f"Nova Conclusão: {nome_analise}")
        st.markdown(nova_conclusao)
    else:
        # Exibir o histórico de chat existente
        chat_history = sorted(
            conclusoes_existentes,
            key=lambda x: x['created_at']
        )
        contador = 1
        for message in chat_history:
            if message['type'] == 'resposta':
                
                st.subheader(f'Conclusão {contador:02d}')                
            elif message['type'] == 'comentario':
                contador -= 1
                st.subheader(f'Comentário {contador:02d}')
            
            st.markdown(message['conclusion'])
            contador += 1

    # Caixa de texto e botão para comentários
    comentario = st.text_area("Faça comentários sobre a conclusão de forma que possa ser atualizada:", key=f"comment_{analysis_id}_{st.session_state['reset_counter']}")
    if st.button('Enviar Comentário', key=f"send_comment_{analysis_id}_{st.session_state['reset_counter']}"):
        gerar_nova_conclusao(analysis_id, etapa_analise, comentario, resultados=None, instrucoes=None)
        st.session_state['reset_counter'] += 1

        st.rerun()

def gravar_resultados(analysis_id, etapa_analise, resultados_texto):
    supabase_manager = SupabaseManager()
    resultado = supabase_manager.inserir_conclusao(analysis_id, etapa_analise, 'resultado', resultados_texto, 'ativa')
    # Verificar se a operação foi bem-sucedida
    if resultado:
        return True
    else:
        return False

def gerar_conclusao(analysis_id, etapa_analise, instrucoes, resultados):
    openai_interface = OpenAIInterface()

    response = openai_interface.criar_conclusao(instrucoes, resultados)
    texto_conclusao = response.content

    supabase_manager = SupabaseManager()
    supabase_manager.inserir_conclusao(analysis_id, etapa_analise, 'resposta', texto_conclusao, 'ativa')

    return texto_conclusao

def gerar_nova_conclusao(analysis_id, etapa_analise, comentario, resultados=None, instrucoes=None):
    supabase_manager = SupabaseManager()
    openai_interface = OpenAIInterface()

    logger.debug("\nIniciando a geração de nova conclusão para a análise ID:", analysis_id, "\n")

    # Recuperar todas as conclusões existentes para a análise
    conclusoes_existentes = supabase_manager.recuperar_conclusoes(analysis_id)
    logger.debug("\nConclusões existentes recuperadas:", conclusoes_existentes, "\n")

    # Solicitar à OpenAI para processar o chat e fornecer uma conclusão atualizada
    response = openai_interface.criar_conclusao(instrucoes, resultados, comentario, conclusoes_existentes)  # "" representa instrucoes e resultados vazios
    updated_conclusion = response.content
    logger.debug("\nResposta da OpenAI recebida:", updated_conclusion, "\n")

    # Inserir o novo comentário e a conclusão atualizada no banco de dados
    supabase_manager.inserir_conclusao(analysis_id, etapa_analise, 'comentario', comentario, 'ativa')
    logger.debug("\nNovo comentário inserido no banco de dados para a análise ID:", analysis_id, "\n")

    supabase_manager.inserir_conclusao(analysis_id, etapa_analise, 'resposta', updated_conclusion, 'ativa')
    logger.debug("\nConclusão atualizada inserida no banco de dados para a análise ID:", analysis_id, "\n")

    return updated_conclusion

def processar_visao_imagem(figura, prompt_text):

    fig_manager = FigManagement()
    openai_interface = OpenAIInterface()

    # Salvar e converter a figura em base64
    caminho_figura = fig_manager.salvar_grafico(figura)
    imagem_base64 = openai_interface.encode_image_to_base64(caminho_figura)
    descricao = openai_interface.descrever_imagem_base64(imagem_base64, prompt_text)
    fig_manager.apagar_grafico(caminho_figura)

    logger.debug(f"Descrição da Imagem ({prompt_text}):", descricao)

    return descricao

def processar_conclusoes_imagem(analysis_id, etapa_analise, fig, prompt_plot, nome_analise, instrucoes):
    supabase_manager = SupabaseManager()
    conclusoes_existentes = supabase_manager.recuperar_conclusoes(analysis_id)

    if not conclusoes_existentes:
        descricao_plot = processar_visao_imagem(fig, prompt_plot)
        resultados = f"Resultados {nome_analise}: {descricao_plot}"

        logger.debug("\nTexto para Geração de Conclusões: ", resultados, "\n")

        gravacao_bem_sucedida = gravar_resultados(analysis_id, etapa_analise, resultados)

        logger.debug("\nRetorno Gravação: ", gravacao_bem_sucedida, "\n")

        if gravacao_bem_sucedida:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)

    else:
        resultados = supabase_manager.recuperar_conclusoes(analysis_id)
        
        if resultados:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)



def processar_conclusoes_tabela(analysis_id, tabela_resultados, nome_analise, instrucoes):
    supabase_manager = SupabaseManager()
    conclusoes_existentes = supabase_manager.recuperar_conclusoes(analysis_id)

    if not conclusoes_existentes:
        # Formatar os resultados agrupados para texto
        texto_resultados = formatar_resultados_para_texto(tabela_resultados)
        resultados= f"Resultados {nome_analise}: {texto_resultados}"

        logger.debug("\nTexto para Geração de Conclusões: ", resultados, "\n")

        # Gravar os resultados formatados
        gravacao_bem_sucedida = gravar_resultados(analysis_id, resultados)

        logger.debug("\nRetorno Gravação: ", gravacao_bem_sucedida, "\n")

        if gravacao_bem_sucedida:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)

    else:
        # Carregar conclusões existentes sem gerar novas descrições
        resultados = supabase_manager.recuperar_conclusoes(analysis_id)

        if resultados:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)

# Função auxiliar para formatar resultados para texto
def formatar_resultados_para_texto(tabela_resultados):
    texto = ""
    for coluna, estatisticas in tabela_resultados.items():
        texto += f"Valores na coluna '{coluna}':\n"
        texto += estatisticas.to_string() + "\n\n"
    return texto


def processar_conclusoes_texto(analysis_id, etapa_analise, texto_resultados, nome_analise, instrucoes):
    supabase_manager = SupabaseManager()
    conclusoes_existentes = supabase_manager.recuperar_conclusoes(analysis_id)

    if not conclusoes_existentes:
        # Preparar o texto dos resultados
        resultados = f"Resultados {nome_analise}: {texto_resultados}"

        logger.debug("\nTexto para Geração de Conclusões: ", resultados, "\n")

        # Gravar os resultados formatados
        gravacao_bem_sucedida = gravar_resultados(analysis_id, etapa_analise, resultados)

        logger.debug("\nRetorno Gravação: ", gravacao_bem_sucedida, "\n")

        if gravacao_bem_sucedida:
            carregar_conclusoes(analysis_id, etapa_analise, nome_analise, resultados, instrucoes)

    else:
        # Carregar conclusões existentes sem gerar novas descrições
        resultados = supabase_manager.recuperar_conclusoes(analysis_id)

        if resultados:
            carregar_conclusoes(analysis_id, nome_analise, resultados, instrucoes)


def processar_resultados(analysis_id):
    supabase_manager = SupabaseManager()
    resultado = supabase_manager.recuperar_resultado(analysis_id)

    if resultado:
        # Exibir resultados em um bloco de texto grande
        resultado_atual = st.text_area("Resultados", resultado, key=f"resultados_{analysis_id}")

        # Botão para atualizar resultados
        if st.button("Atualizar Resultados", key=f"atualizar_{analysis_id}"):
            supabase_manager.atualizar_resultado(analysis_id, resultado_atual)
            st.rerun()

    else:
        # Não existem resultados no Supabase, então exibir os resultados das variáveis de estado
        if 'resultados_calculados' in st.session_state:
            resultado_atual = st.text_area("Resultados", st.session_state['resultados_calculados'], key=f"resultados_{analysis_id}")

            # Botão para atualizar resultados
            if st.button("Atualizar Resultados", key=f"atualizar_{analysis_id}"):
                supabase_manager.atualizar_resultado(analysis_id, resultado_atual)
                st.rerun()



def processar_resumo(analysis_id, etapa_analise, nome_analise):
    supabase_manager = SupabaseManager()
    logger.debug(f"Recuperando resumo para analysis_id: {analysis_id}")
    resumo = supabase_manager.recuperar_resumo(analysis_id)
    logger.debug(f"Resumo recuperado: {resumo}")

    if resumo:
        logger.debug("Resumo encontrado no Supabase.")
        resumo_atual = st.text_area("Resumo", resumo, height=300, key=f"resumo_{analysis_id}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Atualizar Resumo", key=f"atualizar_resumo_{analysis_id}"):
                logger.debug("Atualizando resumo no Supabase.")
                supabase_manager.atualizar_resumo(analysis_id, resumo_atual)
                st.rerun()
        with col2:
            if st.button("Apagar Resumo", key=f"apagar_resumo_{analysis_id}"):
                logger.debug("Apagando resumo no Supabase.")
                supabase_manager.apagar_resumo(analysis_id)
                st.rerun()
    else:
        openai_interface = OpenAIInterface()
        logger.debug("Resumo não encontrado.")
        if st.button("Gerar Resumo", key=f"gerar_resumo_{analysis_id}"):
            logger.debug("Gerando novo resumo com OpenAI.")
            historico_conclusoes = supabase_manager.recuperar_conclusoes(analysis_id)
            resultado_atual = supabase_manager.recuperar_resultado(analysis_id)

            novo_resumo = openai_interface.criar_resumo(nome_analise, resultado_atual, historico_conclusoes)
            if novo_resumo:
                logger.debug("Resumo gerado com sucesso.")
                supabase_manager.inserir_conclusao(analysis_id, etapa_analise, "resumo", novo_resumo, "ativa")
                resumo_atual = st.text_area("Resumo", novo_resumo, height=300, key=f"resumo_{analysis_id}")
                logger.debug(f"Resumo atual do texto: {resumo_atual}")

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Atualizar Resumo", key=f"atualizar_resumo_{analysis_id}"):
                        logger.debug("Atualizando resumo no Supabase.")
                        supabase_manager.atualizar_resumo(analysis_id, resumo_atual)
                        st.rerun()
                with col2:
                    if st.button("Apagar Resumo", key=f"apagar_resumo_{analysis_id}"):
                        logger.debug("Apagando resumo no Supabase.")
                        supabase_manager.apagar_resumo(analysis_id)
                        st.rerun()
            else:
                logger.debug("Falha ao gerar o novo resumo.")
                st.error("Não foi possível gerar um novo resumo. Tente novamente mais tarde.")


    
