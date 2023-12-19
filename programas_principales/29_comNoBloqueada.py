#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Diciembre 2023
#==============================

# Uso de  MPI opimizando para calculos numericos

from mpi4py import MPI
import numpy as np

class Mensaje:
    def __init__(self,rank):

        # lista comun

        self.x = [i for i in range(rank*10)]
        self.p = "vengo del proceso " +str(rank)

        # arreglo de numpy (optimizado)

        self.xx = np.array([float(x+rank) for x  in range(10)])
        self.pp = "vengo del proceso " + str(rank)

# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank-1 if rank!=0 else size-1
    dst = rank+1 if rank!=size-1 else 0

    # Envio no bloqueaste

    comm.isend(s, dest=dst)

    # recibir no bloqueaste con espera
    # req: request (peticion)

    req = comm.irecv(source=src)
    a = req.wait()

    print("soy el proceso ", rank, ", el resultado es ", len(a.x),a.p)

    # arreglo de numpy para enviar

    m = s.xx

    # Isend Irecv son para comunicacion
    # no bloqueante de arreglos de numpy

    comm.Isend(m, dest=dst)

    # arreglo vacio para recibir con dimesion 10 y tipo de datos
    # float64 (doble precision)

    aa= np.zeros(10,dtype=np.float64)
    req = comm.Irecv(aa, source=src)
    req.Wait()

    print("soy el proceso ", rank, ", el resultado es ", aa)
