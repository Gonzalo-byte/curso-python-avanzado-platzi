def recubrimiento(func):
    '''
    decorador que recubre un string
    '''
    def wrapper(texto: str)-> str:
        print(' ' + '-'*len(texto))
        print('|'+(' '*len(texto))+'|')
        print('|' + texto + '|')
        print('|'+(' '*len(texto))+'|')
        print(' ' + '-'*len(texto))
    return wrapper

@recubrimiento
def envolver(texto):
    return texto


if __name__ == '__main__':
    envolver(input('Ingrese la palabra a envolver: '))


        