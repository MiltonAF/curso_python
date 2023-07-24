#Creando una lista (se pueden modificar)
lista = ["hola", "milton", True, 9.09]

#Creando una tupla (no se pueden modificar)
tupla = ("mmmm", "sdwd", 12, False)

#Esto es valido
lista[3] = "otro dato"

#Esto no es valido
#tupla[3] = "otro dato"

#Creando un conjunto {set} | no se puede acceder al documento por su indice | no almacena datos duplicados | son datos desornenados
conjunto = {"1","2","3"}

#print(conjunto[3]) -> no puede acceder al elemento

#Creando un diccionario (dict)
diccionario = {
    "id": 123,
    "nombre": "milton",
    "edad": 12    
    
}

print(tupla)