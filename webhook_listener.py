from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Obtener datos enviados por el emisor
    data = request.json
    print(f"Data received: {data}")
    
    # Respuesta al emisor
    return jsonify({"status": "success", "message": "Data processed correctly"}), 200

if __name__ == '__main__':
    app.run(port=5000)
