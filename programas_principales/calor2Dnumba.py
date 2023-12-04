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
#=====================================
# parametros que se pueden cambiar (Parametros de entrada)
#=====================================

# numero de celdas
n = np.array([512,512])
# tamaño del dominio (menor que uno)
L = np.array([1.0,2.0])
# constante de difusion
k = 0.2
# paso de tiempo
pasos = 100

#==================================================
# parametros secundarios (no se deben cambiar)
#==================================================

# tamaño de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)
# paso de tiempo 
dt = 0.25*(min(dx[0], dx[1])**2)/k
print("dt = ",dt)
# Total de celdas
nt = n[0]*n[1]
print("celdas = ", nt)

#===============================
# Arreglos iniciales
#===============================

# llenar la solucion con ceros
u = np.zeros(nt,dtype=np.float64) #arreglo de lectura
un = np.zeros(nt,dtype=np.float64) # arreglo de escritura

#==============================================================
# evolucion temporal de la ecucion diferencial parcial
# u_t = k*laplaciano(u) (ecucion de difunsion de calor)
# FUncion sin interprete de python
#==============================================================
Qjit(nopython=True)
def evolucion(u,n,udx2,dt,i,k):
    jpl = i + n[0]
    jml = i - n[0]
    laplaciano = (u[i-1]-2.0*u[i]+u[i+1])*udx2[0] + (u[jml]-2.0*u[i]+u[jpl])*udx2[1]
    unueva = u[i] + dt*k*laplaciano

    return unueva

#==================================================================
# loop sobre toda la malla para avanzar la ecucion en el tiempo 
# no contien la frontera (u=0 en toda la orilla del dominio)
# loop acelerado sin interprete de python
#==================================================================
@jit(nopython=True)
def solucion(u,un,udx2,dt,n,k):
    for jj in range(1,n[1]-1):
        for ii in range(1,n[0]-1):
            i = ii + n[0]*jj
            #====================================
            # avanzar la ecuacion en un punto
            #====================================
            unueva = evolucion(u,n,udx2,dt,i,k)
            #====================================================
            # en medio de la malla poner temperatura fija 1
            #====================================================
            if i == int(nt/2)+int(n[0]/2):
                unueva = 1.0
            un[i] = unueva

#============================
# PROGRAMA PRINCIPAL
#============================

start = time.time()

#=====================
# pasos de tiempo
#=====================

for t in range(1,pasos+1):
    #========================================
    # Avanzar ecucion en toda la malla
    #========================================
    solucion(u,un,udx2,dt,n,k)
    #========================================
    # copiar arreglo nuevo al viejo 
    #========================================
    u = un
    #========================================
    # avisar en patalla el paso en el que va
    #========================================
    if t%10==0: print("iteracion = ",t)

end = time.time()
print("Tardo: ", end-start,"s")

#=============================================
# Grafico de la solucion al tiempo final
#=============================================

x,y = np.meshgrid(np.arange(0,L[0],dx[0]),np.arange(0,L[1],dx[1]))
ax = plt.axes(projection="3d")
up = np.reshape(u,(n[0],n[1]))
ax.plot_surface(x,y,u,cmap=cm.hsv)
plt.show()

