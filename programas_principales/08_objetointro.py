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
class Llanta:
    #==== variabl cuenta es de toda la clase ====
    cuenta = 0
    #==== funcion constructora de identidad ====
    #==== __init__ es una funcion reservada ====
    #==== comienza con uno mismo: self ====
    #==== prametro de entrada = default ====

    def __init__(mi,radio=50,ancho=30,presion=1.5):
        #variable de la esctructura completa llanta
        Llanta.cuenta +=1
        #variable exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion 

#==== objetos (instanciados) ====
llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#==== objetos que contiene otros objetos ====

class coche:
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1=ll1
        mi.llanta2=ll2
        mi.llanta3=ll3
        mi.llanta4=ll4

micoche = coche(llanta1,llanta2,llanta3,llanta4)
print("total de llanta: ",Llanta.cuenta) #variable global de la clase
print("presion de la llanta 4 = ", llanta4.presion) #presion de la llanta 4
print("radio de la llanta 4 = ",llanta4.radio)
print("radio de la llanta 3 = ",llanta3.radio)
print("presion de la llanat 1 de mi coche = ", micoche.llanta1.presion)

 #==== encapsulamiento ====

 #==== uso de la funcion de python property para poner y obtener atributos ====
class Estudiante:
    def __init__ (mi):
         mi.__nombre = " "
    def ponerme_nombre(mi, nombre):
            print ("se llamo a ponerme_nombre")
            mi.__nombre=nombre
    def obtener_nombre(mi):
            print("se llamo a obtener_nombre")
            return mi.__nombre
    nombre=property(obtener_nombre,ponerme_nombre)
 
 #==== crear objeto estudiante sin nombre ====
estudiante= Estudiante()
 
 #==== ponerle nombre usando la propiedad nombre y el metodo ponerme_nombre =====
 #==== (sin tener que llamar explicitamente la funcion)====

estudiante.nombre = "diego"

 #==== obtener el nombre con el metodo obtener_nombre ====
 #==== __nombre es una variable encapsulada (no visible desde afuera) ====
 #==== (sin tener que lñlamar explicitamente a la funcion obtener_nombre) ====
print(estudiante.nombre)
  
#==== eesto no funciona ====
#print(estudiante.__nombre)

#==== herencia de clases ====

class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d

    def perimetro(mi):
        p=mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print("perimetro= ",p)
        return p

# ==== su hijo rctangulo [rectangulo es hijo de cuadrilatero(rectangulo(cuadrilatero))

class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        #==== constructor de su madre ====
        super().__init__(a,b,a,b)

#==== su nieto cuadrado (hijo de rectangulo)

class Cuadrado(Rectangulo):
    def __init__(self,a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area

    #def perimetro(self):
    # p=4.0*self.lado1
    # print("perimetro= ",p)
    # return p

#==== crear un cuadrado ====

cuadrado1 = Cuadrado(5)

#==== llamar al metodo perimetro de su abuelo cuadrilatero ====
perimetro1 = cuadrado1.perimetro()

#==== llamar a su propio metodo area ====

area1 = cuadrado1.area()

print("perimetro= ",perimetro1)
print("area= ", area1)

#==== sobre-escribir un metodo de su madre o abuela o tatarabuela... =====
#==== es volver a definir una funcion ya existente ====

