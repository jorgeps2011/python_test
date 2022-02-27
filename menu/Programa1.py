import commonlib

def funcion1():
    items2 = ("Opcion A", "Opcion B", "Opcion C", "Opcion D")
    funciones2 = (funcion1, funcion2, funcion3, funcion4)
    commonlib.crearMenu(items2, funciones2, "SUBMENU")


def funcion2():
    print("Ha pulsado en 2")
    input("Pulse ENTER para continuar...")

def funcion3():
    print("Ha pulsado en 3")
    input("Pulse ENTER para continuar...")

def funcion4():
    print("Ha pulsado en 4")
    input("Pulse ENTER para continuar...")

items=("Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4")
funciones=(funcion1,funcion2,funcion3,funcion4)
commonlib.crearMenu(items,funciones, "MI TITULO")

