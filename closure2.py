#Hola 3-> HolaHolaHola
#gon 2-> gongon


def make_repeater_of(n):
    """[summary]

    funcion que contiene a la nested function y guarda repetidor n

    """
    def repeater(string):

        assert type(string) == str, "Solo puede utilizar cadenas"
        return n * string

    return repeater

def run():
    repeat5 = make_repeater_of(5)
    print(repeat5("hola-"))



if __name__=='__main__':
    run()
