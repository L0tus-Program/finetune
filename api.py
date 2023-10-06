from flask import Flask, request, jsonify, abort
from json_to_openai import fine,json_to_l


# Converter JSON em texto
# Dinamico para rodar com todas as linhas disponiveis



# Chave apenas temporaria
API_KEY = 'Messem@2023'

# Outras configurações do aplicativo
DEBUG = True
ENV = 'development'
HOST = 'localhost'
PORT = 5000

# Criando aplicação
app = Flask(__name__)

# Autenticação
def authenticate():
    api_key = request.headers.get('X-API-KEY')
    if api_key != API_KEY:
        return abort(401)
    print("Autenticado")
    return True

# função de autenticação 
@app.route('/', methods=['POST'])
def receber_json():
    if not authenticate():
        return abort(401)

    try:
        dados_json = request.get_json()
        print("Recebendo JSON \nInvocando função fine")
        fine(dados_json)  # Invocando integração OPENAI
        return jsonify({"mensagem": "JSON recebido com sucesso", "dados": dados_json}), 200

    except Exception as e:
        return jsonify({"erro": "Erro ao processar JSON", "mensagem": str(e)}), 400
    

@app.route('/converter', methods=['POST'])

def convertendo_json():
    if not authenticate():
        return abort(401)

    try:
        dados_json = request.get_json()
        print("Recebendo JSON \nInvocando função fine")
        json_to_l(dados_json)  # Invocando integração OPENAI
        return jsonify({"mensagem": "JSON recebido com sucesso", "dados": dados_json}), 200

    except Exception as e:
        return jsonify({"erro": "Erro ao processar JSON", "mensagem": str(e)}), 400

@app.route('/', methods=['GET'])
def enviar_status():
    try:
        return jsonify({"mensagem": "API online.", "GPT": "Status fine - OK"}), 200
    except Exception as e:
        return jsonify({"erro": "Erro ao acessar dados"}), 400

if __name__ == '__main__':
    app.run(debug=True)
