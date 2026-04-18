# 1. Multiplica por 2
def multiplica_por_dos(num):
    resultado = []
    for i in range(num + 1):
        resultado.append(i * 2)
    return resultado
##print(multiplica_por_dos(20))

# 2. Suma y resta
def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    resta = lista[0] - lista[1]
    print(suma)
    return resta
##print(suma_y_resta([5,4]))
##print(suma_y_resta([4,5]))

# 3. Sumatoria menos longitud
def sumatoria_menos_longitud(lista):
    suma = sum(lista)
    longitud = len(lista)
    return suma - longitud
##print(sumatoria_menos_longitud([1,2,3,4]))
##print(sumatoria_menos_longitud([1,2,3,4,5]))

# 4. Valores multiplicados por el segundo
def valores_multiplicados_segundo(lista):
    print(len(lista))
    
    if len(lista) < 2:
        return []
    
    segundo = lista[1]
    nueva_lista = []
    
    for valor in lista:
        nueva_lista.append(valor * segundo)
    
    return nueva_lista
##print(valores_multiplicados_segundo([1,3,5,7]))
##print(valores_multiplicados_segundo([1,2]))

# 5. Valor multiplicado y longitud
def valor_multiplicado_longitud(valor, longitud):
    resultado = []
    
    for i in range(longitud):
        resultado.append(valor * longitud)
    
    return resultado
#print(valor_multiplicado_longitud(5,2))
#print(valor_multiplicado_longitud(7,5))
#print(valor_multiplicado_longitud(6,6))

# 🔍 Pruebas (importante para demostrar que funciona)

print("1:", multiplica_por_dos(5))
print("2:", suma_y_resta([5, 4]))
print("3:", sumatoria_menos_longitud([1, 2, 3, 4]))
print("4:", valores_multiplicados_segundo([1, 3, 5, 7]))
print("5:", valores_multiplicados_segundo([1]))
print("6:", valor_multiplicado_longitud(5, 2))
print("7:", valor_multiplicado_longitud(7, 5))