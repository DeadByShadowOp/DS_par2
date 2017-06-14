def choiceInput(message, choices):
    print(message)
    print("ingresa 'q' para salir")
    choices = ["{:02d}".format(x) for x in range(1, choices + 1)]
    print(choices)
    opt = ""
    while opt not in choices and opt != 'q':
        opt = input(">")
    if opt == 'q':
        return False
    return opt

def freeTextInput(message):
    print(message)
    return input(">")


def loadFileAsDict(ruta):
    archivo = open(ruta, "r")
    usuarios = {}
    linea2 = []
    linea3 = []
    key1 = []
    linea = archivo.readline()
    while linea != "":
        # creacion de una lista con valores de la linea
        claves = linea.split(",")
        # creacion de lista con los valores de CI o Id para usar como key
        key1.append(claves[0])
        # asignacion de valores en una lista de lista
        for i, elem in enumerate(claves):
            if (elem != "\n") and (elem != ""):
                linea2.append(elem)
        linea3.append(linea2)
        linea2 = []
        linea = archivo.readline()
    # asignacion de valores al diccionario
    for i, elem in enumerate(linea3):
        usuarios.setdefault(key1[i], elem)
    return usuarios, key1


def showPrettyTitle(title):
    print("###### " + title + " ######")
