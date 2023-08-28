cad1 = "Hola soy Dalto"

cad2 = "Bienvenido Maquinola"

#Convierte a Mayuscula
Mayus = cad1.upper()

#Convierte a Minuscula
Minos = cad1.lower()

#Convierte la primera letra en mayuscula
Cap = cad1.capitalize()

#Buscamos una cadena en otra, si no hay concidencia devuelve -1
Buscar = cad1.find("s")

#Buscamos una cadena en otra, si no hay concidencia lanza una excepcion
busqueda_index = cad1.index("a")

#si es numerico devuelve True, si no devuelve false
es_numerico = cad1.isnumeric()

#si es alfanumerico nos devuelve True y si no nos devuelve False
es_alfanumerico = cad1.isalpha()

#Contamos el numero de veces que existe una cadena dentro de la cadena
contar = cad1.count("a")

#Funcion para saber la longitud de la cadena, cuenta la cantidad de caracteres de la cadena
longitud = len(cad1)

#Verificamos si una cadena empiza con una cadena dada, si es asi devuelve True de lo contrario devuelve False
empieza_con = cad1.startswith("Hola")

#Verificamos si una cadena termina con una cadena dada, si es asi devuelve True de lo contrario deviuelve False
termina_con = cad1.endswith("Dalto")

#Remplaza un pedazo de la cadena, si encutra el valor 1 lo remplaza por el valor 2 de lo contrario la cadena se mantiene igual
cad_nueva = cad1.replace("la","lu")

#Separamos cadena con teniendo la cadena dada
separar = cad1.split("a")

print(separar)
