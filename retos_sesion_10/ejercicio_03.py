'''
Tienes dos listas: clientes que compraron en la tienda física y clientes que compraron online.
tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]
a. Quiénes compraron en ambos canales.
b. Quiénes compraron solo en la tienda física.
c. Quiénes compraron solo online.
'''

#listas tiendas
tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

#Convertir a cojuntos
tienda_fisica = set(tienda_fisica)
tienda_online = set(tienda_online)

#a. Quiénes compraron en ambos canales.
ambos = tienda_fisica.union(tienda_online)
print("¿Quiénes compraron en ambos canales?")
print(ambos)

#b. Quiénes compraron solo en la tienda física.
print("¿Quiénes compraron solo en la tienda física?")
print(tienda_fisica)

#c. Quiénes compraron solo online.
print("¿Quiénes compraron solo online?")
print(tienda_online)