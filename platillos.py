import funcionesDeLectura
platillos = dict()
platillos = {}
key = []
funcionesDeLectura.leerArchivo("platillos.txt",platillos,key)

def obtenerID(nombre):
    for j,k in platillos.items():
        if k[1] == nombre:
            return j