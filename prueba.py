'''Desarrollo del programa productores y consumidores. Para ejemplificar el desarrollo de un programa para productores y consumidores, asumimos que el productor es el que genera los recursos que van a utilizar los consumidores, por lo tanto los consumidores necesitan un proceso de sincronización con el productor para saber cuando el momento de consumir ha llegado.'''

import threading
import time


#creaamos una lista vacia
buffer = [] #esto lo hacemos para que el productor pueda agregar elementos a la lista
buffer_size = 5 #tamaño del buffer
#creamos un semaforo
semaphore = threading.Semaphore(0) #inicializamos el semaforo en 0 para que el consumidor no pueda consumir hasta que el productor no haya producido
#creamos un mutex
mutex = threading.Semaphore(1) #inicializamos el mutex en 1 para que el productor pueda producir
#creamos una variable que nos indique el numero de elementos que se han producido
produced = 0
#creamos una variable que nos indique el numero de elementos que se han consumido
consumed = 0
full = threading.Semaphore(0)
empty = threading.Semaphore(buffer_size) 

