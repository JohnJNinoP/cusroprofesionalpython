def mayusculas(func):
    def envoltura(texto,mensaje):
        texto = texto.upper()
        # return func(texto).upper()
        return func(texto,mensaje)
    return envoltura

@mayusculas
def mensaje(nombre,mensaje):
    return f'{nombre} {mensaje}'


print(mensaje('cesar','resibiste un mensaje'))