
import os
import requests
from datetime import datetime

BOCA_URL = "https://bocasocios.bocajuniors.com.ar/matches/878/plateas"
NTFY_TOPIC = "boca-entradas-alertas-2026"

def avisar(mensaje):
    try:
        requests.post(
            f"https://ntfy.sh/{NTFY_TOPIC}",
            data=mensaje.encode("utf-8"),
            headers={"Title": "Boca - Detector"}
        )
    except Exception as error:
        print("Error de notificación:", error)

def revisar():
    print("Revisión:", datetime.now())
    try:
        respuesta = requests.get(
            BOCA_URL,
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        print("Estado HTTP:", respuesta.status_code)

        if respuesta.status_code == 200:
            print("Página accesible. Hay que verificar la sesión.")
        elif respuesta.status_code in (401, 403):
            print("Se necesita iniciar sesión en Boca.")
        else:
            print("Respuesta inesperada.")

    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    avisar("El detector de Boca está funcionando.")
    revisar()

