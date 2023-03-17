inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
dinero = 2400

def usuario(name, puntos):
    if puntos == inaceptable:
        nivel = "Inaceptable"
    elif puntos == aceptable:
        nivel = "Aceptable"
    elif puntos >= meritorio:
        nivel = "Meritorio"
    else:
        nivel = ""

    if nivel == "":
        print("Esta puntuación no es válida")
    else:
        print("Tu nivel de rendimiento es %s" % nivel)
        print("Te corresponde cobrar %.2f€" % (puntos * dinero))
        
        
usuario("edward", 0.7)

