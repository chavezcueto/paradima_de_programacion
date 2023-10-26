#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

#--------------------- yield transforma la funcion a iterador ---------------------

def migenerador():
    print("primero")
    yield 10
    print("segundo")
    yield "20"
    print("tercero")
    yield "hola"

# gen es un iterador

gen = migenerador()
val1 = next(gen)
print(val1)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)

