from v2.utils import loadFileAsDict


class FeikDatabase():
    data = {'usuarios': {}, 'restaurantes': {}, 'platillos': {}, 'categorias': {}}

    def __init__(self):
        FeikDatabase.data["usuarios"] = loadFileAsDict("dataAccess/usuarios.csv")
        FeikDatabase.data["restaurantes"] = loadFileAsDict(
            "dataAccess/restaurante.csv")
        FeikDatabase.data["platillos"] = loadFileAsDict(
            "dataAccess/platillos.csv")
        FeikDatabase.data["categorias"] = loadFileAsDict(
            "dataAccess/categorias.csv")
