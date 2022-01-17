from multiprocessing.context import set_spawning_popen
import re
import time

class FiboIter:

    def __init__(self, max = 10):
        self.max = max

    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.counter = 0
        return self

    def __next__(self):
        
        if self.counter == 0:
            self.counter +=1
            return self.num1
        elif self.counter == 1:
            self.counter += 1
            return self.num2
        elif self.counter == self.max:
            raise StopIteration
        else:
            self.aux = self.num1 + self.num2
            #self.num1 = self.num2
            #self.num2 = self.aux
            self.num1 , self.num2 = self.num2 , self.aux
            self.counter += 1
            return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter(5)
    for element in fibonacci:
        print(element)
        time.sleep(1)

