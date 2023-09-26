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

def muchos_saludos (*nombres):
    """esta funcion saluda a todos los que quieras"""
    i = 0
    #==== end= es para ponerlo de corrido ====
    print("Hola ", end="")
    while len(nombres) > i:
        #ultimo nombre
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            #cualquier otro nombre
            print(nombres[i], end=", ")
        i+=1
muchos_saludos("bosco","angel","david","tamara","mili","edwin","lav","luis","abigail")
def greet(firstname, lastname):
    print("hello", firstname, lastname)
#==== llamar la funcion con argumentos en desorden ====
greet(lastname="jobs", firstname="stave")

#==== funcion con argumentos escondidos ====
def greet(**person):
    #==== persona tiene caracteristicas firstname y lastname ====
    print( "hello", person["firstname"], person["lastname"])

greet (firstname="steve", lastname="hobs")
greet (firstname="jobs", lastname="gates", age=55) # se pueden pasar mas parametros de los necesarios

#====funcion con valoeres por defecto====
def greet(name="guest"):
    print("hello", name)

greet () # utiliza el valor dado de antemano 
greet("steve")

#==== funcion cpn resultado ====
def suma(a,b):
    return a+b

#==== programacion funcional ====
#==== se puede usar funciones dentro de funciones ====

total=suma(5, suma(10,20))
print(total)

#==== calculo lambda ====
#==== nombre de la funcion = lambda variable: funcion ====
x_al_cuadrado = lambda x : x * x
a1 = x_al_cuadrado(5)
print(a1)

#==== lambda de varias variables ====

suma = lambda x1 , x2, x3: x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]
print(sumas(100,200,300,400))

#==== uso de una funcion anonima====
#==== el argumento va afuera entre parentesis ====
print ((lambda x: x*x)(6)) #funcion anonima

