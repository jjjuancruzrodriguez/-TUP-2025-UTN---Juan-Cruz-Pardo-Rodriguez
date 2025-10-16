class Tirador:
    def __init__(self, nombre, nivel, agilidad, precision):
        self.nombre = nombre
        self.nivel = nivel
        self.agilidad = agilidad
        self.precision = precision

        
    def atacar(self):
        if self.precision > 50:
            print(self.nombre, "acierta el disparo.")
        else:
            print(self.nombre, "falla el disparo.")


    def defenderse(self):
        if self.agilidad > 50:
            print(self.nombre, "esquiva con exito.")
        else:
            print(self.nombre, "no pudo esquivar, el personaje recibe daño.")