from modelado import restauranteClass

a = restauranteClass.restaurante("0924995428", "hola", "55866", "555585", "55589630", "1 2 3 4 5 6 7 8 9")
print("hola mundo" + a.nombre)

#desde aqui es tu codigo scarlet
bandera = True
while bandera:
    print("1.- Iniciar juego")
    print("2.- Salir")
    op = input("Ingrese su opción: ")
    if op == "1":
        #aqui el codigo que lanza el juego
        print("algo")
    elif op == "2":
        bandera = False
    else:
        print("Opción invalida, vuelva a intentarlo")