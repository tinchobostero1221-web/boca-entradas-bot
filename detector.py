
import os
import time
import requests
from datetime import datetime

# Configuración
BOCA_URL = "https://bocasocios.bocajuniors.com.ar/matches/878/plateas"
NTFY_TOPIC = "boca-entradas-alertas-2026"

def avisar(mensaje):
    try:
        requests.post(
            f"https://ntfy.sh/{NTFY_TOPIC}",
            data=mensaje.encode("utf-8"),
            headers={"Title": "Boca - Alerta de plateas"}
        )
    except Exception as e:
        print("Error enviando aviso:", e)

def revisar():
    print("Revisando:", datetime.now())
    try:
        respuesta = requests.get(
            BOCA_URL,
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        print("Estado HTTP:", respuesta.status_code)
        print("Tamaño de respuesta:", len(respuesta.text))

        if respuesta.status_code in (401, 403):
            print("La página requiere una sesión iniciada.")
        elif respuesta.status_code == 200:
            print("Página accesible. Falta configurar la sesión para detectar plateas.")
        else:
            print("Respuesta inesperada.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    avisar("El detector de Boca se inició correctamente.")
    while True:
        revisar()
        time.sleep(60)
