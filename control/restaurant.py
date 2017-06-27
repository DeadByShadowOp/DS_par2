from control import platillos, funcionesDeLectura
from modelado import restauranteClass

restauranteDic = {}
objectRestaurantDic = {}
key = []
listName = []
lisNumb = []


def listarNombre():
    a = 0
    for i,I in restauranteDic.items():
        a = a+1
        listName.append(I[1])
        lisNumb.append(a)

def mostrarListas():
    listarNombre()
    for i in range(len(lisNumb)):
        print(str(lisNumb[i]) + ".- " +listName[i])

def listarPlatillo(restaurante):
    for j, k in platillos.platillos.items():
        if k[4] == restaurante:
            print("Su seleccion es: ", k[1], "\n")
            print("La categoria es: ", k[5], "\n")
            print("Esta disponible: ", k[2], "\n")
            print("Es de tipo: ", k[3], "\n")
            print("\n \n <--------------------------> \n\n")

def iniciarRestaurantes():
    funcionesDeLectura.leerArchivo("dataAccess/restaurante.csv", restauranteDic, key)
    for i in range(len(key)):
        listTmp = restauranteDic.get(key[i])
        objectRestaurantDic.setdefault(key[i], restauranteClass.restaurante(listTmp[0], listTmp[1], listTmp[2],
                                                                            listTmp[3], listTmp[4], listTmp[5]))

def addRestaurant(id):
    mostrarListas()
