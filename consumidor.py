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
        while True:
            self.lleno.acquire() # Se adquiere el semáforo lleno
            self.mutex.acquire() # Se adquiere el semáforo mutex, que permite el acceso exclusivo al buffer evita que se acceda al buffer por más de un hilo a la vez y asi evitar condiciones de carrera

            if len(self.buffer) > 0:
                self.buffer.pop()
                self.consumido += 1 # Se incrementa el contador de elementos consumidos
                print("Se consumió un elemento. Total consumidos: ",self.consumido)

            self.mutex.release() # Se libera el semáforo mutex
            self.vacio.release() # Se libera el semáforo vacío
            time.sleep(1) # Se duerme el hilo por un segundo

            