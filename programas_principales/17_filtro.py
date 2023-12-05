#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

#--------------- Uso de filtros --------------------

#==== Hacer una lista de los numeros por arriba del promedio ====

# modulo de estadistica

import statistics

bigdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
promedio = statistics.mean(bigdata)
print(promedio)

# Hazme una lista de elementos que cumplan la condicion x > promedio filter(condicion,datos)

print(list(filter(lambda x: x>promedio, bigdata)))

# Limpiar los datos

paises = ["", "Argentina", "", "Brasil", "", "Chile", "", "Mexico", "", "Columbia", "", "Cuba", "", "Venezulea"]

# Filtra lo que no contine nada

print(list(filter(None, paises)))

