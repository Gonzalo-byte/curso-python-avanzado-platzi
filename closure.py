#nested functions: funciones anidadas
#closures: cuando una variable global es recordada por una funcion inferior, esto permite que si se borra la funcion superior o la variable global, la funcion inferior pueda seguir recordando el valor
# Aparecen en Clases con un solo metodo y en decoradores


def make_multiplier(x):

    def multiplier(n):
        return x*n
    
    return multiplier


t10 = make_multiplier(10)
t4 = make_multiplier(4)

print(t10(3))
print(t4(t10(2)))


