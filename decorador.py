def decora(f):
    def envuelve():
        print('estoy a punto de ejecutar una funcion')
        f()
        print('termine de ejecutar un programa')
    return envuelve

@decora
def hola():
    print('hola mundo')
    
hola()