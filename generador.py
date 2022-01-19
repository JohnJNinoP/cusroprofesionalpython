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

# Generator expression 

my_list = [0,1,4,7,9,10]
my_second_list = [x*2 for x in my_list] # list complehension 
my_second_gen = (x*2 for x in my_list) # generator expression 

