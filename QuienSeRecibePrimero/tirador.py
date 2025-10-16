class Tirador:
    def __init__(self, nombre, nivel, salud, precision):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.precision = precision

    def atacar(self):
        if self.precision > 50:
            print(self.nombre, "acierta el disparo.")
        else:
            print(self.nombre, "falla el disparo.")


            jugador = Tirador("Tirador1")

            jugador.atacar()