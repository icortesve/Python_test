#1. Actualizar valores en diccionarios y listas

# Lista dentro de lista
matriz = [ [10, 15, 20], [3, 7, 14] ]
#Lista de diccionarios
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]



# Diccionario con listas
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

#lista con diccionario
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

## Solución con índices fijos (conociendo valores de las listas)

# matriz[1][0] = 6
# print(matriz)

# cantantes[0]["nombre"] = "Enrique Martin Morales"
# print(cantantes)

# ciudades["México"][2] = "Monterrey"
# print(ciudades)

# print(coordenadas)
# coordenadas[0]["latitud"] = 9.9355431
# print(coordenadas)

## Solución dinámica (no conociendo valores de las listas)

print("Matriz:", matriz)
print("Cantantes:", cantantes)
print("Ciudades:", ciudades)
print("Coordenadas:", coordenadas)