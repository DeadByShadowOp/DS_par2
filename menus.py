import login
import funcionesComunes
def menuUsuario (tipo,restaurante):
    print("1.- Listar Categorías De Platos")
    print("2.- Buscar Plato")
    print("3.- Cerrar Sesión")
    op = input("Ingrese su opción: ")
    if op == "1":
        funcionesComunes.listarCategoria()
        print("Mostrar platos de la categoría:")
        op2 = int(input("Seleccione una categoria: "))
        categoria = funcionesComunes.transformarClave(op2)
        lista1 = funcionesComunes.listarPlatillos(tipo,categoria,restaurante)
        op3 = int(input("Seleccione un plato: "))
        funcionesComunes.mostrarPlatillo(op3,lista1)


    elif op == "2":
        op2 = input("ingrese nombre del plato: ")
    else:
        print(5)
        #login.cerrarSesion()

def menuAdministradorRestaurante (restaurante):
    print("1.- Agregar Platillo")
    print("2.- Listar Platillos")
    print("3.- Listar Categorías De Platillos")
    print("4.- Cerrar Sesión")
    op = input("Ingrese su opción: ")
    if op == "1":
        print("algo")
    elif op == "2":
        funcionesComunes.listarPlatillo(restaurante)

    elif op == "3":
        funcionesComunes.listarCategoria()
    else:
        login.cerrarSesion()

def menuAdministrador ():
    print("1.- Agregar Restaurante")
    print("2.- Listar Restaurantes")
    print("3.- Agregar Usuario")
    print("4.- Cerrar Sesión")
    op = input("Ingrese su opción: ")
    if op == "1":
        print("algo")
    elif op == "2":
        print("1.- Listar Platillos")
        print("2.- Listar Categorías")
        op2 = input("Ingrese su opción: ")
        if op == "1":
            print("algo")
        else:
            funcionesComunes.listarCategoria()
    elif op == "3":
        print("algo")
    else:
        login.cerrarSesion()

