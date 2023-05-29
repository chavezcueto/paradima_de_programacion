#===================================================
# listas
# las listas pueden ser de objetos diferentes
#===================================================
miprimeralista = [] #lista vacia
print (miprimeralista)

#===================================0
# llenado de lista
#===================================
miprimeralista = [1, "Javier", 1.34, "bosco", "angek", "abigail", True]
print (miprimeralista)

#=======================================
# list: hacer una lista
# range(i,j): secuencia de i hasta j-1
#=======================================

nums= list(range(1,61))
for i in nums:
    print (i)

#===========================================
# incluir nuevos elementos en la lista 
#===========================================
nums.append(61)
nums.append(62)
nums.append(61)
print (nums)

#==============================================
# quitar lemento de la lista
#==============================================
nums.remove(61)
print (nums)

#==============================================
# quitar elemento con indice i
#==============================================
i = 61
del nums[i]
print (nums)

#==============================================
# borrar la lista
#==============================================
del nums

#==============================================
# sumar listas 
#==============================================

L1 = [1,2,3]
L2 = [4,5,6]
print (L1+L2)

#===================================
# Llenado a mano 
#===================================
potencial =[]
for i in range(0,10000):
    potencial.append(float(i))
print (potencial[100])

