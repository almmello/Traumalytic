import os
import shutil

def main():
    # Definindo os caminhos de origem e destino
    origem = "C:\\Users\\almme\\Meu Drive\\Pessoas\\Thelma\\Análise de Dados\\modulos\\Criados"
    destino = "C:\\Users\\almme\\Documents\\Github\\Traumalytic\\Development"
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
            shutil.move(item_path, dirModulo, destino)

    print("Arquivos e pastas movidos com sucesso.")

if __name__ == "__main__":
    main()
