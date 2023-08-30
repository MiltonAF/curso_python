#Creamos una lista con list()
lista = list(["hola",23,"cimo"])

#Cremanos una lista sin list()
lista2 = [23,45,343,553,223,2454,3]

#Devuelve la cantidad de elemento de la lista
log = len(lista)

#Agregando un elemento a la lista con append
lista.append(90)

#Agregando un elemento a la lista  en un indice especifico con insert
lista.insert(2,"coche") 

#Agregando varios elementos a la lista con extends
lista.extend(["JAJJA", True, 2303])

#Eliminando un elemento de la lista por su indice con pop
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente

#Eliminamos un elemento de la lista por su valor
lista.remove(True)

#Eliminando todos los elementos de la lista
lista.clear()

#Ordenamos la lista de forma ascedentes, si usamos el parametro reverse = True los ornamos de forma al reves
lista2.sort()

#invirtiendo los elementos de una lista
lista2.reverse()

print(lista2)