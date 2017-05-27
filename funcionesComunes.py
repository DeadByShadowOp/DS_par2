import platillos
import usuarios
import  re
import usuarioLogeado
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

def mastrarPlatillos(logeado,categoria):
    I = 1
    listTmp = []
    if  logeado.rol == "usuario":
        for j,k in platillos.platillos.items():
            if k[5] == categoria:
                print(I, ".- ", k[1],"esta disponible: ",k[2]," es de tipo: ",k[3]," se encuentra en el restaurante: ",k[4])
                listTmp.append(k[1])
                I = I + 1
    elif logeado.rol == "adminRestaurante":
        for j,k in platillos.platillos.items():
            if (logeado.restaurante == k[4]):
                print(I, ".- ", k[1], "esta disponible: ", k[2], " es de tipo: ", k[3],
                      " se encuentra en el restaurante: ", k[4])
                listTmp.append(k[1])
                I = I + 1
    return listTmp

def mostrarPlatillo(logeado,id):
    for j, k in platillos.platillos.items():
        if logeado.rol == "usuario":
            if id == k[0]:
                print("Su seleccion es: ", k[1], "\n")
                print("Esta disponible: ", k[2], "\n")
                print("Es de tipo: ", k[3], "\n")
                print("Lo encuentra en el restaurante: ", k[4], "\n")
                print("La categoria es: ", k[5], "\n")
                print("Los ingredientes son: ", k[6], "\n")
                print("Imagenes: ", k[7], "\n")
                print("Descripción: ", k[8], "\n")
        elif logeado.rol == "adminRestaurante":
            if (k[4] == logeado.restaurante) and (k[1] == id):
                print("Su seleccion es: ", k[1])
                print("Esta disponible: ", k[2])
                print("Es de tipo: ", k[3])
                print("Lo encuentra en el restaurante: ", k[4])
                print("La categoria es: ", k[5])
                print("Los ingredientes son: ", k[6])
                print("Imagenes: ", k[7])
                print("Descripción: ", k[8])



def listarPlatillo(restaurante):
    for j, k in platillos.platillos.items():
        if k[4] == restaurante:
            print("Su seleccion es: ", k[1], "\n")
            print("La categoria es: ", k[5], "\n")
            print("Esta disponible: ", k[2], "\n")
            print("Es de tipo: ", k[3], "\n")
            print("\n \n <--------------------------> \n\n")


def buscarPlato(nombre,pos):
    op1 = ".*"+nombre+".*"
    for j,k in platillos.platillos.items():
        if re.search(op1, k[pos]):
                print("Nombre: ", k[1], "\n")
                print("Servido: ", k[2], "\n")
                print("Tipo: ", k[3], "\n")
                print("Restaurante: ", k[4], "\n")