frutas = ['banana', 'manzana', 'ciruela', 'pera', 'naranja', 'granada', 'durazno']
cadena = 'Hola Dalto'
numero = [2,5,8,10]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'me voy a comer una {fruta}')
    
#evitando que el bucle siga ejecutandose
for fruta in frutas:
    print(f'me voy a comer una {fruta}')
    if fruta == 'pera':
        break
   
    

#Recorre una cadena de texto
for letra in cadena:
    print(letra)


#for en una linea de codigo (duplicamos los numeros)
numero_duplicado = [x*2 for x in numero]
print(numero_duplicado)