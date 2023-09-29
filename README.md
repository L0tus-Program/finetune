
# API Finetuning ChatGPT

API desenvolvida para treinamento via Finetuning com integração com a Openai.








Versão 1.0 para pequenos testes.

## Variáveis de Ambiente

Caso deseje trabalhar no código deste projeto, serão necessárias as seguintes bibliotecas instaladas:

Flask

Openai


Demais bibliotecas são nativas do Python


## Funcionalidades

Com início de desenvolvimento, estas são as funcionalidades já implementadas:

- Envio de JSONL para o SDK da Openai
- Retorno de status da API
- Formatação de JSON para JSONL para envio ao SDK da Openai

## Uso/Exemplos API


Envio de JSONL já formatado

```python

dados_json = Seu JSONL previamente formatado

# URL da API
url = 'http://localhost:5000/'  # Atualize a URL conforme necessário

# Chave de API (se ainda for necessária)
api_key = 'Sua chave'

# Cabeçalho da solicitação com a chave de API 
headers = {'X-API-KEY': api_key} if api_key else {}

# Envia a solicitação POST com os dados JSON e o cabeçalho (se necessário)
try:
    response = requests.post(url, json=dados_json, headers=headers)

    # Verifica a resposta da API
    if response.status_code == 200:
        print("JSONL enviado com sucesso!")
        print("Resposta da API:", response.json())
    else:
        print("Erro ao enviar JSON para a API. Código de status:", response.status_code)
except Exception as e:
    print("Erro ao fazer a solicitação para a API:", str(e))

}
```


Caso não tenha formatado oo seu JSONL, envie o JSON modificando apenas a URL da api. O JSONL será formatado e enviado a Openai


```python
# URL da API
url = 'http://localhost:5000/converter'  # Atualize a URL conforme necessário

```


Caso queira apenas saber o status da API, envie qualquer metodo GET. Um exemplo de retorno:
```
Resposta da API: {'GPT': 'Status fine - OK', 'mensagem': 'API online.'}

```
