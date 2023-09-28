import requests
import json

# https://www.geeksforgeeks.org/json-load-in-python/
# Dados em formato JSON que você deseja enviar para a API
f = open('dados.json',) #Abrir JSON
dados_json = json.load(f) #Carregar JSOn

# URL da API
url = 'http://localhost:5000/'  # Certifique-se de que a API esteja em execução e ajuste a URL conforme necessário

# Envia a solicitação POST com os dados JSON
try:
    response = requests.post(url, json=dados_json)

    # Verifica a resposta da API
    if response.status_code == 200:
        print("JSON enviado com sucesso!")
        print("Resposta da API:", json.loads(response.text))
    else:
        print("Erro ao enviar JSON para a API. Código de status:", response.status_code)
except Exception as e:
    print("Erro ao fazer a solicitação para a API:", str(e))
