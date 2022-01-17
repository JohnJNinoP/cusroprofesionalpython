my_list = [1,2,3,4,5]
my_iter = iter(my_list)

print(next(my_iter))

while True   :
    try:
        element = next(my_iter)
        print(element)
    except:
        break