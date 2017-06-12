diccionarioCategoria = dict()
#diccionarioCategoria = {}
keyC = []
from control import platillos

def mastrarPlatillos(logeado,categoria):
    I = 1
    listTmp = []
    if  logeado.rol == "usuario":
        for j,k in platillos.platillos.items():
            if k[5] == categoria:
                print(I, ".- ", k[1],"esta disponible: ",k[2]," es de tipo: ",k[3]," se encuentra en el restaurante: ",k[4])
                listTmp.append(k[1])
                I = I + 1
    elif logeado.user.rol == "adminRestaurante":
        for j,k in platillos.platillos.items():
            if (logeado.rest.nombre == k[4]) and (k[5] == categoria):
                print(I, ".- ", k[1], "esta disponible: ", k[2], " es de tipo: ", k[3],
                      " se encuentra en el restaurante: ", k[4])
                listTmp.append(k[1])
                I = I + 1
    return listTmp

def mostrarPlatillo(logeado,id):
    print(logeado.rol)
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
        elif logeado.user.rol == "adminRestaurante":
            if (k[4] == logeado.rest.nombre) and (k[0] == id):
                print("Su seleccion es: ", k[1])
                print("Esta disponible: ", k[2])
                print("Es de tipo: ", k[3])
                print("Lo encuentra en el restaurante: ", k[4])
                print("La categoria es: ", k[5])
                print("Los ingredientes son: ", k[6])
                print("Imagenes: ", k[7])
                print("Descripción: ", k[8])

def pausa():
    pause = input("Pulse ENTER para continual")