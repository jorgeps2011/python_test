import re

MORADO = '\033[95m'
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
RESET = '\033[0m'
NEGRITA = '\033[1m'
SUBRAYADO = '\033[4m'


def rojo(texto):
    return ROJO + texto + RESET
def azul(texto):
    return AZUL + texto + RESET
def verde(texto):
    return VERDE + texto + RESET
def amarillo(texto):
    return AMARILLO + texto + RESET
def morado(texto):
    return MORADO + texto + RESET
def negrita(texto):
    return NEGRITA+ texto + RESET
def subrayado(texto):
    return SUBRAYADO+ texto + RESET


DEFAULT_TITLE = "Menu Principal"
OPCION_0_DEFECTO="Salir"

def crearMenu(  items,
                funciones,
                titulo=DEFAULT_TITLE,
                texto_opcion_0=OPCION_0_DEFECTO,
                en_bucle=True):
    while True:
        for cuenta in range(0,100):
            print("")
        print(negrita(titulo))
        print("")
        opcion = 0
        for item in items:
            opcion += 1
            print(" " + str(opcion) + ". " + item)

        print("")
        print(morado(" 0. "+texto_opcion_0))
        print("")
        opcionElegida = superInput("Elija su opción",
                                              mensaje_error_fatal="Opción inválida. Pulse ENTER para continuar...",
                                              maximo_intentos=1 ,
                                              patron="^[0-" + str(opcion) + "]$",
                                              simbolo_fin_pregunta=":")
        if(opcionElegida is None):
            input()
            if (not en_bucle):
                return
            continue
        if(opcionElegida=="0"):
            return
        funciones[int(opcionElegida)-1]()
        if(not en_bucle):
            return
MENSAJE_ERROR_ESTANDAR = "El valor introducido no es válido"
MENSAJE_ERROR_FATAL = "Demasiados intentos"
PATRON_NOMBRE_COMPLETO="^[A-Z][a-z]{2,}(\s[A-Z][a-z]+)+$"
PATRON_ENTERO_POSITIVO="^[0-9]+$"
PATRON_ENTERO_POSITIVO_SIN_CERO="^[1-9][0-9]+$"
PATRON_ENTERO="^\-?[0-9]+$"
PATRON_FECHA_NACIMIENTO="^((0[1-9])|([12][0-9])|(3[01]))/((0[1-9])|(1[0-2]))/((19)|(20))[0-9]{2}$"

def superInput(pregunta,
               defecto="",
               listaPermitidos=(),
               patron=".*",
               mensaje_error=MENSAJE_ERROR_ESTANDAR,
               mensaje_error_fatal=MENSAJE_ERROR_FATAL,
               maximo_intentos=3,
               simbolo_fin_pregunta="?",
               mostrar_valores_permitidos=False):
    prompt=pregunta
    if(mostrar_valores_permitidos and len(listaPermitidos)!=0):
        prompt += " ("
        for valor in listaPermitidos:
            prompt += valor+"/"
        prompt = prompt[:-1]+")"
    prompt+=simbolo_fin_pregunta
    prompt=verde(prompt)
    if(len(defecto)!=0):
        prompt+=azul("["+defecto+"]")
    prompt+=" "
    while True:
        respuesta=input(prompt)
        if(len(respuesta)==0):
            respuesta=defecto
        if(
            (len(listaPermitidos)==0 or respuesta in listaPermitidos)
            and re.match(patron,respuesta)):
            return respuesta
        else:
            maximo_intentos-=1
            if(maximo_intentos!=0):
                print(rojo(mensaje_error))
            else:
                print(negrita(rojo(mensaje_error_fatal)))
                return

