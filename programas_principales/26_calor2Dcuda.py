#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Diciembre 2023
#==============================

#=================================================
# importar numpy, matplotlib, mpl_toolkits, time
#=================================================
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from numba import jit
from numba import cuda
from numba import *
#=====================================
# parametros que se pueden cambiar (Parametros de entrada)
#=====================================

# numero de celdas
n = np.array([512,512],dtype=np.int64)
# tamaño del dominio (menor que uno)
L = np.array([1.0,2.0],dtype=np.float64)
# constante de difusion
kd:float64 = 0.2
# paso de tiempo
pasos:int = 100

#==================================================
# parametros secundarios (no se deben cambiar)
#==================================================

# tamaño de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)
# paso de tiempo
dt = 0.25*(min(dx[0], dx[1])**2)/kd
print("dt = ",dt)
# Total de celdas
nt = n[0]*n[1]
print("celdas = ", nt)

#==============================================================
# evolucion temporal de la ecucion diferencial parcial
# u_t = k*laplaciano(u) (ecucion de difunsion de calor)
# FUncion sin interprete de python
#==============================================================
@jit(nopython=True)
def evolucion(u,n_0,n_1,udx2_0,udx2_1,dt,i,kd):
    jpl = i + n_0
    jml = i - n_0
    laplaciano = (u[i-1]-2.0*u[i]+u[i+1])*udx2_0 + (u[jml]-2.0*u[i]+u[jpl])*udx2_1
    unueva = u[i] + dt*kd*laplaciano

    return unueva
#========================
# Funcion para el GPU
#========================
evolucion_gpu = cuda.jit(device=True)(evolucion)

#=================================
# Rutina de CUDA (nvidia)
#=================================
@cuda.jit
def solucion_kernel(u_d,un_d,udx2_0,udx2_1,dt,n_0,n_1,kd):
    ii, jj =cuda.grid(2)
    i = ii + n_0*jj
    if ii==0 or jj==0 or ii==n_0-1 or jj==n_1-1:
        unueva = 0.0
    else:
        unueva = evolucion_gpu(u_d,n_0,n_1,udx2_0,udx2_1,dt,kd,i)
    if i== int((n_0*n_1)/2)+int(n_0/2):
        unueva = 1.0
    un_d[i] = unueva

blockdim = (32,16) #hilos por bloque
griddim = (int(n[0]/blockdim[0]), int(n[1]/blockdim[1])) #bloques en el dominio

#============================
# PROGRAMA PRINCIPAL
#============================

start = time.time()

# llenar la solucion con ceros
u = np.zeros(nt,dtype=np.float64) #arreglo de lectura
un = np.zeros(nt,dtype=np.float64) # arreglo de escritura

# pasar arreglos al GPU
u_d = cuda.to_device(u)
un_d = cuda.to_device(un)

#=====================
# pasos de tiempo
#=====================

for t in range(1,pasos+1):
    solucion_kernel[griddim,blockdim](u_d,un_d,udx2[0],udx2[1],dt,n[0],n[1],kd)
    # copiar arreglo dentro del GPU
    u_d = cuda.to_device(un_d)
    if t%100==0: print("paso = ",t)
# pasar arreglo dentro del GPU
u_d.copy_to_host(u)
end = time.time()
print("Tardo: ", end-start,"s")

#=============================================
# Grafico de la solucion al tiempo final
#=============================================

u = np.reshape(u,(n[0],n[1]))
x,y = np.meshgrid(np.arange(0,L[0],dx[0]),np.arange(0,L[1],dx[1]))
ax = plt.axes(projection="3d")
ax.plot_surface(x,y,u,cmap=cm.hsv)
plt.show()
