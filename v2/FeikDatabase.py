from v2.utils import loadFileAsDict


class FeikDatabase():
    data = {'usuarios': {}, 'restaurantes': {}, 'platillos': {}, 'categorias': {}}

    def __init__(self):
        FeikDatabase.data["usuarios"] = loadFileAsDict("dataAccess/usuarios.txt")
        FeikDatabase.data["restaurantes"] = loadFileAsDict(
            "dataAccess/restaurante.txt")
        FeikDatabase.data["platillos"] = loadFileAsDict(
            "dataAccess/platillos.txt")
        FeikDatabase.data["categorias"] = loadFileAsDict(
            "dataAccess/categorias.txt")
