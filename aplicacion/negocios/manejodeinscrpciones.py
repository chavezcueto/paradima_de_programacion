#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#==== Clsase ManejoDeInscripciones (NO TIENE VARIABLES) ====

class ManejoDeInscripciones:

    # Decorado staticmethod
    # el objeto solo tiene la funcion inscribirUsuario
    # ENVUELVE LA FUNCION LLAMAR VARIABLES LOCALES 
    # el obejto ManejoDeInscripciones el al interface intercambiable

    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("----> Guardando Usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()

