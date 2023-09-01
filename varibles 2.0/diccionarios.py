#creando un diccionario con dict
diccionario = dict(nombre="milton", apellido="felizzola")

#las listas no pueden ser claves  y usando fronzeset para meter conjunto
diccionario = {frozenset(["dalto","rancio"]): "jajaj"}

#Creando diccionario con fromkeys, valor por defecto none
diccionario = dict.fromkeys(["nombre", "apellido"])

#Creando diccionario con fromkeys, estableciendo el valor
diccionario = dict.fromkeys(["nombre", "apellido"], "no se")

print(diccionario)