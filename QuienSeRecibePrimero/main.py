from juego import jugar, decidir_inicio, tirar_moneda
from jugador import Jugador
from tablero import mostrar_tablero, materias, trampas


def main():
    # Punto de inicio del programa
    print("🎓 Bienvenido a '¿Quién se recibe primero?'")

    # Ejecutar el juego principal
    jugar()


if __name__ == "__main__":
    main()