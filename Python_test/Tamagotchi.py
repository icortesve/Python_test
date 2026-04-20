class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        print(f"{self.nombre} está jugando con {self.tamagotchi.nombre}")
        self.tamagotchi.jugar()

    def darle_comida(self):
        print(f"{self.nombre} le da de comer a {self.tamagotchi.nombre}")
        self.tamagotchi.comer()

    def curarlo(self):
        print(f"{self.nombre} está curando a {self.tamagotchi.nombre}")
        self.tamagotchi.curar()

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

# Crear Instancias
mascota = Tamagotchi("Pixel", "Verde")
dueno = Persona("Juan", "Perez", mascota)

dueno.darle_comida()
dueno.curarlo()
dueno.jugar_con_tamagotchi()