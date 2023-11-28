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

