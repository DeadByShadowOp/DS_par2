from modelado import restauranteClass

from modelado import usuarioClass


class asistente(usuarioClass.userLogin):
    rest = restauranteClass.restaurante
    user = usuarioClass.userLogin
    def __init__(self,logeado,restauranteClass):
        self.user = logeado
        self.rest = restauranteClass
