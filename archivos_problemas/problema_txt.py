# 2 listas, una con nombre otra con apellidos
nombre = ['milton', 'andres', 'camila', 'valentina', 'eduardo']
apellido = ['martinez', 'torres', 'vuege', 'cardenas', 'montiel']

# Registrar esta informacion en un TXT de forma optima
with open('archivo_problemas_resuelto/nombre_y_apellido.txt', 'w') as arch:
    arch.writelines('los datos son: \n\n')
    [arch.writelines(f'nombre: {n}.\napellido: {a}.\n--------------\n') for n,a in zip(nombre,apellido)]