import random
from jugador import Jugador
from tablero import mostrar_tablero, trampas

def limpiar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def tirar_moneda():
    return random.choice(['cara', 'cruz'])

def decidir_inicio(jugador1, jugador2):
    print("\n🎲 Tirando moneda para ver quién empieza...")
    while True:
        d1 = tirar_moneda()
        d2 = tirar_moneda()
        print(f"{jugador1.nombre} {jugador1.emoji} sacó {d1}")
        print(f"{jugador2.nombre} {jugador2.emoji} sacó {d2}")
        if d1 != d2:
            if d1 == 'cara':
                print(f"Empieza {jugador1.nombre} {jugador1.emoji}")
                return 1
            else:
                print(f"Empieza {jugador2.nombre} {jugador2.emoji}")
                return 2
        print("Los dos sacaron el mismo lado de la moneda, se vuelve a tirar...\n")

def jugar():
    limpiar()
    print("🎓 Bienvenido a '¿Quién se recibe primero?'")
    print("¡Compite por ver quién cursa todas las materias y se recibe primero!\n")

    nombre1 = input("Nombre del estudiante 1: ")
    nombre2 = input("Nombre del estudiante 2: ")

    jugador1 = Jugador(nombre1, "🧑‍🎓")
    jugador2 = Jugador(nombre2, "👩‍🎓")

    jugadores = [jugador1, jugador2]

    turno = decidir_inicio(jugador1, jugador2)

    while True:
        jugador_actual = jugadores[turno - 1]

        if jugador_actual.pierde_turno:
            print(f"\n⛔ {jugador_actual.nombre} pierde este turno por una materia complicada.")
            jugador_actual.pierde_turno = False
            turno = 2 if turno == 1 else 1
            continue

        input(f"\nTurno de {jugador_actual.nombre} {jugador_actual.emoji} (ENTER para rendir)...")
        limpiar()

        print("Cara vale 2 casillas, Cruz vale 1 casilla")
        moneda = tirar_moneda()
        pasos = 2 if moneda == 'cara' else 1
        print(f"{jugador_actual.nombre} {jugador_actual.emoji} sacó {moneda} y avanza {pasos} casilla(s)")

        jugador_actual.avanzar(pasos)

        if jugador_actual.posicion in trampas:
            print("¡Materia complicada! Pierdes el próximo turno ⛔")
            jugador_actual.pierde_turno = True

        mostrar_tablero(jugadores)

        if jugador_actual.posicion >= 10:
            print(f"\n🎉 ¡{jugador_actual.nombre} {jugador_actual.emoji} se recibió y obtuvo el título universitario! 🏆🎓")
            break

        turno = 2 if turno == 1 else 1