import funcionesDeLectura
platillos = dict()
platillos = {}
key = []
estructura = ["ID","NOMBRE","SERVIDO","TIPO","RESTAURANT","CATEGORIA","INGREDIENTES","IMAGENES","DESCRIPCION"]
funcionesDeLectura.leerArchivo("platillos.txt",platillos,key)

def obtenerID(nombre):
    for j,k in platillos.items():
        if k[1] == nombre:
            return j


def generarKey():
    return len(key)

def addPlatillo(key):
    tmp =[]
    tmp.append(key)
    tmp.append(input("Ingrese el nombre del plato: "))
    tmp.append(input("El plato esta servido SI/No: "))
    tmp.append(input("Ingrese el tipo del plato: "))
    tmp.append(input("Ingrese el restaurante: "))
    tmp.append(input("Ingrese la categoria: "))
    tmp.append(input("Ingrese los ingredientes del plato: "))
    tmp.append(input("Ingrese las imagenes del plato: "))
    tmp.append(input("Ingrese la descripción del plato: "))
    platillos.setdefault(tmp[0],tmp)

def getPlatillo (id):
    return platillos.get(id)

def modificarPlatillo(ide):
    tmp = getPlatillo(ide)
    tmp[1] = input("Ingrese el nombre del plato: ")
    tmp[2] = input("El plato esta servido SI/No: ")
    tmp[3] = input("Ingrese el tipo del plato: ")
    tmp[4] = input("Ingrese el restaurante: ")
    tmp[5] = input("Ingrese la categoria: ")
    tmp[6] = input("Ingrese los ingredientes del plato: ")
    tmp[7] = input("Ingrese las imagenes del plato: ")
    tmp[8] = input("Ingrese la descripción del plato: ")
    platillos[ide] = tmp


def listarCategorias():
    tmp = []
    for j,k in platillos.items():
        if (k[5] in tmp) == False:
            tmp.append(k[5])
    return tmp