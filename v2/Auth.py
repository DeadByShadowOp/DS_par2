from utils import loadFileAsDict, choiceInput, yesNoInput
from models import Usuario
from functools import wraps
import views
from FeikDatabase import FeikDatabase


def getCurrentUser():
    user = loadFileAsDict("activeuser")
    if user and name in user:
        return user
    else:
        return None


def isAuthenticated():
    return getCurrentUser() is not None


# Decorador de vista que requiere autenticacion
def require_login(view):
    @wraps(view)
    def wrapper(*args, **kwds):
        if not isAuthenticated():
            print("Debes iniciar sesion primero")
            if yesNoInput("Deseas iniciar sesión?"):
                views.login_view()
        else:
            view(*args, **kwds)
    return wrapper


def authenticate(user, psw):
    if user in FeikDatabase.data["usuarios"]:
        usuario = Usuario(FeikDatabase.data["usuarios"][user][0],
                          FeikDatabase.data["usuarios"][user][1],
                          FeikDatabase.data["usuarios"][user][2])
        return usuario
    return None
