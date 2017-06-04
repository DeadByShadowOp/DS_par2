import usuarios
import menus
#from contracts import contract
import usuarioClass
import  restauranteClass
import asistenteClass
import restaurant
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
            logeado = usuarioClass.userLogin(User[0],User[1],User[2],User[3])
            if User[3] == "usuario":
                menus.menuUsuario(logeado)
            elif User[3] == "administrador,":
                menus.menuAdministrador()
            else:
                restTmp = restaurant.objectRestaurantDic.get(User[0])
                asistente = asistenteClass.asistente(logeado,restTmp)
                menus.menuAdministradorRestaurante(asistente)
            return False
        else:
            print("Contraseña Erronea")
            return True

    else:
        print("Usuario no valido")

def cerrarSesion ():
    InicioDeSesion()


