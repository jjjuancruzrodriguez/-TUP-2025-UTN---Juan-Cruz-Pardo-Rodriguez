class Jugador:
    def __init__(self, nombre, emoji):
        self.nombre = nombre
        self.emoji = emoji
        self.posicion = 0
        self.pierde_turno = False

    def avanzar(self, pasos):
        self.posicion += pasos
        if self.posicion > 10:
            self.posicion = 10

    def perder_turno(self):
        self.pierde_turno = True

    def __str__(self):
        return f"{self.emoji} {self.nombre} (Casilla {self.posicion})"