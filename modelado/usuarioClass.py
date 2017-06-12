import re

from control import platillos

diccionarioCategoria = dict()
keyC = []
keyCSinRepeticiones = []

def transformarClave(op):
    for i in range (len(keyC)):
        if (keyC[i] in keyCSinRepeticiones) == False:
            keyCSinRepeticiones.append(keyC[i])
    bandera = True
    while bandera:
        if (op-1) < len(keyCSinRepeticiones):
            bandera = False
            return keyCSinRepeticiones[op - 1]
        else:
            op = int(input("Categoria erronea, seleccione una opcion correcta: "))


def buscarPlato(nombre,pos):
    bandera = 0
    op1 = ".*"+nombre+".*"
    for j,k in platillos.platillos.items():
        if re.search(op1, k[pos]):
                bandera = 1
                print("Nombre: ", k[1], "\n")
                print("Servido: ", k[2], "\n")
                print("Tipo: ", k[3], "\n")
                print("Restaurante: ", k[4], "\n")
    return bandera

def listarCategoria():
    tmp = platillos.platillos
    key = platillos.key
    I = 1
    for i in range(len(key)):
        lista2 = tmp.get(key[i])
        diccionarioCategoria.setdefault(lista2[5], 0)
        keyC.append(lista2[5])
        if lista2[5] in diccionarioCategoria:
            diccionarioCategoria[lista2[5]] = diccionarioCategoria.get(lista2[5]) + 1
    for i, k in diccionarioCategoria.items():
        print(I, ".- Categoria: ", i, "\t\tnumero de platos ", k)
        I = I + 1

class userLogin:

    id = ""
    nombre = ""
    password = ""
    rol = ""
#    restaurante = ""

    def __init__(self,id,nombre,password,rol):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.rol = rol