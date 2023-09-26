#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matematica Algoritmica
# Paradigmas de programacion
# ESFM IPN Septiembre 20023
#==============================

#===========
#funciones
#===========

#==== Mi primera funcion====

def saludo():
        #-------------------------------------
        # Documentacion rapida de la funcion
        #-------------------------------------
        """Esta funcion saluda"""
        print('¡Quiuboles!, ¿como estas?')

#==== Llamado de la funcion ====
saludo()

#==== Se ejecuta pero no se asigna ====
salida = saludo()

#==== Esto no funciona ====
print(salida)

#==== Mostrar documentacion ====
#help(saludo)

#==== Funcion con argumento ====

def saludos(nombre):
    """ Esta funcion te saluda por tu nombre """
    print("¡Que onda ese",nombre,"!")
saludos("Julian")
saludos("yare")

#==== Ahorrar trabajo al interprete ====
#==== nombre:str la variable nombre es un str ====

def salu2(nombre:str):
    """Esta funcion te saluda por tu nomre estrictamente"""
    print("!que onda ese", nombre,"¡")
salu2("yare")
a=123
print(type(a))
salu2(a)

#==== funcion con muchos argumentos====
def saludos_multiples(nombre1,nombre2,nombre3):
     """esta funcion saluda a tres personas al mismo tiempo"""
     print("Hola ",nombre1, ",",nombre2, "y", nombre3)
saludos_multiples("Hugo","Paco","luis")

#==== funcion con cualquier numero de argumentos ====

def muchos_saludos (*nombre):
    """esta funcion saluda a todos los que quieras"""
    i = 0
    #==== end= es para ponerlo de corrido ====
    print("Hola ", end="")
    while len(nombre) > i:
        #ultimo nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            #cualquier otro nombre
            print(nombre[i], end=", ")
        i+=1
