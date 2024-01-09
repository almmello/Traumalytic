import streamlit as st
import importlib
import csv
import os
from data_loader import DataLoader

from app_interface import mostrar_conteudo as mostrar_home

def ler_menu_map_csv():
    diretorio_base = "C:\\Users\\almme\\Documents\\Github\\Traumalytic\\Production"
    arquivo_csv = os.path.join(diretorio_base, "sidemenu_mapping.csv")

    menu_map = {}
    with open(arquivo_csv, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)  # Pular cabeçalho

        for linha in csv_reader:
            tipo_analise, analise, id_modulo = linha
            id_modulo = id_modulo.strip()
            modulo = f"{id_modulo}.interface_{id_modulo}"
            funcao = f"mostrar_{id_modulo}"

            if tipo_analise not in menu_map:
                menu_map[tipo_analise] = {}

            menu_map[tipo_analise][analise] = (modulo, funcao)

    return menu_map

def importar_funcao(modulo, funcao):
    modulo_importado = importlib.import_module(f"modulos.{modulo}")
    return getattr(modulo_importado, funcao)

def create_fixed_buttons():
    if st.sidebar.button("Home", key="btn_home"):
        st.session_state['pagina_atual'] = 'home'

def handle_fixed_button_actions():
    if st.session_state.get('pagina_atual') == 'home':
        mostrar_home()

def create_sidebar():
    st.sidebar.title("Traumalytics")

    # Cria e inicializa a instância de DataLoader
    data_loader = DataLoader()

    # Botões fixos
    create_fixed_buttons()

    # Lê o mapeamento do menu a partir do CSV
    menu_map = ler_menu_map_csv()

    #pagina_atual = st.session_state.get('pagina_atual')

    for tipo_analise, paginas in menu_map.items():
        st.sidebar.markdown(f"## {tipo_analise}")
        for pagina, (modulo, funcao_nome) in paginas.items():
            # Gerar uma chave única para cada botão
            button_key = f"{tipo_analise}_{pagina}".replace(' ', '_').lower()
            if st.sidebar.button(pagina, key=button_key):
                st.session_state['pagina_atual'] = (modulo, funcao_nome)

    # Exibição de Conteúdo Baseado na Página Atual
    handle_fixed_button_actions()
    if st.session_state.get('pagina_atual') and st.session_state['pagina_atual'] not in ['home', 'configuracoes']:
        funcao_mostrar = importar_funcao(*st.session_state['pagina_atual'])
        funcao_mostrar()

