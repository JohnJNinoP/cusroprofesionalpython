import time


def fibo_gen(max_gen:int):
    max = max_gen
    a , b = 0,1
    counter = 0
    while True:
        yield a
        a, b = b , a+b
        counter += 1
        if max == counter:
            break

fibo = fibo_gen(20)
for  element in fibo:
    print(element)
    time.sleep(1)