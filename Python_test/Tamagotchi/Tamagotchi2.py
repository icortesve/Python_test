class Tamagotchi:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.salud = 100
        self.felicidad = 100
        self.energia = 100

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        print(f"{self.nombre} está jugando. Felicidad: {self.felicidad}, Salud: {self.salud}")

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(f"{self.nombre} está comiendo. Felicidad: {self.felicidad}, Salud: {self.salud}")

    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(f"{self.nombre} se está curando. Salud: {self.salud}, Felicidad: {self.felicidad}")
