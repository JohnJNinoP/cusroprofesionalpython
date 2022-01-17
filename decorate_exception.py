def execute_exception(func):
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except:
            print("an error has occurred, count the system administrator")
    return wrapper

@execute_exception
def division(a:int):
    b= 10/a
    print(b)


#Error controlado
division(0)

division(1)