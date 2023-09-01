#Creamos una lista para iterar
animales = ["perro", "gato", "loro", "coodrilo"]
numero = [10,23,21,24]


#recorremos la lista animales
for animal in animales:
    print(animal)
    
#recorriendo la lista numero yn multiplicando cada valor por 10
for num in numero:
    res = num * 10
    print(f'numero es: {res}')
    
#iterando dos listas del mismo tañano al mismo tiempo   
for num, animal in zip(numero, animales):
    print(f'recorriendo lista 1: {num}')
    print(f'recorriendo lista 2: {animal}')
    
    
#forma no optima de recorrer una lista con su indice, NO FUNCIONA EN CONJUNTOS
for num in range(len(numero)):
    print(numero[num])
    
    
#forma correcta de reccorer una lista con su indice
for num in enumerate(numero):
    print(f'el indice es: {num[0]} y el valor es: {num[1]}')
    

#usando el for/else
for num in numero:
    print(f'ejecutamos el ultimo bucle: valor actual: {num}')
else:
    print('el bucle termino')
    
    
#TODO LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL PARA TUPLAS Y CONJUNTOS