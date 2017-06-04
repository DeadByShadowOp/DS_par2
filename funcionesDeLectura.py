def leerArchivo(ruta,diccionario,key):
    archivoUsuarios = open(ruta, "r")
    usuarios = diccionario
    linea2 = []
    linea3 = []
    key1 = key
    linea = archivoUsuarios.readline()
    while linea != "":
        # creacion de una lista con valores de la linea
        claves = linea.split(",")
        # creacion de lista con los valores de CI o Id para usar como key
        key1.append(claves[0])
        # asignacion de valores en una lista de lista
        for i in range(len(claves)):
            if (claves[i] != "\n") and (claves[i] != ""):
                linea2.append(claves[i])
        linea3.append(linea2)
        linea2 = []
        linea = archivoUsuarios.readline()
    # asignacion de valores al diccionario
    for i in range(len(linea3)):
        usuarios.setdefault(key1[i], linea3[i])
    return usuarios,key1