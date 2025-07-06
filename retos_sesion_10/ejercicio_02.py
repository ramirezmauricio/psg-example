'''
El dueño de una tienda de ropa deportiva ha comprado ropa formal y quiere abrir una nueva tienda que combine ambos estilos. 
Crea un conjunto con las prendas de ambos tipos con las listas de prendas
'''

prendas_1 = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
prendas_2 = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

#Convertir a cojuntos

prendas_1 = set(prendas_1)
prendas_2 = set(prendas_2)

#Combinación de estilos de prendas

prendas_combinadas = prendas_1.union(prendas_2)

print(prendas_combinadas)