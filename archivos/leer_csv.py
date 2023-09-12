import csv

with open('archivos/texto.csv') as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)