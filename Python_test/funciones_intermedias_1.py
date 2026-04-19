
##1. Actualizar valores en diccionarios y listas

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

# 1. Reemplazar 3 por 6 en matriz (búsqueda)
for fila in matriz:
    for i in range(len(fila)):
        if fila[i] == 3:
            fila[i] = 6
#print(matriz)

# 2. Cambiar nombre buscando valor
for cantante in cantantes:
    if cantante["nombre"] == "Ricky Martin":
        cantante["nombre"] = "Enrique Martin Morales"
#print(cantantes)

# 3. Cambiar "Cancún" por "Monterrey"
for pais, lista_ciudades in ciudades.items():
    for i in range(len(lista_ciudades)):
        if lista_ciudades[i] == "Cancún":
            lista_ciudades[i] = "Monterrey"
#print(ciudades)

# 4. Cambiar latitud (sin asumir posición)
for coord in coordenadas:
    if "latitud" in coord:
        coord["latitud"] = 9.9355431
#print(coordenadas)

print("Matriz:", matriz)
print("Cantantes:", cantantes)
print("Ciudades:", ciudades)
print("Coordenadas:", coordenadas)

##2. Iterar a través de una lista de diccionarios

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for diccionario in lista:
        line = ""
        for clave, valor in diccionario.items():
            line += f"{clave}: {valor}, "
        print(line.strip(", "))

iterarDiccionario(cantantes)

##3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
   for diccionario in lista:
        print(diccionario[llave])
        
iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)

##4. Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        
        for elemento in lista:
            print(elemento)
        
        print()  # línea en blanco para separar

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)