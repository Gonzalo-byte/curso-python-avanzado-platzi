# 1 instalo mypy para que me alerte de errores de tipado.
# 2 luego ejecuto el archivo con mypy nombre.py --check-untyped-defs


def is_palindrome(word: str)-> bool:

    """[summary]
    
    Funcion que determina si una palabra es palindromo o no.

    Arguments:
        word {str} -- [palabra a verificar]
    
    Returns:
        bool -- [True si es palindrome, False si no]
    """


    
    word = word.replace(" ","").lower()
    word_reverse = word[::-1]

    if word == word_reverse:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_palindrome('ana'))