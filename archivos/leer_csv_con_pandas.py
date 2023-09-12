import pandas as pd

# Usamos la funcion read_csv para leer el archivo csv
df = pd.read_csv('archivos/texto.csv')
df2 = pd.read_csv('archivos/texto.csv')

# Obteniendo los datos de la columna nombres
nombres = df['nombre']

#ordenamos el dataframes por edad
df_ordenado = df.sort_values('edad')

#ordenandolo de forma decendentes
df_ordenado = df.sort_values('edad',ascending=False)

#concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 fila con head()
primera_fila = df.head(3)

#accediendo a las ultimas 3 filas con tails()
ultima_fila = df.tail(3)

#accediendo a la cantidad de columna y filas con shape
filas, columnas = df.shape

#obteniendo data estadistico del datafranes
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30 con loc
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)