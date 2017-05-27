import usuarios
import menus
from contracts import contract
import usuarioLogeado
diccionarioUsuarios = dict()
User = []
diccionarioUsuarios = usuarios.usuarios
logeado = usuarioLogeado.userLogin()


def InicioDeSesion ():
    usuario = input("ingrese su usuario: ")
    if usuario in diccionarioUsuarios:
        contrasena = input("ingrese su contraseña: ")
        User = diccionarioUsuarios.get(usuario)
        if User[2] == contrasena:
            print("ingreso existoso")
            logeado.id = User[0]
            logeado.nombre = User[1]
            logeado.password = User[2]
            logeado.rol = User[3]
            logeado.restaurante = User[4]
            if User[3] == "usuario":
                menus.menuUsuario(logeado)
            elif User[3] == "administrador,":
                menus.menuAdministrador()
            else:
                menus.menuAdministradorRestaurante(logeado)
            return False
        else:
            print("Contraseña Erronea")
            return True

    else:
        print("Usuario no valido")

def cerrarSesion ():
    InicioDeSesion()


