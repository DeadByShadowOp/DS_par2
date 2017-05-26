import usuarios
import menus
from contracts import contract
diccionarioUsuarios = dict()
User = []
diccionarioUsuarios = usuarios.usuarios
def InicioDeSesion ():
    usuario = input("ingrese su usuario: ")
    if usuario in diccionarioUsuarios:
        contrasena = input("ingrese su contraseña: ")
        User = diccionarioUsuarios.get(usuario)
        if User[2] == contrasena:
            print("ingreso existoso")
            if User[3] == "usuario":
                menus.menuUsuario()
            elif User[3] == "administrador,":
                menus.menuAdministrador()
            else:
                menus.menuAdministradorRestaurante()
            return False
        else:
            print("Contraseña Erronea")
            return True

    else:
        print("Usuario no valido")

def cerrarSesion ():
    InicioDeSesion()


