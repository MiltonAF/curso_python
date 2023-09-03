
#Creando una funcion simple
#def saludar():
#   print('hola lucas, mi maestro ¿como andas?')
    

#ejecutanto la funcion simple
#saludar()

#Creando una funcio con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == 'mujer':
        adj = 'Maestra'
    else:
        adj = 'maestro'
    
    print(f'Hola {nombre}, mi {adj} ¿como andas?')
    

saludar('liucas', 'hombre')

#Crear una funcion que nos retornes valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num

#desempaquetando la funcion
password, num = crear_contraseña_random(9)

#mostrando los resultados obtenidos y los datos usados para obtenerlos
print(f'tu contraseña es: {password}')
print(f'el numero para crearla fue: {num}')