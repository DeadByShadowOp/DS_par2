import login
import funcionesComunes
import  platillos

def menuUsuario (logeado):
    print("1.- Listar Categorías De Platos")
    print("2.- Buscar Plato")
    print("3.- Cerrar Sesión")
    op = input("Ingrese su opción: ")
    if op == "1":
        funcionesComunes.listarCategoria()
        print("Mostrar platos de la categoría")
        op2 = int(input("Seleccione una categoria: "))
        categoria = funcionesComunes.transformarClave(op2)
        lista1 = funcionesComunes.mastrarPlatillos(logeado,categoria)
        op3 = int(input("Seleccione un plato: "))
        funcionesComunes.mostrarPlatillo(logeado,platillos.obtenerID(lista1[op3-1]))

    elif op == "2":
        print("1.- Por nombre: ")
        print("2.- Por descripción: ")
        op2 = input("ingrese su opción: ")
        if op2 == "1":
            op4 = input("Ingrese el nombre del plato: ")
            funcionesComunes.buscarPlato(op4,1)
            op6 = input("Quiere mostrar un plato y/n: ")
            if op6 == "y":
                op5 = input("ingrese nombre del plato a ver: ")
                funcionesComunes.mostrarPlatillo(logeado,platillos.obtenerID(op5))
            else:
                menuUsuario(logeado)
        elif op2 == "2":
            op4 = input("Ingrese la descripción del plato: ")
            funcionesComunes.buscarPlato(op4,8)
            op6 = input("Quiere mostrar un plato y/n: ")
            if op6 == "y":
                op5 = input("ingrese nombre del plato a ver: ")
                funcionesComunes.mostrarPlatillo(logeado, platillos.obtenerID(op5))
            else:
                menuUsuario(logeado)
        else:
            print("Opción erronea")

    else:
        login.cerrarSesion()

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

