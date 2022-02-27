import Colors
import SuperInput

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
        print(Colors.negrita(titulo))
        print("")
        opcion = 0
        for item in items:
            opcion += 1
            print(" " + str(opcion) + ". " + item)

        print("")
        print(Colors.morado(" 0. "+texto_opcion_0))
        print("")
        opcionElegida = SuperInput.superInput("Elija su opción",
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
