#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

from aplicacion.repositorio.repositoriodeusurios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#==== S3 es hijo de RepositorioDeUsuarios ====

class S3(RepositorioDeUsuarios):
    __clientId: str
    __secretKey: str
    __bucket: str

    def __init__(mi,clientId: str, secretKey: str, __bucket:str):
        mi.__clientId = clientId
        mi.__secretKey = secretKey
        mi.__bucket = bucket

    def abrir(mi) -> None:
        print(f"Establecioendo conexiona AWS S3 {mi.__clientId}:{mi.secretKey}")

    def guardar(mi, usuario:Usuario) -> None:
        userData = {"Nombre": usuario.getNombre(),
                "apellidos": usuario.getApellidos(),
                "edad": usuario.getEdad() }
        print(f"Guardando usuario de mi bandeja:{mi.__bucket}: {userData}")

    def cerrar(mi) -> None:
        print("cerrando conexion AWS S3")
