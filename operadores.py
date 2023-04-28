#================================
# conjunto en python
#================================
even_nums={2, 4, 6, 8, 10} #conjunto de numeros pares
print (even_nums)
# el bool no es parte del conjunto 
emp = {1, 'steve', 10.5, True } #conjunto de diferentes objetos 
print(emp)
nums = {1,2,2,3,4,4,5,5}
print (nums)

#==================================
# convertir secuencia a conjunto 
# no lo genera en orden 
#==================================

s = set ('hello')
print(s)
s = set ((1,2,3,4,5)) #tupla a conjunto
print (s)

#================================================
# de diccionario a conjunto: conjunto de llaves
#================================================
d = {1: 'one', 2:'two'}
s = set (d)
print(s)
s.add(100)
print(s)
s.update(nums)
print(s)
s.remove(100)
print(s)
s1={1,2,3,4,5}
s2={4,5,6,7,8}

su= s1|s2 #union
print(su)

si= s1&s2 #interseccion
print(si)

