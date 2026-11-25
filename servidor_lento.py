import time
from flask import Flask, jsonify

app = Flask(__name__)


# No usa hilos concurrentes avanzados y hace un cálculo pesado que satura la CPU
@app.route('/api/proceso', methods=['GET'])
def proceso_sin_optimizar():

    contador = 0
    for i in range(1000000):
        contador += i
        
    time.sleep(0.2)
    
    return jsonify({
        "estado": "exitoso",
        "mensaje": "Peticion procesada sin optimizacion"
    })

if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=5000, threaded=False)