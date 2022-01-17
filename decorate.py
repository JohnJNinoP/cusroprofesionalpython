from datetime import datetime
def execute_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print(f"Pasaron {+ time_elapse.total_seconds()} Seguntos")
    return wrapper

@execute_time
def random_func():
    for _ in range(1,1000000):
        pass

@execute_time
def suma(a: int , b : int):
    return a + b

@execute_time
def saludo(name = "Cesar"):
    print(name)

random_func()
suma(5,5)
saludo()