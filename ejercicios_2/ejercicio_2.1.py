#Falto el profesor y los alumnos van a armar la clase

#Primero vamos a perdir el nombre y la edad de cada alumno
#Luego determinarmos quien es el mayor y el menor, el mayor sera el profesor y el menor el asistente

#funcion para obtener el profesor y el asistente 
def get_compañero(cant_compañero):
    #creamos un lista vacia para almacenar los datos registados
    compañeros = []
    
    #ejecutamos el for para pedir la informacion de los compañeros
    for i in range(cant_compañero):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input('ingrese la edad del compañero: '))
        print('----------------------------------------------')
        compañero = (nombre,edad)
        
        #agregamos la informacion a la lista
        compañeros.append(compañero)
        
    #orgnadomos la lista de menor a mayor por la edad    
    compañeros.sort(key=lambda x : x[1])
    
    #compañero[x] devuelve una tupla con (nombre, edad) y despues accederemos al nombre
    #para definir la asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    # Retornamos una tupla
    return asistente, profesor


cant_comp = int(input('dame la cantidad de compañeros asistidos: '))

# Desempaquetamos lo que nos retorna la funcion
asistente, profesor = get_compañero(cant_comp)

# Mostramos el resultado
print(f'el profesor es {profesor} y su asistente es {asistente}')