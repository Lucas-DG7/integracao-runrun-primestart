from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receber_evento():
    evento = request.get_json(silent=True)

    if not evento:
        return jsonify({"error": "Requisição inválida, JSON não encontrado"}), 400

    print("📩 Evento recebido do Runrun.it:")
    print(json.dumps(evento, indent=2))
    
    # Aqui você pode adicionar lógica para tratar o evento, ex:
    # enviar_para_prime_start(evento)

    return jsonify({"status": "Evento processado com sucesso"}), 200
