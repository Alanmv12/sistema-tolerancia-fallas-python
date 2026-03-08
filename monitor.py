import subprocess
import time
import logging
import os
import signal
import sys

# obtener ruta de la carpeta del script
ruta_actual = os.path.dirname(os.path.abspath(__file__))

ruta_servicio = os.path.join(ruta_actual, "servicio.py")
ruta_log = os.path.join(ruta_actual, "monitor.log")

logging.basicConfig(
    filename=ruta_log,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

proceso = None


def iniciar_servicio():
    global proceso
    logging.info("Iniciando servicio principal")

    proceso = subprocess.Popen(
        ["python", ruta_servicio],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def detener_monitor(signal_recibida, frame):
    logging.info("Monitor detenido manualmente")

    if proceso and proceso.poll() is None:
        proceso.terminate()
        logging.info("Servicio terminado por el monitor")

    sys.exit(0)


signal.signal(signal.SIGINT, detener_monitor)
signal.signal(signal.SIGTERM, detener_monitor)


def monitor():
    iniciar_servicio()

    while True:
        time.sleep(5)

        if proceso.poll() is None:
            logging.info("Servicio funcionando correctamente")
        else:
            logging.warning("Servicio detenido inesperadamente. Reiniciando...")
            iniciar_servicio()


if __name__ == "__main__":
    logging.info("Monitor iniciado")
    monitor()