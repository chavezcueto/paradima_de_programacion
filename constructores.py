#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Septiembre 2023
#=============================

#------------------ CONTRUCTORES y  DESTRUCTORES --------------------

#==== Clase computadora ====

class Computadora:
    marca: str = None
    capacidad: int = 0
    ram: int = 0

    #==== Constructor ====

    def __init__(self, marca:str, capacidad:int, ram:int):
        print(f"Accediendo al constructor de la pc: {marca}")
        self.marca = marca
        self.capacidad = capacidad
        self.ram = ram

    def imprimirInfoPc(self):
        print(f"Esta es la computadora marca: {self.marca} con almacenamiento de {self.capacidad}GB y memoria de {self.ram}GB")

     #==== Destructor ====

    def __del__(self):
      print(f"se elimino la computadora: {self.marca}")

#===== Clase persona ====


class Persona:
     nombres: str = None
     apellidos: str = None
     edad: int = 0
     direccion: str = None
     computadora: Computadora = None

     #==== Constructor de persona ====
     def __init__ (self, nombres:str, apellidos:str, edad:int, direccion:str, marca:str, capacidad:int, ram:int):
         self.nombres = nombres
         self.apellidos = apellidos 
         self.edad = edad
         self.direccion = direccion
         self.Computadora = Computadora(marca, capacidad, ram)
         print(f" ----Accedimos al contructor de la persona: {nombres} {apellidos}")

     def ImprimirInfo(self) -> None:
         print(f"--- Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años de edad, vivo en {self.direccion} ")
         self.Computadora.ImprimirInfoPc()

     #==== Destructor ====

     def __del__(self):
         print(f"--- Eliminamos a la persona... {self.nombres} {self.apellidos}")

#==== Funcion 1 es el programa ====

def Funcion1():
    persona = Persona("jaretzy", "Chavez", 21, "Tlalnepantla", "Lenovo", "800", "8")
    print("\n")
    persona.ImprimirInfo()
    print("\n")
    persona2 = Persona("dylan", "alcanatara", 21, "Tlalnepantla", "Pc", "800", "8")
    print("\n")
    persona2.ImprimirInfo()
    print("\n")

#==== llamar a la funcion ====

Funcion1()
