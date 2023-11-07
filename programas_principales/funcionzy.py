#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Noviembre 2023
#==============================

#====== Tres listas =======

mi_lista = [1,2,3]
tu_lista = (10,20,30)
su_lista = (40,50,100)

#==== funcion multiplica por 2 ====

def multiplicar_por2(elemento):
    return elemento % 2 !=0

#============================================
# lista de pares de datos de las dos listas 
# zip sirve para juntar listas 
# list es para que la haga lista
#============================================

print(list(zip(mi_lista, tu_lista, su_lista)))

print("                         ")

una_lista = ["a", "b", "c", "b", "d", "m", "n", "n"]

#==== crear conjunto de elementos que se repiten ====

duplicados = set([x for x in una_lista if una_lista.count(x) > 1])
print(duplicados)

print("                                ")
#======================================================
# expresion generadora 
# contiene un iterador 
# range (5) es un iterador de 0 a 4
# utiliza ()
#======================================================

cuadrados = (x*x for x in range(5))

#==== next llama a la siguiente evalucion del iterador ====

print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))

print("                           ")
#==== pasar una funcion generadora ====

import math

#==== suma los elementos del iterador ====

print(sum(x*x for x in range(5)))

print(" ")

#=======================================================
# lista de comprehension pasad acomo funcion
# arma la lista por usar[]
#=======================================================

numeros_pares = [x for x in range(21) if x%2 == 0]
print([x for x in range(21) if x%2 == 0])
print(numeros_pares)

