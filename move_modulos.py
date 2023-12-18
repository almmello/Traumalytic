import os
import shutil
from dotenv import load_dotenv

def main():
    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()

    # Definir ambiente atual
    ambienteAtual = "Mac"  # Mude para "Mac" caso esteja no Macintosh

    # Definindo os caminhos de origem e destino com base no ambiente
    if ambienteAtual == "Mac":
        origem = os.getenv("origemMac")
        destino = os.getenv("destinoMac")
    else:
        origem = os.getenv("origemWin")
        destino = os.getenv("destinoWin")
    
    dirModulo = "modulos"

    # Apagar o arquivo sidemenu.py no destino, se existir, e mover o novo
    sidemenu_destino = os.path.join(destino, "sidemenu.py")
    if os.path.exists(sidemenu_destino):
        os.remove(sidemenu_destino)

    sidemenu_origem = os.path.join(origem, "sidemenu.py")
    if os.path.exists(sidemenu_origem):
        shutil.move(sidemenu_origem, sidemenu_destino)

    # Verificar se alguma pasta em origem já existe em destino
    for item in os.listdir(origem):
        item_path = os.path.join(origem, item)
        destino_path = os.path.join(destino, dirModulo, item)
        if os.path.isdir(item_path) and os.path.exists(destino_path):
            print(f"A pasta '{item}' já existe no destino. Processo interrompido.")
            return

    # Mover todas as pastas restantes de origem para destino
    for item in os.listdir(origem):
        item_path = os.path.join(origem, item)
        if os.path.isdir(item_path):
            shutil.move(item_path, os.path.join(destino, dirModulo))

    print("Arquivos e pastas movidos com sucesso.")

if __name__ == "__main__":
    main()
