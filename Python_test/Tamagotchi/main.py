# Importamos las clases necesarias desde nuestros módulos
from Tamagotchi2 import Tamagotchi
from Persona import Persona

# 1. Creamos la instancia del Tamagotchi
mi_mascota = Tamagotchi("Pixel", "Verde")

# 2. Creamos la instancia de la Persona y le asignamos la mascota
mi_dueno = Persona("Juan", "Perez", mi_mascota)

# 3. Probamos la interacción
mi_dueno.darle_comida()
mi_dueno.curarlo()
mi_dueno.jugar_con_tamagotchi()

#Bonus Sensei
class Dragon(Tamagotchi):
    def lanzar_fuego(self):
        self.energia -= 20
        print(f"{self.nombre} lanzó fuego!")