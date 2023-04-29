import threading
import time
class Consumidor(threading.Thread):
    def __init__(self,buffer,bufferSize,producido,consumido,mutex,vacio,lleno):
        threading.Thread.__init__(self)
        self.buffer = buffer # Buffer compartido
        self.bufferSize = bufferSize # Tamaño del buffer
        self.producido = producido # Contador de elementos producidos
        self.consumido = consumido # Contador de elementos consumidos
        self.mutex = mutex # Semáforo mutex
        self.vacio = vacio # Semáforo vacío
        self.lleno = lleno # Semáforo lleno

    def run(self): # Método que se ejecuta al iniciar el hilo