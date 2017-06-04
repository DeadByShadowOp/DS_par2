import funcionesDeLectura
import  restauranteClass
restauranteDic = {}
objectRestaurantDic = {}
key = []


def iniciarRestaurantes():
    funcionesDeLectura.leerArchivo("restaurante.txt", restauranteDic, key)
    for i in range(len(key)):
        listTmp = restauranteDic.get(key[i])
        objectRestaurantDic.setdefault(key[i],restauranteClass.restaurante(listTmp[0],listTmp[1],listTmp[2],
                                                                                    listTmp[3],listTmp[4],listTmp[5]))

