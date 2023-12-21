#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Diciembre 2023
#==============================

# modulos de hilos, procesos, sistema, atematicas y tiempo
from threading import Thread
from multiprocessing import Process
import os
import math
import time

# funcion
def calc():
    for i in range(0,4000000):
        math.sqrt(i)

# lista de hilos
threads = []

# procesadores en mi maquina
cpus = os.cpu_count()
print("Numero de procesadores: ", cpus)

# inscribir hilos en la lista
for i in range(cpus):
    print("registrando el hilo %d" % i)
    threads.append(Thread(target=calc))

start = time.time()

# iniciar todos los hilos (son seriales)
for thread in threads:
    thread.start()

# esperar a que termine los hilos
for thread in threads:
    thread.join()

end = time.time()

# restar los tiempos
print("se tardo: ", end-start)

# lista de procesos
procesos = []
for i in range(cpus):
    print("registrando el proceso %d" % i)
    procesos.append(Process(target=calc))

start = time.time()

# iniciar procesos (en paralelo)
for proceso in procesos:
    proceso.start()

end = time.time()
print("se tardo: ",end-start)
