from modelado import funcionesDeLectura

DicCategoria = {}
key = []
DicObjectCategoria = {}
class categoria():
    id = ""
    nombre = ""

    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre

    def generarHash (self):
        return len(key)

    def cargarCategorias(self):
        funcionesDeLectura.leerArchivo("dataAccess/categorias.txt",DicCategoria,key)
        for i in range(len(key)):
            listTmp = DicCategoria.get(key[i])
            DicObjectCategoria.setdefault(key[i],categoria(listTmp[0],listTmp[1]))

    def getCategoria(self,id):
        return DicObjectCategoria.get(id)

    def addCategoria(self,id,nombre):
        DicObjectCategoria.setdefault(id,categoria(id,nombre))

    def mostrarCategorias(self):
        for i,k in DicObjectCategoria.items():
            print(i+".- "+k.nombre)

    def hashExiste(self,op):
        if (op in key) == True:
            return True
        else: return False
