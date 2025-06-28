'''
Una dulcería tiene 2 listas una con los productos y otra con los precios

Agregar 2 productos nuevos al final de las listas
Eliminar el producto con el nombre "Bon Bon Bum" de las listas
¿Cuánto cuesta el producto "Oreo" y "Chizitos"?
¿Cuál es el producto más caro y el más barato?
¿Cuántos productos tienes en total?
¿Cuanto cuestan todos los productos?
Ordena los productos y precios del más barato al más caro
Eliminar todos los productos de las listas
'''

#listas de productos y precios
productos = ["Bon Bon Bum", "Oreo", "Chizitos"]
precios = [1.00, 5.50, 30.00]

#agregar 2 productos nuevos
productos.append("pan")
precios.append(0.50)

productos.append("huevos")
precios.append(47)

print(productos)
print(precios)

#eliminar el nombre "Bon Bon Bum" de la lista
indice = productos.index("Bon Bon Bum")
productos.pop(indice)
precios.pop(indice)

print(productos)
print(precios)

#cuánto cuesta "Oreo" y "Chizitos"?
indice = productos.index("Oreo")
print(productos[indice], precios[indice])

indice = productos.index("Chizitos")
print(productos[indice], precios[indice])

#cuál es el producto más caro y el más barato?

indice = precios.index(max(precios))
print("mas caro", productos[indice], precios[indice])

indice = precios.index(min(precios))
print("mas barato", productos[indice], precios[indice])

#cuántos productos existen en total?
cantidad = len(productos)

print("productos en total:", cantidad)