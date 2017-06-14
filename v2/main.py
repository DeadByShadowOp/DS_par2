from views import main_view
from FeikDatabase import FeikDatabase


class Programa:
    bd = ""

    def __init__(self):
        bd = FeikDatabase()

    def empezar(self):
        print("Bienvenidos a restaurantes Espol \n")
        opcion = True
        while opcion:
            opcion = main_view()
        print("Chao!")


p = Programa()
p.empezar()
