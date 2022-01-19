from turtle import write_docstringdict


my_set = {3,4,5}
print(my_set)
my_set2 = {"Hola",23.3,False,True}
print(my_set2)

my_set3 = {3,3,2}
print(my_set3)

# Error no es un set por que es mutable 
# my_set4 = {[1,2,3]}

empty_set = {}
print(type(empty_set))

empty_set = set()
print(type(empty_set))

# casting to sets
print("Casting set")
my_list = [1,1,2,3,4,4,5]
my_set = set(my_list)

print(my_set)

my_tuple = ("Hola" , "Hola","Hola", 1)
my_set2 = set(my_tuple)
print(my_set2)

#  add element to the sets
print("Add element to set")
my_set = {1,2,3}
print(my_set)

my_set.add(4)
print(my_set)

my_set.update([1,2,5])
print(my_set)

my_set.update((1,7,2), {6,8})
print(my_set)

# Remove element to sets
print("remove Element to set")
my_set = {1,2,3,4,5,6,7}
print(my_set)

my_set.discard(1)
my_set.discard(10) # element not find
print(my_set)

my_set.remove(2)
# my_set.remove(12) error the element not found

# Remove element random

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)


# union in sets
print("sets union")
my_set = {3,4,5}
my_set2 = {5,6,7}
my_set_union = my_set | my_set2
print(my_set_union)

# intercession sets
print("Intercession sets")
my_set = {3,4,5}
my_set2 = {5,6,7}
my_set_intercession = my_set & my_set2
print(my_set_intercession)
# different sets
print("different sets")
my_set = {3,4,5}
my_set2 = {5,6,7}
my_set_different = my_set - my_set2
print(my_set_different)

# remove duplicate sets values 

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    
    return without_duplicates

random_list = [1,1,2,2,4]
print(remove_duplicates(random_list))
