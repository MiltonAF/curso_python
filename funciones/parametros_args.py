#forma no optima de sumar valores
#def suma(lista):
#    num_sumados = 0
#    for num in lista:
#        num_sumados+= num
#    
#    return num_sumados

# res = suma([3,4,3,2,2])

#forma optima de sumar valores
def suma_total(num):
    return sum([*num])

res = suma_total([3,4,3,2,2]) 

# lo mismo pero utilizando el operador * como parametro (*args)
def suma(*num):
    return sum(num)



print(res)