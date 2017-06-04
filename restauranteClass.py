class restaurante():
    asistente = ""
    nombre = ""
    direccion = ""
    telefono = ""
    dueño = ""
    platillos = []

    def __init__(self,asistente,nombre,direccion,telefono,dueño,platillos):
        self.asistente = asistente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.dueño = dueño
        self.platillos = platillos
