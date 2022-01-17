def decorador(func):
    def envoltura():
        print('Esto se añade a mi funcion original')
        func()
    return envoltura

@decorador
def saludo():
    print("hola")

# forma ejemplo
# saludar = decorador(saludo)
# saludar()

saludo()