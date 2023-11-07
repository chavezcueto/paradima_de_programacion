#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Noviembre 2023
#==============================

#==== recursividad y memorizacion ====

#==== herramientas para memorizacion ====

from functools import lru_cache

def fibonacci_lento(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fibonacci_lento(n-1)+fibonacci_lento(n-2)

for i in range(1,34):
    print(str(i) + ":", fibonacci_lento(i))

#=========================================================
# optimizacion 1: uso de conjuntos ára guardar valores
#=========================================================

#==== conjunto de fibonaccs ====

fibonaccis = {}
def fibonacci(n):

    #==== revisa si ya existe y regresa el valor ====

    if n in fibonacci:
        return fibonaccis[n]


