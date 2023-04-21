''' ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
'''
#=====================
# Operaciones basicas 
#=====================
print (2+3)
print (2*3)
print (2/3)
print (1**10)
print(2**0.5) #raiz cuadrada
print (10%2)
print (10%0.1) #exclusivo en python
#=============================================
# Para saber el tipo de objeto se usa en type
#=============================================
t=0
print(type(t)) # entero
t=3.6
print(type(t)) #real (flotante)
t=True
print(type(t)) #boleano (bool)
#======================
# Mensaje a patalla
#======================
print ("Este es un comando de python ", "Este es otro enunciado", t)
print ('id: ',1)
print ('First Name: ','Steve')
print ('last Name: ', 'jobs')
print ("vamos a sumar esto" + " con esto otro")
#===============================================
# Continuar una instruccion en varios renglones
#===============================================
if 100>99 and \
        200 <= 300 and \
        True != False:
            print('hello word')
#=========================================
# Comandos diferentes en la misma linea
#=========================================
print("Hola "); print("tu!!") #Se considera mala pratica

#======================================================
# Usando parentesis redondos, cuadrados o llaves
# se puede escribir en varios renglones
#======================================================
list = [1,2,3,4,
        5,6,7,8,
        9,10,11,12]
matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]
print (list)
print(matriz)

#==================================================================
# Indentacion estricta para procesos dependientes de : (dos puntos)
#==================================================================
if 10>5:
    print (" diez meyor que cinco")
    print("otra indentacion")
for i in list:
    print (i)
    print ("ok")
if 10>5:
    print("verdadero")
    if 10<20:
        print ("verdadero")
elif 5>3: #comienza segundo condicional 
    print ("esto no se imprimira")
else:
    print ("aqui nunca llega")
#===============
# Funciones
#===============
def say_hello(name):
    print ("hello ", name)
    print ("welcome to python Tutorials")

say_hello ("julian")

#=========================================================
#input permite obtener datos del usuario en prompter
#=========================================================
nombre =  input ("dame tu nombre: ")
print ("Hola como esta" , nombre)
#=======================================
# enteros son de precision ilimitada
#=======================================
y = 500000000000000000000000000000000000
print (y)

#======================================================
#la notacion cientifica de flotantes utiliza e o E
#======================================================
# 1.2x10^{-9}
#=================
y=1.2E-09
print(y)

#==========================================================
# la funcion float() convierte strings y enteros a floats
#==========================================================
y = float ("14.3")
print (y)

#==============================================================
# Los complejos se escriben con la raiz de menos uno
# j siempre con un numero como prefija
# no se acepta j suelta
#==============================================================
z= 1+1j

#suma +
#resta -
#multiplicaion *
#division /
#modulo %
#exponente **
#// funcion piso
# funciones para transformar numeros int() float() complex()
#operaciones abs() round() pow()
print(round(3.14159,4))

#===========================================
# strings de varias lineas
#===========================================
parrafo = """En el bosque de la china
la chinita se perdio"""
print(parrafo)

#=================================================
# la funcion len() obtiene el tamaño del string
#=================================================
n=len(parrafo)
print(n)

#==============================================================
# Las letras en un string ocupan lugares como en un arreglo
# (tambien de atras para adelante comenzando en -1 el ultimo)
#==============================================================
palabra =("hola")
print(palabra[0])
print(palabra[-4])

