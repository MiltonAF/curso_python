#cambial el tipo de dato de una columna
import pandas as pd
df = pd.read_csv('archivos_problemas/texto.csv')

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna
#print(type(df['edad'][0]))

# Eliminar espacios en blanco adicionales y realizar el reemplazo
df['nombre'] = df['nombre'].str.strip()  # Eliminar espacios en blanco adicionales
df['nombre'].replace('jose', 'julian', inplace=True)

# Imprimir la columna 'nombre' después del reemplazo
#print(df['nombre'])

#eliminamos filas con datos faltante
df = df.dropna()

#eliminamos filas repetidas
df = df.drop_duplicates()

#creando un CSV con los dataframe resultante (limpio)
df.to_csv('archivos_problemas/texto2.csv')

print(df)
