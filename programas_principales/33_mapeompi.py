#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Diciembre 2023
#==============================

from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# datos
n = 40
x = range(n)
m = int(math.ceil(float(len(x)) / size))

# cada proceso tiene un pedazo de los datos
x_chunk = list(x[rank*m:(rank+1)*m])
r_chunk = list(map(math.sqrt, x_chunk))

# una sola lista de todos los datos en cada proceso 
r = comm.allreduce(r_chunk)

# una matriz con todos los daos en cada proceso
rr = comm.allgather(r_chunk)

# una matriz con todos los daos para el proceso 1
rrr = comm.gather(r_chunk,root=1)

# ver lo que paso
if rank == 0:
    print(r)
    print(rr)
    print(rrr)
if rank == 1:
    print(rrr)
