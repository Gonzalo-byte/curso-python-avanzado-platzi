def mayusculas(func):
    def envoltura(texto):
        print('ejecutando envoltura')
        return func(texto).upper()
    return envoltura


@mayusculas
def mensaje(texto):
    return f'Hola {texto}, recibiste un mensaje'


if __name__ == '__main__':
    print(mensaje('gonzalo'))