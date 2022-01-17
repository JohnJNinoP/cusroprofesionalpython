from operator import ne
from tkinter import N


def my_gen():
     """Un ejemplo de generadores"""

     print("Hello word")
     n = 0
     yield n

     print("hello heaven")
     n = 1
     yield n

     print("hello hell")
     n = 2
     yield n


a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))

