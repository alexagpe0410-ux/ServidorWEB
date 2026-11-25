import time
from flask import Flask, jsonify
from waitress import serve

app = Flask(__name__)

@app.route('/api/proceso', methods=['GET'])
def proceso_lento():
  
    time.sleep(0.05)
    
    return jsonify({
        "estado": "exitoso",
        "mensaje": "¡Peticion atendida correctamente!"
    })

if __name__ == '__main__':
    print("Iniciando servidor robusto con Waitress en el puerto 5000...")
    serve(app, host='127.0.0.1', port=5000, threads=100)