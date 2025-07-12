'''
Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies
{"🐶" : 2, "🐱" : 2, "🐯" : 2, "🐵" : 2, "🦄" : 0, "🦒" : 1}

Añade al arca 3 especies más usando update()
Toma lista de los animales en el arca iterando el diccionario
Existe en el arca la especie 'dragon' 🐲?
Elimina la especie unicornio del arca
Modifica el valor de la especie jirafa por 2
Vacía el arca después del diluvio
'''

#diccionari de noe

arca = {"🐶" : 2, "🐱" : 2, "🐯" : 2, "🐵" : 2, "🦄" : 0, "🦒" : 1}
print("arca: ")
print(arca)

#añdir 3 especies más usando update()

arca.update({"🐧": 2, "🦘": 2, "🦚": 2})

#tomar lista de los animales
especies = list(arca.keys())
print("especies: ")
print(especies)

#existe dragon?
print("existe 🐲?")
print('🐲' in arca)

#eliminar unicornio
del arca['🦄']

#modificar el valor de la especie jirafa por 2
arca['🦒'] = 2

#Vacía el arca después del diluvio
arca.clear()
print(arca)
