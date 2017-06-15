from utils import showPrettyTitle, freeTextInput, choiceInput
import Auth
import FeikDatabase

def login_view():
    showPrettyTitle("INICIAR SESION")
    user = ""
    while True:
        usuario = freeTextInput("Ingrese su usuario:")
        psw = freeTextInput("Ingrese su clave")
        user = Auth.authenticate(usuario, psw)
        if user:
            print("Bienvenido " + user.nombre)
            return True
    return user

@Auth.require_login
def saludar():
    print("hola")


def main_view():
    showPrettyTitle("Restaurantes ESPOL")
    menu = "01. Saludar\n"
    acciones = {
        0: saludar
    }
    opt = choiceInput(menu, 1)
    if opt:
        acciones[int(opt)-1]()
    else:
        return False
    return True