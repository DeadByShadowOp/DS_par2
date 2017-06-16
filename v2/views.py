from v2.utils import showPrettyTitle, add_file, freeTextInput, choiceInput, mostrar_imagen
import v2.Auth
import v2.FeikDatabase
import image
#from controllers import buscarPlatilloPorNombre, buscarPlatilloPorDescripcion


def login_view():
    showPrettyTitle("INICIAR SESION")
    user = ""
    while True:
        usuario = freeTextInput("Ingrese su usuario:")
        psw = freeTextInput("Ingrese su clave")
        user = Auth.authenticate(usuario, psw)
        if user:
            print("Bienvenido " + user.nombre)
            break
        print("Datos ingresados erroneos")
    return user


@v2.Auth.require_login
def admin_view():
    print("hola")


def categorias_view():
    showPrettyTitle("Categorías de platillos")
    for categorias in FeikDatabase.FeikDatabase.data["categorias"]:
        print(categorias)
    input("asd")


def ingresarimagen_view(nombre):
    ruta = freeTextInput("Ingrese la ruta de la imagen")
    add_file(ruta, "platillos", nombre)


def mostrarimagen_view(imagenes):
    mostrar_imagen(imagenes)


def buscarPorNombre_view():
    nombre = freeTextInput("Ingrese el nombre")
    print(buscarPlatilloPorNombre(nombre))


def buscarPorDescripcion_view():
    descripcion = freeTextInput("Ingrese la descripcion")
    print(buscarPlatilloPorDescripcion(descripcion))


def buscar_view():
    showPrettyTitle("Buscar Platillo")
    menu = "01.- Por nombre\n02.- Por descripción\n03.- Volver"


def main_view():
    showPrettyTitle("Restaurantes ESPOL")
    menu = "01.- Listar Categorías De Platos\n02.- Buscar Plato\n03.- Administracion"
    acciones = {
        0: categorias_view,
        1: buscar_view,
        3: admin_view
    }
    opt = choiceInput(menu, 1)
    if opt:
        acciones[int(opt) - 1]()
    else:
        return False
    return True
