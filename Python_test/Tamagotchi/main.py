# Importamos las clases necesarias desde nuestros módulos
from Python_test.Tamagotchi.Tamagotchi2 import Tamagotchi
from Persona import Persona

# 1. Creamos la instancia del Tamagotchi
mascota = Tamagotchi("Pixel", "Verde")

# 2. Creamos la instancia de la Persona y le asignamos la mascota
dueno = Persona("Juan", "Perez", mascota)

# 3. Probamos la interacción
dueno.darle_comida()
dueno.curarlo()
dueno.jugar_con_tamagotchi()