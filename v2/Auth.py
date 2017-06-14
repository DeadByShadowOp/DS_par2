from utils import loadFileAsDict, choiceInput
from models import Usuario


def getCurrentUser():
    user = loadFileAsDict("activeuser")
    if name in user:
        return user
    else:
        return None


def isAuthenticated():
    return getCurrentUser() is not None


# Decorador de vista que requiere autenticacion
def require_login(view):
    def wrapper():
        if not isAuthenticated():
            print("Debes iniciar sesion primero")
            if choiceInput("Deseas iniciar sesión? Y/n", ['y', 'Y', 'n', 'N']):
                return 6
        else:
            view()


def authenticate(user, psw):
    return Usuario(0, user, psw)
