#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Diciembre 2023
#==============================

# broadcast com MPI
# distribucion de datos

from mpi4py import MPI
import numpy

# objeto comunicador 
comm = MPI.COMM_WORLD

# quien soy
rank = comm.Get_rank()
 
#  el proceso 0 tiene datos y los otros no 
if rank == 0:
    data = {"key1" : [7, 2.72, 2+3],
            "key2" : ("abc","xyz")}

else:
    data = None

# enviar diccionario a todos los procesos desde root
data = comm.bcast(data, root=0)
print(data)

# ahora mas rapido usando numpy

# tamañp del arreglo
n = 10
if rank == 0:
    # arreglo de enteros del 0 al n-1
    data = numpy.arange(n, dtype="i")
else:
    # arreglo vaci de enteros de tamaño n
    data = numpy.empty(n, dtype="i")

# broadcast pro que indica el tipo de dato
# opimizado paa comunicacion rapida
comm.Bcast([data,MPI.INT], root=0)

# asegurarse que todo salio bien
for i in range(n):
    assert data[i] == i
print(data)
