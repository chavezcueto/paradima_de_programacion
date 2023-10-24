#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

#==== Del directorio aplicacion, el subdirectorio repositorio, el archivo basededatos.py 
#     : traer el objeto Basededatos ====

from aplicacion.repositorio.basededatos import BaseDeDatos

#==== Del directorio aplicacion, el subdirectorio reposicion, el archivo s3.py : traer el objeto S3 ====

from aplicacion.repositorio.s3 import S3

#==== Del directorio aplicacion, el subdirectorio repositorio, el archivo sistemadearchivos.py : trer el objeto SistemaDeArchivos ====

from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#==== del directorio aplicacion, del subdirectorio  modelos, el archivo usuario.py :  traer el objeto Usuario ====

from aplicacion.modelos.usuario import Usuario 

#==== del directprio aplicacion, el subdirectorio negocios, el archivo manejodeinscribciones.py : traer el objeto Manejodeinscripciones ====

from aplicacion.negocios.manejodeinscrpciones import ManejoDeInscripciones

#==== crear el objeto usuario ====

usuario = Usuario("Dylan","Alcantara",21)

#==== crear el objeto s3 ====

repositorioS3 = S3("321321321","sdf324223","Micuenta")

#==== Interface inscribirUsuario del objeto Manejodeinscripciones ====

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#==== Crear el objeto sistemadearchivos ====

repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#==== Interface inscribirUsuario del objeto ManejoDeInscrpciones ====

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#==== crear el objeto basededatos ====

repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

#==== Interface inscribirUsuario dek objeto ManejoDeInscripciones ====

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")
