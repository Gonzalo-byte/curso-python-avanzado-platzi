# reto : eliminar duplicados con sets y sin usar un ciclo for

list1 = [1,1,2,2,3,4,6,7,7]

def eliminarDuplicados():
    return list(set(list1))

if __name__ == '__main__':
    print(eliminarDuplicados())
