#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Noviembre 2023
#==============================

#=================================================
# importar numpy, matplotlib, mpl_toolkits, time
#=================================================
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time

#=====================================
# parametros que se pueden cambiar
#=====================================

# numero de celdas
n = np.array([512,512])
# tamaño del dominio (menor que uno)
L = no.array([1.0,2.0])
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

#
