import time

class FiboIter():
    def __init__(self, max=None) -> None:
        self.max = max + 1

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            if self.max <= self.aux:
            # return self.aux
                raise StopIteration
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

if __name__ == '__main__':
    maxIter = int(input('¿Hasta que numero deseas iterar?\n'))
    fibonacci = FiboIter(maxIter)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)