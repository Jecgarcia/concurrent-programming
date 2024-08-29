import time
import threading
import queue
from tqdm import tqdm  # Librería para la barra de progreso
import math

# Definimos los valores para las operaciones
N_PRIMO = 5000
GRAN_NUMERO = 987654321

# Creamos una cola para las tareas
tarea_cola = queue.Queue()

# Función para calcular el n-ésimo número primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def calcular_n_primo(n):
    print(f"\nComenzando el cálculo del {n}-ésimo número primo...\n")
    contador, numero = 0, 1
    while contador < n:
        numero += 1
        if es_primo(numero):
            contador += 1
        time.sleep(0.0001)  # Simula un proceso intensivo y lento
    print(f"\nEl {n}-ésimo número primo es {numero}.\n")

# Función para calcular la raíz cuadrada entera de un número grande
def calcular_raiz_cuadrada_entera(num):
    print(f"\nComenzando el cálculo de la raíz cuadrada entera de {num}...\n")
    raiz = int(math.sqrt(num))
    time.sleep(1)  # Simula un proceso intensivo y lento
    print(f"\nLa raíz cuadrada entera de {num} es {raiz}.\n")

# Función para mostrar la barra de progreso durante el cálculo del número primo
def mostrar_barra_primo():
    for _ in tqdm(range(N_PRIMO), desc="Calculando Primo"):
        time.sleep(0.0001)  # Simula el tiempo para mostrar el progreso

# Función para mostrar la barra de progreso durante el cálculo de la raíz cuadrada
def mostrar_barra_raiz():
    for _ in tqdm(range(100), desc="Calculando Raíz Cuadrada"):
        time.sleep(0.01)  # Simula el tiempo para mostrar el progreso

# Añadimos las tareas a la cola
tarea_cola.put(lambda: calcular_n_primo(N_PRIMO))
tarea_cola.put(mostrar_barra_primo)
tarea_cola.put(lambda: calcular_raiz_cuadrada_entera(GRAN_NUMERO))
tarea_cola.put(mostrar_barra_raiz)

# Función que se encarga de ejecutar tareas desde la cola
def ejecutar_tareas():
    while not tarea_cola.empty():
        tarea = tarea_cola.get()
        tarea()  # Ejecuta la tarea
        tarea_cola.task_done()  # Marca la tarea como completada

# Creamos 4 hilos para ejecutar las 4 tareas concurrentemente
for i in range(4):
    hilo_trabajador = threading.Thread(target=ejecutar_tareas)
    hilo_trabajador.start()

# Esperamos a que todas las tareas terminen
tarea_cola.join()

print("Todas las tareas han terminado.")