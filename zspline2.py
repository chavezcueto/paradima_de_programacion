#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Septiembre 2023
#=============================

#------------------ z-spline  --------------------

import numpy as np
from zspline import Curva,zpline
import matplotlib.pyplot as plt
import math

#==== Conjunto de puntos ====

# Numero de puntos 
nump:np.int32 = 5
# dimension
dim:np.int32 = 2
# memoria para puntos
puntos  = np.zeros(dim*nump,dtype=np.float64)
# parametrizacion
X = np.linspace(0.0,2*np.pi,nump+1)
# cordenada x
puntos[0:nump] =np.cos(X[0:nump]) + 0.0*np.sin(2*X[0:nump])
# cordenada y 
puntos[nump:2*nump] = np.sin(X[0:nump]) + 0.0*np.sin(2*X[0:nump])

#================================================================================================# Curva Z-spline de n puntos zpline(p,d,n,m)
# p: puntos, d:dimension, n: segmentos de curva, m:continuidad
#================================================================================================

n:np.int32 = 1000
x1,y1 = zpline(puntos,dim,n,2)
x2,y2 = zpline(puntos,dim,n,1)
x3,y3 = zpline(puntos,dim,n,0)
plt.plot(x3,y3,lw=3,color="orange")
plt.plot(x2,y2,lw=3,color="red")
plt.plot(x1,y1,lw=3,color="blue")
plt.scatter(puntos[0:nump],puntos[nump:2*nump],marker='o', color='black')
plt.xlabel("coordenada x")
plt.ylabel("coordenada y")
plt.title("CUrva cerrada Z-spline en 2D")
plt.show()

