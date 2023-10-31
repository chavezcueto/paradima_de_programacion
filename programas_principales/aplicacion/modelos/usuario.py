#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

#==== Clsase Usuario ====

class Usuario:
    __nombre: str
    __apellidos: str
    __edad: int

    # Constructor

    def __init__ (mi,nombre:str,apellidos:str,edad:int):
        mi.__nombre = nombre
        mi.__apellidos = apellidos
        mi.__edad = edad

    # Getters

    def getNombre(mi) -> str:
        return mi.__nombre
    def getApellidos(mi) -> str:
        return mi.__apellidos
    def getEdad(mi) -> int:
        return mi.__edad
