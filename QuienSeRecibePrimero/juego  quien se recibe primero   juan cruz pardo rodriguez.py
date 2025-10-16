import random
import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tirar_moneda():
    return random.choice(['cara', 'cruz'])

def mostrar_tablero(pos1, pos2, trampas, materias, emoji1, emoji2):
    print("\n📚 Plan de estudios (de abajo hacia arriba):")
    contenido_inicio = ""
    if pos1 == 0:
        contenido_inicio += emoji1 + " "
    if pos2 == 0:
        contenido_inicio += emoji2 + " "
    print(f"Inicio (Casilla 0): [{contenido_inicio.strip()}]")

    for i in range(1, 11):
        nombre = materias.get(i, f"Materia {i}")
        contenido = ""
        if i in trampas:
            contenido += "📉 "
        if i == pos1:
            contenido += emoji1 + " "
        if i == pos2:
            contenido += emoji2 + " "
        print(f"{nombre} (Casilla {i}): [{contenido.strip()}]")
    print("-" * 40)

def turno_jugador(nombre, emoji, pos, pierde_turno):
    if pierde_turno:
        print(f"\n⛔ {nombre} pierde este turno por una materia complicada.")
        return pos, False
    input(f"\nTurno de {nombre} (ENTER para lanzar la moneda)...")
    limpiar()
    print("➡️ Lado Cara avanza 2 casillas, Lado Cruz avanza 1 casilla")
    resultado = tirar_moneda()
    avance = 2 if resultado == 'cara' else 1
    print(f"{nombre} {emoji} sacó {resultado} y avanza {avance} casilla(s).")
    pos += avance
    if pos > 10:
        pos = 10
    pierde_turno = pos in trampas
    if pierde_turno:
        print("¡Materia complicada! Pierdes el próximo turno ⛔")
    return pos, pierde_turno

def decidir_inicio(jug1, jug2, emoji1, emoji2):
    print("\n🎲 Lanzando monedas para ver quién empieza...")
    while True:
        d1 = tirar_moneda()
        d2 = tirar_moneda()
        print(f"{jug1} {emoji1} sacó {d1}")
        print(f"{jug2} {emoji2} sacó {d2}")
        if d1 != d2:
            if d1 == 'cara':
                turno = 1
                print(f"Empieza {jug1} {emoji1}")
            else:
                turno = 2
                print(f"Empieza {jug2} {emoji2}")
            return turno
        print("Los dos sacaron el mismo lado de la moneda, se vuelve a lanzar...\n")

# Datos iniciales
trampas = [3, 5, 7, 9, 10]
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

print("🎓 Bienvenido a '¿Quién se recibe primero?'")
print("¡Compite por ver quién cursa todas las materias y se recibe primero!\n")

jug1 = input("Nombre del estudiante 1: ")
jug2 = input("Nombre del estudiante 2: ")

emoji1 = "🧑‍🎓"
emoji2 = "👩‍🎓"

pos1 = 0
pos2 = 0
pierde_turno_1 = False
pierde_turno_2 = False

turno = decidir_inicio(jug1, jug2, emoji1, emoji2)

while True:
    if turno == 1:
        if pierde_turno_1:
            print(f"\n⛔ {jug1} pierde este turno por una materia complicada.")
            pierde_turno_1 = False
            turno = 2
            continue
        pos1, pierde_turno_1 = turno_jugador(jug1, emoji1, pos1, pierde_turno_1)
        mostrar_tablero(pos1, pos2, trampas, materias, emoji1, emoji2)
        if pos1 >= 10:
            print(f"\n🎉 ¡{jug1} {emoji1} se recibió y obtuvo el título universitario! 🏆🎓")
            break
        turno = 2
    else:
        if pierde_turno_2:
            print(f"\n⛔ {jug2} pierde este turno por una materia complicada.")
            pierde_turno_2 = False
            turno = 1
            continue
        pos2, pierde_turno_2 = turno_jugador(jug2, emoji2, pos2, pierde_turno_2)
        mostrar_tablero(pos1, pos2, trampas, materias, emoji1, emoji2)
        if pos2 >= 10:
            print(f"\n🎉 ¡{jug2} {emoji2} se recibió y obtuvo el título universitario! 🏆🎓")
            break
        turno = 1