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

sr=s1-s2 #diferencia de conjuntos
print(sr)

sp=s2-s1
print (sp)

ss=s1^s2 #diferencia simetrica
print(ss)

#=============================
# Uso de diccionarios 
#=============================
capitals = {"USA":"Washington D.C","France":"paris", "India" : "New Delhi"}
print (capitals)

#========================
# llave:valor
#========================
#diccionario vacio
d={}

#llave entera, valor string
numNames={1:"One", 2:"Two", 3:"Three"}

#llave real, valor string
decNames={1.5:"One and Half", 2.5:"Two and Half" , 3.5:"Three and half"}

#llave tupla, valor string
items={("parker","reynolds","camlin"):"pen",("Lg","Whirlpool","Samsung"):"Refrigerator"}

#llave string, valor int
romanNums = {'I':1 , 'II':2 , 'III':3 , 'IV':4 ,'V':5}

print (romanNums)
print (romanNums["I"])

print (capitals.get("India"))
print (capitals.get("india"))

#reportar llave y valor
for k in capitals:
    print("key= "+k+",Value= " + capitals[k])

#Nuevo dato para el diccionario 
capitals ["Mexico"] = "CDMX"
print (capitals)

#BOrrar dato del diccionario 
del capitals ["Mexico"]

#Borrar todo el diccionario 
del capitals

#Reportar llaves
print (romanNums.keys ())

#reportar valores
print(romanNums.values())

#juicio de llave (esta o no esta la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)

