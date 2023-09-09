#si el modulo estuviera dentro de la carpta de la misma ruta
#import funciones_buenas.saludos as sal

import sys

sys.path.append('/home/milt_adri/Documentos/Proyectos/curso_python/funciones_buenas')

import saludos

print(saludos.saludar('Milton'))