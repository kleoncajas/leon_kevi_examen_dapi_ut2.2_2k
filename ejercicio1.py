def LeerDocument(archivo):
    """Función que recibe un fichero y lee su información para posteriormente guardarla en una variable de tipo lista
Parámetros:
- archivo: variable que contiene la ruta de acceso al fichero a leer
Salida:
Lista con los datos del fichero
"""
    lista = []
    archivo = 'LibroCuentas.txt'
    file = open(archivo, "r")
    lineas = file.readlines()
    for a in lineas:
        x = a.replace("\n", "")
        lista.append(x)
    file.close()
    return lista

def IdentificarPagado(lista):
    """Función que crea un fichero con todas las líneas del documento en las en las que pone PAGADO
Parámetros:
lista: lista de str 
Salida:
No devuelve nada
"""
    archivo_1 = "PAGADO.txt"
    file_1 = open(archivo_1, "w")
    file_1.write(LeerDocument(lista[3]))
    file_1.close()