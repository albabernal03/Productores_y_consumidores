from productor import *
from consumidor import *

if __name__ == '__main__':
    buffer = [] 
    buffer_size = 5 
    mutex = threading.Semaphore(1) 
    full = threading.Semaphore(0) 
    empty = threading.Semaphore(buffer_size) 
    produced = 0 
    consumed = 0 

   
    p = Productor(buffer, buffer_size, produced, consumed, mutex, full, empty)
    c = Consumidor(buffer, buffer_size, produced, consumed, mutex, full, empty)

   
    p.start()
    c.start()


    p.join()
    c.join()
