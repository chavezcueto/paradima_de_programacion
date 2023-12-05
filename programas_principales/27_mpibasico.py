#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Diciembre 2023
#==============================

# para correr en 4 procesos
from mpi4py import MPI

# crear un objeto comunicador
comunicadores = MPI.COMM_WORLD

# numero total de procesos
n_procesos = comunicadores.Get_size()

# identificador de este proceso
quien soy = comunicadores.Get_rank()

print("saludos desde el proceso ", str(quien_soy), "de ", str(n_procesos))

# si yo soy el cero hago esto
if quien_soy == 0:
    print("yo soy el proceso 0")

# si yo soy el uno hago esto
elif quien_soy == 1:
    print("yo soy el proceso 1")

# si yo no soy ni el uno ni el cero hago esto

else:
    print("yo no soy ninguno de los dos primeros procesos")

