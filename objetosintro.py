#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Septiembre 2023
#=============================

#------------------ PROGRAMACION ORIENTDA A OBJETOS -----------------------

# ==== Una clase para un objeto vacio ====
# ==== no esta vacio, necesita la palabra pass = pasar ====

class objetovacio:
    pass

#==== nada es un objeto vacio ====

nada= objetovacio()
print(type(nada))

#==== la clase llanta ====
class llanta:
    #==== variabl cuenta es de toda la clase ====
    cuenta = 0
    #==== funcion constructora de identidad ====
    #==== __init__ es una funcion reservada ====
    #==== comienza con uno mismo: self ====
    #==== prametro de entrada = default ====

    def __int__(mi,radio=50,ancho=30,presion=1.5):
        #variable de la esctructura completa llanta
        llanta.cuenta +=1
        #variable exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion 

#==== objetos (instanciados) ====
llanta1 = llanta(50,30,1.5)
llanta2 = llanta(presion=1.2)
llanta3 = llanta()
llanta4 = llanta(40,30,1.6)

#==== objetos que contiene otros objetos ====

class coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1=ll1
        mi.llanta2=ll2
        mi.llanta3=ll3
        mi.llanta4=ll4

micoche = coche(llanta1,llanta2,llanta3,llanta4)

print("total de llanta: ",llanta.cuenta) #variable global de la clase
print("presion de la llanta 4 = ", llanta4.presion) #presion de la llanta 4
print("radio de la llanta 4 = ",llanta4.radio)
print("radio de la llanta 3 = ",llanta3.radio)
print("presion de la llanat 1 de mi coche = ", micoche.llanta1.presion)

 #==== encapsulamiento ====

 #==== uso de la funcion de python property para poner y obtener atributos ====
 class estudiantes:
     def __init__ (mi):
         mi._nombre = " "
        def ponerme_nombre(mi, nombre):
            print ("se llamo a ponerme_nombre")
            mi._nombre=nombre
        def obtener_nombre(mi):
            print("se llamo a obtener_nombre")
            return mi._nombre
        nombre=property(obtener_nombre,ponerme_nombre)
 
 #==== crear objeto estudiante sin nombre ====
 Estudiante= estudiante()
 
 #==== ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre =====
 #==== (sin tener que llamar explicitamente la funcion)====

 estudiante.nombre = "diego"

 #==== obtener el nombre con el metodo obtener_nombre ====
 #==== __nombre es una variable encapsulada (no visible desde afuera) ====
 #==== (sin tener que lñlamar explicitamente a la funcion obtener_nombre) ====
 print(estudiante.nombre)
  
#==== eesto no funciona ====
#print(estiante.__nombre)

#==== herencia ====
