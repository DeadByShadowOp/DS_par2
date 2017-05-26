import login
def menuUsuario ():
    print("1.- Listar Categorías De Platos")
    print("2.- Buscar Plato")
    print("3.- Cerrar Sesión")
    op = input("Ingrese su opción: ")
    if op == "1":
        print("algo")
    elif op == "2":
        print("algo")
    else:
        login.cerrarSesion()

def menuAdministradorRestaurante ():
    print("1.- Agregar Platillo")
    print("2.- Listar Platillos")
    print("3.- Listar Categorías De Platillos")
    print("4.- Cerrar Sesión")
    op = input("Ingrese su opción: ")
    if op == "1":
        print("algo")
    elif op == "2":
        print("algo")
    elif op == "3":
        print("algo")
    else:
        login.cerrarSesion()

def menuAdministrador ():
    print("1.- Agregar Restaurante")
    print("2.- Listar Restaurantes")
    print("3.- Agregar Usuario")
    print("4.- Cerrar Sesión")
    if op == "1":
        print("algo")
    elif op == "2":
        print("algo")
    elif op == "3":
        print("algo")
    else:
        login.cerrarSesion()

def 