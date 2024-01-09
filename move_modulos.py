import os
import shutil
from dotenv import load_dotenv

def main():
    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()

    # Definir se inclui a copia do menu
    incluiMenu = False

    # Definir ambiente atual
    ambienteAtual = "Mac"  # Mude para "Mac" caso esteja no Macintosh

    # Definindo os caminhos de origem e destino com base no ambiente
    if ambienteAtual == "PC":
        origem = os.getenv("origemMac")
        destino = os.getenv("destinoMac")
    else:
        origem = os.getenv("origemWin")
        destino = os.getenv("destinoWin")
    
    dirModulo = "modulos"

    # Verificar se move o menu
    if incluiMenu:
        # Verificar e mover o arquivo sidemenu.py, se existir
        sidemenu_origem = os.path.join(origem, "sidemenu.py")
        sidemenu_destino = os.path.join(destino, "sidemenu.py")
        if os.path.exists(sidemenu_origem):
            if os.path.exists(sidemenu_destino):
                os.remove(sidemenu_destino)
            shutil.move(sidemenu_origem, sidemenu_destino)
            print("Arquivo sidemenu.py movido com sucesso.")
        else:
            print("Arquivo sidemenu.py não encontrado na origem.")

    # Verificar se existem pastas na origem
    if any(os.path.isdir(os.path.join(origem, item)) for item in os.listdir(origem)):
        # Verificar e mover pastas
        for item in os.listdir(origem):
            item_path = os.path.join(origem, item)
            destino_path = os.path.join(destino, dirModulo, item)
            if os.path.isdir(item_path):
                if os.path.exists(destino_path):
                    print(f"A pasta '{item}' já existe no destino. Não será movida.")
                else:
                    shutil.move(item_path, destino_path)
                    print(f"Pasta '{item}' movida com sucesso.")
    else:
        print("Nenhuma pasta encontrada na origem para ser movida.")

if __name__ == "__main__":
    main()

