import json
import requests

# Carregue os dados JSON do arquivo
with open('dados.json') as json_file:
    dados_json = json.load(json_file)

# URL da API
url = 'http://localhost:5000/'  # Atualize a URL conforme necessário

# Chave de API (se ainda for necessária)
api_key = 'Messem@2023'

# Cabeçalho da solicitação com a chave de API (se ainda for necessária)
headers = {'X-API-KEY': api_key} if api_key else {}

# Envia a solicitação POST com os dados JSON e o cabeçalho (se necessário)
try:
    #jsonl = json.dumps(dados_json)
    response = requests.post(url, json=dados_json, headers=headers)

    # Verifica a resposta da API
    if response.status_code == 200:
        print("JSON enviado com sucesso!")
        print("Resposta da API:", response.json())
    else:
        print("Erro ao enviar JSON para a API. Código de status:", response.status_code)
except Exception as e:
    print("Erro ao fazer a solicitação para a API:", str(e))
