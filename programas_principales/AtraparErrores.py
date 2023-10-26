#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

#==== La clase ClienteBancario esta en el subdirectorio aplicacion/banco ====

from cliente_bancario import ClienteBancario

# try: intenta (correr las instrucciones)
# except: atrapar el error en una variable e
# e se puede convertir  a string

#==== Error por sacar mas dinero del que tiene ====
try:
    cliente= ClienteBancario("Jaretzy Yajahira","Chavez Cueto",21,0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())

# Exception es el objeto mas general de error

except Exception as e:
    print("Error: " + str(e)) 

#==== Error por uszsar un artributo privado ====
try:
    print(cliente.nombres)
except Exception as ex:
    print("Error: " + str(ex))

#==== Fornma correcta ====
print(cliente.nombres)
