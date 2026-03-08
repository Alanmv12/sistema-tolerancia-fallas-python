# Sistema Tolerante a Fallas en Python

Proyecto desarrollado para la materia **Computación Tolerante a Fallas**.

## Problema a resolver

En muchos sistemas informáticos los servicios pueden fallar inesperadamente debido a errores del sistema, excepciones o problemas de memoria.  
Cuando esto ocurre, el sistema puede dejar de funcionar completamente.

## Ejecución en segundo plano

Para solucionar este problema se implementa un proceso monitor que se ejecuta en segundo plano y revisa constantemente el estado del servicio principal.

## Tipo de falla

El servicio principal puede fallar debido a errores simulados dentro del programa.  
Cuando esto ocurre, el proceso termina inesperadamente.

## Estrategia de tolerancia a fallas

Se utiliza un **proceso monitor** que detecta cuando el servicio principal deja de ejecutarse.

Si el monitor detecta que el proceso se detuvo:

1. Registra el evento en un archivo log
2. Reinicia automáticamente el servicio

## Estructura del proyecto

monitor.py  
Proceso que monitorea el servicio principal.

servicio.py  
Aplicación que simula una tarea continua y puede fallar.

## Cómo ejecutar el proyecto

Ejecutar el monitor:


El monitor iniciará el servicio y lo reiniciará automáticamente si falla.

## Tecnologías utilizadas

- Python
- subprocess
- logging

## Autor

Alan Lorenzo Muro Villegas  
Ingeniería en Computación  
Universidad de Guadalajara