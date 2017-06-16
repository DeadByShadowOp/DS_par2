from control import usuarios, funcionesComunes, restaurant
from modelado import usuarioClass, restauranteClass
tiposUsuarios = {3 :"usuario", 2: "administrador", 1: "adminRestaurante"}



def selectRol():
    print("1.- Administrador de restaurante")
    print("2.- Administrador de sistema")
    print("3.- Usuario regular")
    tmp = True
    while tmp:
        op = int(input("Seleccione el tipo de usuario: "))
        if (op > 0) and (op < 4):
            tmp = False
        else:
            print("Opción erronea")
    return tiposUsuarios.get(op)

class userAdmin(usuarioClass.userLogin):
    def __init__(self,id,nombre,password,rol):
        usuarioClass.userLogin(id,nombre,password,rol)


    def addUser(self):
        key = str(len(usuarios.key))
        while True:
            id = input("Ingrese la CI del nuevo usuario: ")
            if (id in usuarios.usuarios) == False:
                break
            else:
                print("CI de usuario ya existe ingrese una diferente")
                funcionesComunes.pausa()

        name = input("ingrese el nombre del nuevo usuario: ")
        while True:
            contrasena = input("Ingrese la pass del nuevo usuario: ")
            conPass = input("Confirme su contraseña: ")
            if conPass == contrasena:
                print("Confirmacion de contraseña exitosa")
                break
            else:
                print("Error no coinciden datos")
                funcionesComunes.pausa()
        rol = selectRol()
        print(rol)
        userTmp = [key,name,contrasena,rol]
        usuarios.usuarios.setdefault(key,userTmp)
        usuarios.key.append(key)
        if rol == tiposUsuarios.get(1):
            nameR = input("Ingrese el nombre de restaurante: ")
            dirR = input("Ingrese la dirección del restaurante: ")
            telR = input("Ingrese el telefono del nuevo restaurante: ")
            duenoR = input("Ingrese el nombre del dueño: ")
            platillos = []
            objResTmp = restauranteClass.restaurante(key,nameR,dirR,telR,duenoR,platillos)
            restaurant.objectRestaurantDic.setdefault(key,objResTmp)