import time
import random
import signal
import sys
import logging
import os

ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_log = os.path.join(ruta_actual, "servicio.log")

logging.basicConfig(
    filename=ruta_log,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def manejar_cierre(signal, frame):
    logging.info("Servicio recibió señal de cierre")
    sys.exit(0)

signal.signal(signal.SIGINT, manejar_cierre)
signal.signal(signal.SIGTERM, manejar_cierre)

logging.info("Servicio principal iniciado")

while True:
    print("Servicio trabajando...")
    logging.info("Ejecutando tarea")

    time.sleep(4)

    if random.randint(1,12) == 6:
        logging.error("Falla crítica simulada")
        raise Exception("Crash simulado")