import requests
import os
import json
from dotenv import load_dotenv
from tabulate import tabulate

class CheckModels:
    def __init__(self, output_format="table"):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        self.output_format = output_format

    def get_available_models(self):
        response = requests.get("https://api.openai.com/v1/models", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Erro ao acessar a API: {response.status_code}"

    def print_models(self):
        models_data = self.get_available_models()
        if 'data' in models_data:
            # Ordenando os modelos pelo ID
            sorted_models = sorted(models_data['data'], key=lambda x: x['id'])

            if self.output_format == "table":
                table = [[model['id'], model['created'], model['owned_by']] for model in sorted_models]
                print(tabulate(table, headers=["ID", "Created", "Owned By"]))
            elif self.output_format == "json":
                sorted_data = {'object': models_data['object'], 'data': sorted_models}
                print(json.dumps(sorted_data, indent=4))
        else:
            print(models_data)

# Configuração da variável de formato de saída
output_format = "table"  # Opções: "table" ou "json"

# Exemplo de uso
model_checker = CheckModels(output_format)
model_checker.print_models()
