dic = {
    "nombre": "lucas",
    "apellido": "dalto",
    "sub": 10000
}


#nos devulve las claves del diccionario
claves = dic.keys()

#nos devuelve el valor de una clave
get_valor = dic.get("apellido")


#eliminamos un elemento
dic.pop("nombre")

#eliminamos todos los elementos
dic.clear()

#nos devuelve un elemento dict_item iterable
elemt = dic.items()

print(dic)