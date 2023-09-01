#Creando un conjunto con set
conjunto =  set(["dato1", "dato2"])

#Metiendo un conjunto en otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato4", "dato5"}

print(conjunto2)

#Teoria de conjunto
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Verificar si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#Verificar si hay un numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)