import random
import time
import os

# -------- FUNCIONES DE DADO --------
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

caras_dado = {
    1: ["+-------+",
        "|       |",
        "|   o   |",
        "|       |",
        "+-------+"],
    2: ["+-------+",
        "| o     |",
        "|       |",
        "|     o |",
        "+-------+"],
    3: ["+-------+",
        "| o     |",
        "|   o   |",
        "|     o |",
        "+-------+"],
    4: ["+-------+",
        "| o   o |",
        "|       |",
        "| o   o |",
        "+-------+"],
    5: ["+-------+",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "+-------+"],
    6: ["+-------+",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "+-------+"]
}

def tirar_dado_animado():
    for _ in range(10):
        cara = random.randint(1, 6)
        limpiar_consola()
        print("Rodando el dado...\n")
        for linea in caras_dado[cara]:
            print(linea)
        time.sleep(0.1)
    return cara

# -------- CLASE PERSONAJE --------
class Personaje:
    def __init__(self, nombre, turno):
        self.nombre = nombre
        self.turno = turno
        self.posicion = 0

    def avanzar(self, cantidad):
        self.posicion += cantidad
        if self.posicion > 10:
            self.posicion = 10

    def mostrar_estado(self):
        print(f"{self.nombre} está en la casilla {self.posicion}")

# -------- INICIO DEL JUEGO --------
player1= input("ingrese el nombre del jugador")
player2= input("ingrese el nombre del jugador")

while True:
    print("Se tiran los dados para ver quien arranca!!")
    input(f"Le toca tirar el dado a {player1}, presiona enter para tirar el dado") 
    turno1 = tirar_dado_animado()
    print(f"Sacaste {turno1}")
    input(f"Le toca tirar el dado a {player2}, presiona enter para tirar el dado")
    turno2 = tirar_dado_animado()
    print(f"Sacaste {turno2}")
    if turno1 > turno2:
        print(f"Arranca {player1}")
        break
    elif turno1 < turno2:
        print(f"Arranca {player2}")
        break
    else:
        print("Sacaron lo mismo, se vuelven a tirar los dados")



jugador1 = Personaje(player1, turno=1)
jugador2 = Personaje(player2, turno=2)

print("¡Comienza la carrera hasta la casilla 10!")
time.sleep(1)

juego_terminado = False

while not juego_terminado:
    for jugador in [jugador1, jugador2]:
        input(f"\nTurno de {jugador.nombre}. Presiona ENTER para tirar el dado...")
        resultado = tirar_dado_animado()
        print(f"\n{jugador.nombre} sacó un {resultado} 🎲")
        jugador.avanzar(resultado)
        jugador.mostrar_estado()
        print("-" * 30)
        time.sleep(1.5)

        if jugador.posicion >= 10:
            print(f"\n🎉 ¡{jugador.nombre} ha llegado a la meta y ganó!")
            juego_terminado = True
            break