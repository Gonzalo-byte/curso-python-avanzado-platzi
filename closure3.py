def make_division_by(n):
    """[summary]

    funcion que contiene a la nested function y guarda el divisor n

    """
    def division(number):

        assert type(number) == int, " INGRESE UN NUMERO!"

        return number/n
    
    return division

def run():
    div_by5= make_division_by(5)
    print(div_by5(15))

if __name__ == '__main__':
    run()

