from datetime import datetime


#-------------------------------decorador------------------------------------------------------------
def execution_time(func):

    def wrapper(*args, **kwargs):

        inicial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        exec_time = final_time - inicial_time

        print('pasaron: ' + str(exec_time.total_seconds()) + ' segundos...')
    return wrapper

#------------------------------func1
@execution_time
def random_func():
    for _ in range(1,100000000):
        pass

#------------------------------func2
@execution_time
def suma(num1: int,num2: int) -> int:
    resultado = num1 + num2
    
    return print(resultado)



if __name__ == '__main__':
    random_func()
    suma(5, 5)