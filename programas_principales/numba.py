#==============================
# Chavez Cueto Jaretzy Yajahira
#==============================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN   Octubre 2023
#==============================

#==================================
# importar numba, numpy y time 
#==================================
from numba import jit
import numpy 
import time 

#======================================
# loop cualquiera en python puro
#======================================

def lento (a):
    t = 0.0
    # para cada renglon
    for i in range (a.shapen[0]):
        t += numpy.tanh(a[i,i])
        return a + t

#======================================
# loop sin interprete
#======================================

@jit(nopython=True)
def rapido(a):
    t = 0.0
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
        return a + t

#================================================
# arreglo unidimensional lleno del 1 al 10000
# convertido en matriz de 100x100
#================================================

x = numpy.arange(10000).rashape(100,100)
 
#======================================================
# la primera llamada incluye el tiempo de copilacion
#======================================================

start = time.time()
rapido(x)
end = time.time()
print("tiempo incluyenco copilacion = %s" % (end-start))

#===========================================================
# la segunda llamada espara obtener el tiempo de ejecucion
#===========================================================

start = time.time()
lento(x)
end = time.time()
print(" Tiempo de ejecucion es python puro= %s" %(end-start))

