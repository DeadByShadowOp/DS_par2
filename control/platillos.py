from control import funcionesDeLectura
from modelado import categoriaClass

platillos = dict()
platillos = {}
key = []
listCategoria = categoriaClass.categoria("0","fantasma")
listCategoria.cargarCategorias()

estructura = ["ID","NOMBRE","SERVIDO","TIPO","RESTAURANT","CATEGORIA","INGREDIENTES","IMAGENES","DESCRIPCION"]
funcionesDeLectura.leerArchivo("dataAccess/platillos.txt", platillos, key)

def obtenerID(nombre):
    for j,k in platillos.items():
        if k[1] == nombre:
            return j


def generarKey():
    return len(key)

def servido():
    bandera = True
    print("¿El platillo es: ?")
    while bandera:
        print("1.- Caliente")
        print("2.- Frío")
        op = input("Ingrese una opción: ")
        if op == "1":
            bandera = False
            return "Caliente"
        elif op == "2":
            bandera = False
            return "Frío"
        else:
            print("Opción erronea vuelva a intentarlo")


def tipo():
    bandera = True
    print("¿El platillo es de tipo: ?")
    while bandera:
        print("1.- Aperitivo")
        print("2.- Plato fuerte")
        print("3.- Postre")
        op = input("Ingrese su opción: ")
        if op == "1":
            return "Aperitivo"
        elif op == "2":
            return "Plato fuerte"
        elif op == "3":
            return "Postre"
        else:
            print("Opción erronea vuelva a intentarlo")

def seleccionCategoria():
    bandera = True
    while bandera:
        listCategoria.mostrarCategorias()
        op = input("Seleccione una categoria: ")
        if listCategoria.hashExiste(op) == True:
            objTmp = listCategoria.getCategoria(op)
            bandera = False
        else:
            print("Categoria no existe")
    return objTmp.nombre

def addPlatillo(key,restaurante):
    #version 2.0
    tmp =[]
    tmp.append(key)
    tmp.append(input("Ingrese el nombre del plato: "))
    tmp.append(servido())
    tmp.append(tipo())
    tmp.append(restaurante)
    tmp.append(seleccionCategoria())
    tmp.append(input("Ingrese los ingredientes del plato: "))
    tmp.append(input("Ingrese las imagenes del plato: "))
    tmp.append(input("Ingrese la descripción del plato: "))
    platillos.setdefault(tmp[0],tmp)

def getPlatillo (id):
    return platillos.get(id)

def modificarPlatillo(ide):
    #Version 2.0
    tmp = getPlatillo(ide)
    tmp[1] = modNombre(tmp[1])
    tmp[2] = modServido(tmp[2])
    tmp[3] = modTipo(tmp[3])
    tmp[5] = modCategoria(tmp[5])
    tmp[6] = modIngredientes(tmp[6])
    tmp[7] = modImagenes(tmp[7])
    tmp[8] = modDescripcion(tmp[8])
    platillos[ide] = tmp


def listarCategorias():
    tmp = []
    for j,k in platillos.items():
        if (k[5] in tmp) == False:
            tmp.append(k[5])
    return tmp

def modNombre(parametro):
    op = input("Ingrese el nuevo nombre del plato, o deje blanco para mantener el mismo: ")
    if op != "":
        return op
    else:
        return parametro

def modCategoria(parametro):
    op = input("Escriba Y para modificar la categoria o deje blanco para mantener el mismo: ")
    if op != "":
        return seleccionCategoria()
    else:
        return parametro

def modIngredientes(parametro):
    op = input("Ingrese los nuevos ingredientes del plato, o deje blanco para mantener el mismo: ")
    if op != "":
        return op
    else:
        return parametro

def modImagenes(parametro):
    op = input("Ingrese las nuevas imagenes del plato, o deje blanco para mantener el mismo: ")
    if op != "":
        return op
    else:
        return parametro

def modDescripcion(parametro):
    op = input("Ingrese la descripción del plato, o deje blanco para mantener el mismo: ")
    if op != "":
        return op
    else:
        return parametro

def modTipo(parametro):
    bandera = True
    print("¿El platillo es de tipo: ?")
    while bandera:
        print("1.- Aperitivo")
        print("2.- Plato fuerte")
        print("3.- Postre")
        op = input("Ingrese su opción: ")
        if op == "1":
            return "Aperitivo"
        elif op == "2":
            return "Plato fuerte"
        elif op == "3":
            return "Postre"
        elif op == "":
            return parametro
        else:
            print("Opción erronea vuelva a intentarlo")

def modServido(parametro):
    bandera = True
    print("¿El platillo es: ?")
    while bandera:
        print("1.- Caliente")
        print("2.- Frío")
        op = input("Ingrese una opción: ")
        if op == "1":
            bandera = False
            return "Caliente"
        elif op == "2":
            bandera = False
            return "Frío"
        elif op == "":
            return parametro
        else:
            print("Opción erronea vuelva a intentarlo")