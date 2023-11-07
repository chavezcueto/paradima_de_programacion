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

print(" ")
#=========================================================
# optimizacion 1: uso de conjuntos ára guardar valores
#=========================================================

#==== conjunto de fibonaccs ====

fibonaccis = {}
def fibonacci(n):

    #==== revisa si ya existe y regresa el valor ====

    if n in fibonaccis:
        return fibonaccis[n]

    if n == 1:
        valor = 1
    elif n==2:
        valor = 1
    elif n>2:
        valor = fibonacci(n-1) + fibonacci(n-2)

    # guardalo

    fibonaccis[n] = valor
    return valor

for i in range(1,10001):
    print(str(i) + ":", fibonacci(i))
print(" ")

#==========================================================
# uso de decoradores para memorizacion
# maxsize: es cuantos anteriores guarde
#==========================================================

@lru_cache(maxsize = 3)

def nfibonacci(n):
    if type(n) != int:
        raise TypeError("n debe ser entero positivo")
    if n<1:
        raise ValueError("n debe ser entero positivo")

    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return nfibonacci(n-1) + nfibonacci(n-2)
    for i in range(1,10001):
        print(str(i) + ":", nfibonacci(i))
