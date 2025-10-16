materias = {
    1: "Programación 1",
    2: "Programación 2",
    3: "Inglés",
    4: "Matemática",
    5: "Base de Datos",
    6: "Arquitectura en Sistemas Operativos",
    7: "Organización Empresarial",
    8: "Análisis y Probabilidad",
    9: "Inglés 2",
    10: "Base de Datos 2"
}

trampas = {3, 5, 7, 9, 10}

def mostrar_tablero(jugadores):
    print("\n📚 Plan de estudios (de abajo hacia arriba):")
    contenido_inicio = "Inicio (Casilla 0): ["
    for jugador in jugadores:
        if jugador.posicion == 0:
            contenido_inicio += f"{jugador.emoji} "
    contenido_inicio += "]"
    print(contenido_inicio)

    for i in range(1, 11):
        contenido = ""
        if i in trampas:
            contenido += "📉 "
        for jugador in jugadores:
            if jugador.posicion == i:
                contenido += f"{jugador.emoji} "
        print(f"{materias[i]} (Casilla {i}): [{contenido.strip()}]")
    print("-" * 40)