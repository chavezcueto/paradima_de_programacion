#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Diciembre 2023
#==============================

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# se indican el tipo de datos explicitamente
# este ejemplo solo tiene 2 procesos

# EJEMPLO 1 USANDO ENTEROS

if rank == 0:
    
    # arreglos de enteros del 0 al 9 
    data = numpy.arange(10, dtype="i")

    # envio bloqueante especificado el tipo de dato 
    # tag es in identificador del mensaje

    comm.Send([data, MPI.INT], dest=1, tag=77)

elif rank == 1:
    data = numpy.empty(10, dtype="i")
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print (data)

# tambien se puede sin decir el tipo de dato pero deben coincidir el tipo de arreglos a los extremos del mensaje

# EJEMPLO 2 USANDO FLOTANTES

if rank == 0:
    data = numpy.arange(10, dtype=numpy.float64)
    comm.Send(data, dest=1, tag=13)
elif rank == 1:
    data = numpy.empty(10, dtype=numpy.float64)
    comm.Recv(data, source=0, tag=13)
    print(data)
