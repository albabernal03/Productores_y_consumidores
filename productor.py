import threading
import time

class Productor(threading.Thread): # Clase Productor hereda de la clase Thread
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
        while True:
            self.vacio.acquire() # Se adquiere el semáforo vacío
            self.mutex.acquire() # Se adquiere el semáforo mutex, que permite el acceso exclusivo al buffer evita que se acceda al buffer por más de un hilo a la vez y asi evitar condiciones de carrera
            if len(self.buffer) < self.bufferSize:
                self.buffer.append(1) # Se agrega un elemento al buffer
                self.producido += 1 # Se incrementa el contador de elementos producidos
                print("Se produjo un elemento. Total producidos: ",self.producido)

            self.mutex.release() # Se libera el semáforo mutex
            self.lleno.release() # Se libera el semáforo lleno
            time.sleep(1) # Se duerme el hilo por un segundo
            


    