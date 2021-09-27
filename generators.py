import time

def fibo_gen(max:int) -> int:
    n1 = 0
    n2 = 1
    counter = 0
    
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else: 
            aux = n1 + n2
            if max + 1 <= aux:
                break
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == '__main__':
    maxIter = int(input('Maximo valor a buscar:\n'))
    fibonacci = fibo_gen(maxIter)
    for element in fibonacci:
        print(element)
        time.sleep(0.1)