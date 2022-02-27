import Colors
import re
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
    prompt=Colors.verde(prompt)
    if(len(defecto)!=0):
        prompt+=Colors.azul("["+defecto+"]")
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
                print(Colors.rojo(mensaje_error))
            else:
                print(Colors.negrita(Colors.rojo(mensaje_error_fatal)))
                return


#print(superInput("Cual es su nombre",patron="^[A-Z][a-z]{2,}(\s[A-Z][a-z]+)+$",mensaje_error="Debe incluir al menos un apellido."))
#print(superInput("Usa usted base de datos??","s",('s','n')))
#print(superInput(   listaPermitidos=('s','n')),
#                    pregunta="Usa usted base de datos?? ")



