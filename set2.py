my_set = {1,2,3,6,"hola"}

#anado un solo elemento
my_set.add(1)

#podemos ver que no añade el 1 ya que se encontraba en el set
print(my_set)

#anado multiples elementos en un ITERABLE
my_set.update([1,3,5,6,"chau"])

#se observa que solo añade aquellos que no estaban en el set

print(my_set)


# algo curioso es que siempre que ejecuto los muestra en distinto orden
#pero si hago un ciclo for imprime siempre igual
for i in range(10):
    print(my_set)


#para borrar elementos puedo usar remove o discard, la unica diferencia es que con discard si el valor que le paso no está, me retorna el mismo set sin dar error

my_set.remove(1)
print(my_set)

my_set.discard(12)
print(my_set)

#borrar elemento aleatorio: pop()

my_set.pop()