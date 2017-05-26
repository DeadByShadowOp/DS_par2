import platillos
import usuarios
diccionarioCategoria = dict()
diccionarioCategoria = {}
keyC = []
def listarCategoria():
    tmp = dict()
    tmp = platillos.platillos
    key = platillos.key
    lista = []
    lista2 = []
    I = 1
    for i in range(len(key)):
        lista2 = tmp.get(key[i])
        diccionarioCategoria.setdefault(lista2[5], 0)
        keyC.append(lista2[5])
        if lista2[5] in diccionarioCategoria:
            diccionarioCategoria[lista2[5]] = diccionarioCategoria.get(lista2[5]) + 1
    for i,k in diccionarioCategoria.items():
        print(I,".- Categoria: ", i ,"\t\tnumero de platos ",k)
        I = I+1

def transformarClave(op):
    return keyC[op-1]

def listarPlatillos (tipo,categoria,restaurante):
    I = 1
    listTmp = []
    if tipo == "usuario":
        for j,k in platillos.platillos.items():
            if k[5] == categoria:
                print(I, ".- ", k[1])
                listTmp.append(k[1])
                I = I + 1
    else:
        for j,k in platillos.platillos.items():
            if (restaurante == k[4]):
                print(k[4])
    return listTmp

def mostrarPlatillo(op,lisTmp):
    for j, k in platillos.platillos.items():
        if lisTmp[op-1] == k[1]:
            print("Su seleccion es: ",k[1],"\n")
            print("Esta disponible: ", k[2], "\n")
            print("Es de tipo: ", k[3], "\n")
            print("Lo encuentra en el restaurante: ", k[4], "\n")
            print("La categoria es: ", k[5], "\n")
            print("Los ingredientes son: ", k[6], "\n")
            print("Imagenes: ", k[7], "\n")
            print("Descripción: ", k[8], "\n")

def listarPlatillo(restaurante):
    for j, k in platillos.platillos.items():
        if k[4] == restaurante:
            print("Su seleccion es: ", k[1], "\n")
            print("La categoria es: ", k[5], "\n")
            print("Esta disponible: ", k[2], "\n")
            print("Es de tipo: ", k[3], "\n")
            print("\n \n <--------------------------> \n\n")