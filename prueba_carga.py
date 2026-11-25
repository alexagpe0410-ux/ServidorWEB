import concurrent.futures
import time
import requests

URL = "http://127.0.0.1:5000/api/proceso"

def hacer_peticion(_):
    inicio = time.time()
    try:
        response = requests.get(URL)
        fin = time.time()
        if response.status_code == 200:
            return (fin - inicio) * 1000  
        pass
    return None

def probar_carga(usuarios_concurrentes):
    print(f"\n--- Probando con {usuarios_concurrentes} usuarios concurrentes ---")
    inicio_total = time.time()
    
    # Usamos múltiples "hilos" para simular usuarios al mismo tiempo
    with concurrent.futures.ThreadPoolExecutor(max_workers=usuarios_concurrentes) as executor:
        resultados = list(executor.map(hacer_peticion, range(usuarios_concurrentes)))
    
    fin_total = time.time()
    

    tiempos_exitosos = [t for t in resultados if t is not None]
    
    if tiempos_exitosos:
        latencia_promedio = sum(tiempos_exitosos) / len(tiempos_exitosos)
        print(f"Latencia promedio: {latencia_promedio:.2f} ms")
        print(f"Tiempo total de la prueba: {(fin_total - inicio_total):.2f} segundos")
        return latencia_promedio
    else:
        print("El servidor colapsó o no respondió.")
        return None

if __name__ == "__main__":
    niveles_carga = [10, 50, 100, 200, 300]
    
    print("Iniciando pruebas de estrés para el Cálculo Diferencial...")
    for n in niveles_carga:
        probar_carga(n)
        time.sleep(1)