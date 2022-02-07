#operar con sets

my_set = {1,2,3,4}
my_set2 = {4,5,6,7}

#union de 2 sets
my_set3 = my_set | my_set2
print(my_set3)

#union de coincidencias unicamente
my_set4 = my_set & my_set2
print(my_set4)


#interserccion o diferencias (quita del 1° todo lo que coincida en el 2°)

my_set5 = my_set - my_set2
print(my_set5)

#diferencia simetrica (se queda con los valores de ambos, menos los que se repiten)

my_set6 = my_set ^ my_set2
print(my_set6)