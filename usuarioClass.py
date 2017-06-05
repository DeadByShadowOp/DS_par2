class userLogin:
    id = ""
    nombre = ""
    password = ""
    rol = ""
#    restaurante = ""

    def __init__(self,id,nombre,password,rol):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.rol = rol