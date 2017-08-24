class Usuario:
    def __init__(self, identificador, nombre, password):
        self.identificador = identificador
        self.nombre = nombre
        self.password = password


class Categoria:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Restaurante:
    def __init__(self, asistente, nombre, direccion, telefono, duenio, platillos):
        self.asistente = asistente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.duenio = duenio
        self.platillos = platillos
    def __str__(self):
        return self.nombre

class Asistente(Usuario):
    def __init__(self, identificador, nombre, password, restaurante):
        Usuario.__init__(self, identificador, nombre, password)
        self.restaurante = restaurante


class Platillo:
    def __init__(self, numeroPlatillo, nombre, servido, tipo, restaurant, categoria, ingredientes, imagenes, descripcion):
        self.numeroplatillo = numeroPlatillo
        self.nombre = nombre
        self.tipo = tipo
        self.restaurant = restaurant
        self.categoria = categoria
        self.ingredientes = ingredientes
        self.imagenes = imagenes
        self.descripcion = descripcion

    def __str__(self):
        return "Nombre: " + self.nombre + "\nDescripción: " + self.descripcion + "\nCategoria: " + self.categoria + "\nTipo: " + self.tipo
