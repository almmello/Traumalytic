import os
import matplotlib.pyplot as plt
from datetime import datetime

class FigManagement:
    def __init__(self, pasta_temp="fig_temp"):
        self.pasta_temp = pasta_temp
        if not os.path.exists(pasta_temp):
            os.makedirs(pasta_temp)

    def salvar_grafico(self, fig):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"grafico_{timestamp}.png"
        caminho_arquivo = os.path.join(self.pasta_temp, nome_arquivo)

        fig.savefig(caminho_arquivo)
        plt.close(fig)  # Fechar a figura para liberar recursos

        return caminho_arquivo

    def apagar_grafico(self, caminho_arquivo):
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)


