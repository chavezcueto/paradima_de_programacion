#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   enero 2024
#==============================

from multiprocessing import Process, Lock, Value
import random
import os

# simulacion montecarlo en paralelo
def montecarlo(N:int,resultado:Value,lock:Lock) -> None:
    semilla:float = random.uniform(-1,1)
    random.seed(semilla)
    dentro:int = 0
    for i in range(N):
        x:float = random.uniform(-1,1)
        y:float = random.uniform(-1,1)
        if (x*x + y*y) < 1.0:
            dentro +=1
    # bloquear escritura para evitar conflictos
    with lock:
        resultado.value += dentro

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    lock = Lock()
    n:int = 1.0e7
    cpus = os.cpu_count()
    N:int = int (n/cpus)
    print("Procesadores = ", cpus)
    # valor compartido
    resultado = Value("i",0)
    procesos = []
    for i in range(cpus):
        print("registrando el proceso %d ", i)
        procesos.append(Process(target=montecarlo,args=(N,resultado,lock)))
    for proceso in procesos:
        proceso.start()
    for proceso in procesos:
        proceso.join()

    print("numero de tiros = ", cpus*N)
    print("numero de aciertos = ", resultado.value)
    print("aproximacion de pi = ", 4*float(resultado.value)/(cpus*N))
