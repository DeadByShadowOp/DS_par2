from control import usuarios, restaurant
from modelado import asistenteClass
from modelado import usuarioClass, adminClass
from vista import menus

diccionarioUsuarios = usuarios.usuarios
asistente = asistenteClass.asistente
restaurant.iniciarRestaurantes()
def InicioDeSesion ():
    usuario = input("ingrese su usuario: ")
    if usuario in diccionarioUsuarios:
        contrasena = input("ingrese su contraseña: ")
        User = diccionarioUsuarios.get(usuario)
        if User[2] == contrasena:
            print("ingreso existoso")
            logeado = usuarioClass.userLogin(User[0], User[1], User[2], User[3])
            if User[3] == "usuario":
                menus.menuUsuario(logeado)
            elif User[3] == "administrador":
                logeado2 = adminClass.userAdmin(User[0], User[1], User[2], User[3])
                menus.menuAdministrador(logeado2)
            else:
                restTmp = restaurant.objectRestaurantDic.get(User[0])
                asistente = asistenteClass.asistente(logeado, restTmp)
                menus.menuAdministradorRestaurante(asistente)
            return False
        else:
            print("Contraseña Erronea")
            return True

    else:
        print("Usuario no valido")

def cerrarSesion ():
    InicioDeSesion()


