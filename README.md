# concurrent-programming
# Programación Concurrente

## Definición y Fundamentos
- **Concurrencia**: Ejecución simultánea de múltiples tareas. Permite que tareas independientes se ejecuten en paralelo sin necesidad de que unas dependan de la finalización de otras.
- **Exclusión Mutua**: Mecanismo para asegurar que solo una tarea acceda a un recurso compartido a la vez, utilizando técnicas como locks, mutexes y semáforos.
  - **Problemas Clásicos**:
    - **The Dining Philosophers**: Ejemplo de sincronización y exclusión mutua para evitar condiciones de carrera y deadlock.
    - **The Sleeping Barber**: Ejemplo que ilustra la sincronización entre un barbero y sus clientes.
    - **The Dutch Flag Problem**: Ejemplo de particionamiento de datos en sistemas concurrentes.
- **Computación Distribuida**: Coordinación de sistemas independientes para resolver problemas, enfrentando desafíos de exclusión mutua y sincronización a través de redes.

## Concurrencia vs. Paralelismo
- **Concurrencia**: Manejo de múltiples tareas que pueden estar en progreso, pero no necesariamente ejecutándose al mismo tiempo.
- **Paralelismo**: Ejecución simultánea de múltiples tareas, aprovechando hardware con múltiples núcleos o procesadores.
  - **Ejemplo de Concurrencia**: Un solo barista en una cafetería que maneja múltiples pedidos de forma alternada.
  - **Ejemplo de Paralelismo**: Múltiples baristas atendiendo a clientes simultáneamente.

## Procesos vs. Hilos
- **Procesos**: Unidades independientes con su propio espacio de memoria.
- **Hilos**: Unidades dentro de un proceso que comparten el mismo espacio de memoria.

## Importancia de la Programación Concurrente
- **Ganancia de Procesamiento**: Utiliza hardware multiprocesador o computadoras múltiples para mejorar la capacidad de cómputo.
- **Incremento del Throughput**: Mejora la cantidad de trabajo procesado en un tiempo determinado.
- **Mejora de Respuesta de Aplicaciones**: Permite aplicaciones más responsivas al usuario.
- **Manejo de Múltiples Eventos**: Ideal para controlar diversas actividades y eventos simultáneamente.
- **Soporte para Sistemas Distribuidos**: Facilita la coordinación en sistemas con múltiples dispositivos.

## Historia y Evolución
### Orígenes y Primeros Avances
- **1961**: Multiprogramación en el ordenador Atlas introduce la simulación de concurrencia.
- **1965**: Edsger Dijkstra identifica la exclusión mutua y presenta problemas como "The Dining Philosophers."
- **1967**: Publicación del artículo de Dijkstra que introduce conceptos clave y semáforos.

### Desarrollo en los Años 70 y 80
- **Década de 1970**: Inicios de la computación distribuida con técnicas de redundancia modular.
- **1973**: Proyecto SIFT destaca la tolerancia a fallos.
- **Finales de los 70 y 80**: ARPANET y sistemas de tiempo compartido revolucionan el acceso a recursos computacionales.

### Avances en Lenguajes y Modelos de Concurrencia
- **Años 80 y 90**: Introducción de lenguajes y modelos como Erlang, Ada, y modelos CSP y de actores para manejar la concurrencia.

### Era de los Multiprocesadores y Desafíos Modernos
- **Actualidad**: La programación concurrente es esencial para sistemas multiprocesador y el manejo de aplicaciones complejas. Tecnologías como OpenMP y MPI, y bibliotecas como `concurrent.futures` y `asyncio` en Python son relevantes.

## Casos de Uso
1. Aplicaciones de Servidor: Manejo de múltiples solicitudes simultáneamente.
2. Procesamiento en Paralelo: Dividir tareas en sub-tareas para procesar grandes volúmenes de datos.
3. Interfaces de Usuario Responsivas: Mantener la interfaz fluida mientras se realizan tareas en segundo plano.
4. Simulaciones y Juegos: Manejo de múltiples entidades y eventos.
5. Procesamiento de Eventos: Gestión eficiente de eventos sin bloquear el sistema.
6. Computación Distribuida: Coordinación de tareas en clústeres de servidores o en la nube.
7. Aplicaciones en Tiempo Real: Respuesta rápida en sistemas críticos.
8. Desarrollo de Sistemas Operativos: Gestión de procesos y hilos del sistema.
9. Procesamiento Multimedia: Manejo simultáneo de tareas como renderizado y sincronización.
10. Cálculos Científicos y Simulaciones: Ejecución rápida de simulaciones complejas.

## Lenguajes de Programación Asociados
- **Erlang**: Diseñado para sistemas concurrentes y distribuidos, ideal para alta disponibilidad y escalabilidad.
- **ADA**: Enfocado en sistemas críticos y tiempo real, con robustez en la concurrencia.
- **Concurrent Pascal**: Diseñado para facilitar la programación concurrente y la enseñanza de conceptos relacionados.
- **C++**: Permite implementar aplicaciones paralelas utilizando hilos para manejar procesos ligeros.

## Parte Práctica: Implementación de un Ejemplo
Implementación de un ejemplo práctico de programación concurrente para ilustrar conceptos teóricos.

## Desafíos y Consideraciones
- **Retos**: Manejo de la naturaleza no determinista, condiciones de carrera, bloqueos muertos, programación inadecuada de hilos, y fallos en la comunicación.

## Comparación con Otros Paradigmas
- **Programación Secuencial**: Más simple, pero no eficiente para hardware moderno.
- **Programación Paralela**: Enfocada en la ejecución simultánea de tareas en múltiples núcleos.
- **Programación Distribuida**: Maneja tareas a través de sistemas distribuidos, con herramientas como Apache Hadoop.
- **Programación Asíncrona**: Ideal para operaciones no bloqueantes, con herramientas como `asyncio` en Python.
- **Programación Funcional**: Utiliza abstracciones para manejar la concurrencia de manera natural, aunque Python requiere gestión explícita del estado compartido.

## Instrucciones para Ejecutar el Código
Este código en Python implementa un sistema de ejecución concurrente de tareas utilizando hilos (threads) y una cola (queue) para gestionar estas tareas. Además, utiliza la librería `tqdm` para mostrar barras de progreso durante la ejecución de algunas de las tareas.

### Importación de Módulos
- `time`: Para manejar el tiempo, como agregar retrasos artificiales.
- `threading`: Para crear y manejar hilos de ejecución.
- `queue`: Para crear una cola de tareas, donde se almacenan las tareas que los hilos ejecutarán.
- `tqdm`: Para mostrar barras de progreso en la terminal.
- `math`: Para realizar operaciones matemáticas, como el cálculo de la raíz cuadrada.

### Definición de Constantes
- `N_PRIMO`: Es el número del primo que se va a calcular (el primo número 5000).
- `GRAN_NUMERO`: Es el número del que se va a calcular la raíz cuadrada entera.

### Creación de Cola de Tareas
Se crea una cola de tareas (`tarea_cola`) donde se almacenarán las funciones que los hilos ejecutarán.

### Funciones
1. **`es_primo(num)`**: Determina si un número es primo.
   - Verifica si `num` es divisible por algún número menor o igual a la raíz cuadrada de `num`.
   
2. **`calcular_n_primo(n)`**: Calcula el n-ésimo número primo (en este caso, el primo número 5000).
   - Utiliza la función `es_primo` para verificar si un número es primo y aumenta el contador hasta alcanzar el n-ésimo primo.
   - `time.sleep(0.0001)` introduce un pequeño retraso para simular una operación intensiva.

3. **`calcular_raiz_cuadrada_entera(num)`**: Calcula la raíz cuadrada entera de un número grande (en este caso, 987654321).
   - El cálculo de la raíz cuadrada entera se realiza utilizando `int(math.sqrt(num))`, y se introduce un retraso de 1 segundo para simular un cálculo intensivo.

4. **`mostrar_barra_primo()`**: Muestra una barra de progreso para el cálculo del primo.
   - Utiliza `tqdm` para recorrer un rango de `N_PRIMO` (5000) y simular el progreso con un pequeño retraso.

5. **`mostrar_barra_raiz()`**: Muestra una barra de progreso para el cálculo de la raíz cuadrada.
   - Recorre un rango de 100 con un pequeño retraso para simular el progreso.

6. **`ejecutar_tareas()`**: Esta función se ejecuta en cada hilo y toma tareas de la cola hasta que esté vacía.
   - Ejecuta la tarea y marca la tarea como completada.

### Añadiendo Tareas a la Cola
Aquí se añaden cuatro tareas a la cola:
1. Calcular el 5000-ésimo número primo.
2. Mostrar la barra de progreso del cálculo del primo.
3. Calcular la raíz cuadrada entera de 987654321.
4. Mostrar la barra de progreso del cálculo de la raíz cuadrada.

### Creación de Hilos para Ejecutar las Tareas Concurrentemente
Se crean cuatro hilos (`Thread`) que ejecutarán la función `ejecutar_tareas`.

### Esperando que Terminen Todas las Tareas
- `tarea_cola.join()`: Espera a que todas las tareas en la cola se hayan completado antes de continuar.

### Fin
El mensaje "Todas las tareas han terminado." se imprime cuando todas las tareas han finalizado.

En resumen, el código implementa una pequeña simulación de procesamiento concurrente de tareas utilizando hilos. Cada hilo toma tareas de la cola y las ejecuta. Las tareas incluyen cálculos matemáticos (como encontrar un número primo o calcular una raíz cuadrada) y la visualización de barras de progreso durante estos cálculos. Las operaciones se distribuyen entre los hilos para ejecutarse de manera concurrente, lo que acelera el proceso en sistemas con múltiples núcleos de CPU.

## Repositorio
Puedes encontrar el código en el siguiente repositorio: [Github](https://github.com/Jecgarcia/concurrent-programming)
