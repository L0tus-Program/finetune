from flask import Flask, request, jsonify
from main import fine
app = Flask(__name__)

@app.route('/', methods=['POST'])
def receber_json():
    try:
        dados_json = request.get_json()
        print("Recebendo JSON \nInvocando funcao fine")
        fine(dados_json) #invocando integração OPENAI
        return jsonify({"mensagem": "JSON recebido com sucesso", "dados": dados_json}), 200
        
        
    except Exception as e:
        return jsonify({"erro": "Erro ao processar JSON", "mensagem": str(e)}), 400
    
@app.route('/', methods=['GET']) 
def enviar_status():
    try:
        return jsonify({"mensagem": "API online.","GPT": "Status fine -"}),200
    except Exception as e:
        return jsonify({"erro": "Erro ao acessar dados"}),400

if __name__ == '__main__':
    app.run(debug=True)