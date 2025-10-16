import random
import time
import os

# ---------- FUNCIONES ----------
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def tirar_dado():
    dado = random.randint(1, 6)
    print(f"🎲 Salió un {dado}")
    return dado

def mostrar_tablero(pos1, pos2, nombre1, nombre2):
    print("\n📍 Estado del tablero:\n")
    for i in range(1, 11):
        casilla = f"Casilla {i}: "

        if i == pos1 and i == pos2:
            casilla += f"{nombre1} y {nombre2}"
        elif i == pos1:
            casilla += f"{nombre1} 👤"
        elif i == pos2:
            casilla += f"{nombre2} 👤"
        elif i in trampas:
            casilla += "¡Trampa! ⚠️"
        else:
            casilla += "Vacía"

        print(casilla)
    print("-" * 40)
# ---------- CONFIGURACIÓN ----------
trampas = {
    4: -2,
    7: -3,
    9: -1
}

print("🎮 Bienvenido al juego de carrera con dados y trampas 🎮\n")
jugador1 = input("Ingresa el nombre del Jugador 1: ")
jugador2 = input("Ingresa el nombre del Jugador 2: ")

pos1 = 0
pos2 = 0

# Tirar dado para decidir quién empieza
while True:
    input(f"\n{jugador1}, tira el dado (Enter)...")
    t1 = tirar_dado()
    input(f"{jugador2}, tira el dado (Enter)...")
    t2 = tirar_dado()

    if t1 > t2:
        turno_actual = 1
        print(f"\n👉 Empieza {jugador1}")
        break
    elif t2 > t1:
        turno_actual = 2
        print(f"\n👉 Empieza {jugador2}")
        break
    else:
        print("Empate. Se repite la tirada.")

# ---------- BUCLE PRINCIPAL ----------
ganador = None

while True:
    if turno_actual == 1:
        input(f"\nTurno de {jugador1} (Enter para tirar)...")
        dado = tirar_dado()
        pos1 += dado
        if pos1 in trampas:
            print("⚠️ ¡Caíste en una trampa!")
            pos1 += trampas[pos1]
            if pos1 < 0:
                pos1 = 0
        print(f"{jugador1} está en la casilla {pos1}")
        mostrar_tablero(pos1, pos2, jugador1, jugador2)
        if pos1 >= 10:
            ganador = jugador1
            break
        turno_actual = 2
    else:
        input(f"\nTurno de {jugador2} (Enter para tirar)...")
        dado = tirar_dado()
        pos2 += dado
        if pos2 in trampas:
            print("⚠️ ¡Caíste en una trampa!")
            pos2 += trampas[pos2]
            if pos2 < 0:
                pos2 = 0
        print(f"{jugador2} está en la casilla {pos2}")
        mostrar_tablero(pos1, pos2, jugador1, jugador2)
        if pos2 >= 10:
            ganador = jugador2
            break
        turno_actual = 1

# ---------- FIN DEL JUEGO ----------
print(f"\n🏁 ¡{ganador} ha ganado la carrera! 🏆\n")