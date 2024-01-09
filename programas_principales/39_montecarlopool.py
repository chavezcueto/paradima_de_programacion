#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   enero 2024
#==============================

from multiprocessing import Pool 
import random
import os

# simulacion montecarlo en paralelo
def montecarlo(N:int) -> int:
    semilla:float = random.uniform(-1,1)
    random.seed(semilla)
    dentro:int = 0
    for i in range(N):
        # pares de numeros al azar en (-1,1)
        x:float = random.uniform(-1,1)
        y:float = random.uniform(-1,1)
        # contar los que estan dentro del circulo radio 1
        if (x*x +y*y) < 1.0:
            dentro +=1
    return dentro
if __name__ == "__main__":
    n:int = 1.0e7
    cpus = os.cpu_count()
    N:int = int(n/cpus)
    print("procesdores = ",cpus)
    arg = [N for i in range(cpus)]
    # el objeto grupo tiene metodo map para repetir tarea
    results = Pool(cpus).map(montecarlo,arg)
    print("numero de tiros: ",cpus*N)
    print("numero de aciertos: ", results)
    # sumar los resultados y calcular pi
    print("aproximacion de pi = ",4*sum(results)/(cpus*N))
