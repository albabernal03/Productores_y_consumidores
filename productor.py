import threading
import time

class Productor(threading.Thread): # Clase Productor hereda de la clase Thread
    def __init__(self,buffer,bufferSize,productor,consumidor,mutex,vacio,lleno):
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.bufferSize = bufferSize
        self.productor = productor
        self.consumidor = consumidor
        self.mutex = mutex
        self.vacio = vacio
        self.lleno = lleno
    
    def run(self): # Método que se ejecuta al iniciar el hilo
        while True:
            

    