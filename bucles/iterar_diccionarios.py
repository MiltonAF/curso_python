diccionario = {
    'nombre': 'lucas',
    'apellido': 'dalto',
    'subs': 1000000
}

#recorriendo diccionario para obtener las claves
for key in diccionario:
    print(f'la clave es: {key}')

#recorriendo diccionario con item para obtener las claves y los valores
for value in diccionario.items():
    key = value[0]
    valor = value[1]
    print(f'la clave es: {key} y el valor es: {valor}')