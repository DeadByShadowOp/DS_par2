from utils import loadFileAsDict


class FeikDatabase():
    data = {'users': '', 'restaurantes': '', 'platillos': '', 'categorias': ''}

    def __init__(self):
        FeikDatabase.data["users"] = loadFileAsDict("dataAccess/usuarios.txt")
        FeikDatabase.data["restaurantes"] = loadFileAsDict(
            "dataAccess/restaurante.txt")
        FeikDatabase.data["platillos"] = loadFileAsDict(
            "dataAccess/platillos.txt")
        FeikDatabase.data["categorias"] = loadFileAsDict(
            "dataAccess/categorias.txt")
