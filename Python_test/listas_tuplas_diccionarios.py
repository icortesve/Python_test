
#Crear lista de diccionarios
ventas = [
    {"fecha": "2021-01-01", "producto": "Agar", "cantidad": 2, "precio": 100000},
    {"fecha": "2022-02-01", "producto": "Extracto de Maltosa", "cantidad": 5, "precio": 80000},
    {"fecha": "2023-03-02", "producto": "Nitrato de Sodio", "cantidad": 1, "precio": 50000},
    {"fecha": "2024-04-02", "producto": "Cloruro de Sodio", "cantidad": 3, "precio": 1000},
    {"fecha": "2025-05-03", "producto": "Hidróxido de Potasio", "cantidad": 4, "precio": 10000},
    ]

#Cálculo ingreso total
ingreso_total = 0
for sale in ventas:
  ingreso_total += sale["cantidad"]*sale["precio"]
print("Ingresos totales:", ingreso_total)

#Producto más vendido
ventas_por_producto = {}
for sale in ventas:
    producto = sale["producto"]
    cantidad = sale["cantidad"]
    
    if producto in ventas_por_producto:
       ventas_por_producto[producto] += cantidad
    else:
       ventas_por_producto[producto] = cantidad

mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print("El producto más vendido:", mas_vendido)
print("Cantidad vendida", ventas_por_producto[mas_vendido])

