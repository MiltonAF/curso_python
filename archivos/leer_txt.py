#Usando open para abrir un archivo con un codificacion universal
archivo = open('archivos/texto.txt',encoding='UTF-8')
#leer archivo completo
#archivo = archivo_sin_leer.read()

#leer linea por lineas
linea = archivo.readlines()

#cerramos el archivo
archivo.close()
print(linea)