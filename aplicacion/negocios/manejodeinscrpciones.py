#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriousurios import RepositoriosDeUsuarios

#==== Clsase ManejoDeInscripciones (NO TIENE VARIABLES) ====

class ManejoDeInscrpciones:

    # Decorado staticmethod
    # el objeto solo tiene la funcion inscribirUsuario
    # ENVUELVE LA FUNCION LLAMAR VARIABLES LOCALES 
    # el obejto ManejoDeInscripciones el al interface intercambiable

    @staticmethod
    def inscribirUsuario(usuario: Uusuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("----> Guardando Usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()

