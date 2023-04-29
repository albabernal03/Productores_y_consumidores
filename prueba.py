'''Desarrollo del programa productores y consumidores. Para ejemplificar el desarrollo de un programa para productores y consumidores, asumimos que el productor es el que genera los recursos que van a utilizar los consumidores, por lo tanto los consumidores necesitan un proceso de sincronización con el productor para saber cuando el momento de consumir ha llegado.'''

import threading
import time


#creaamos una lista vacia
buffer = [] #esto lo hacemos para que el productor pueda agregar elementos a la lista
buffer_size = 5 #tamaño del buffer