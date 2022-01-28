import time

def fibo_gen(max: int = None):
    n1, n2  = 0, 1
    
    while not max or max > n1:
        yield n1
        n1, n2 = n2, n1+ n2


if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(0.05)
