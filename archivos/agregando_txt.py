with open('archivos/texto.txt','a',encoding='UTF-8') as archivo:
    #Agregando un linea en el archivo con append
    archivo.write('\n')
    #usasno un bucle para agregar varias lineas
    
    [archivo.write(f'linea {i+1} agregada \n') for i in range(5)]
    