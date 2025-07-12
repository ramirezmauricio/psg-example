'''
Crea un diccionario de alimentos y que animales domésticos lo consumen, por ejemplo
{"carne" : ["gato", "perro"], "zanahoria" : ["conejo"] }
Añade al diccionario 4 alimentos más, usando update(clave=valor)
Existe en el diccionario de alimentos la comida 'trigo'?
Elimina la comida 'zanahoria' del diccionario de alimentos
'''

#Diccionario de alimentos

alimentos = {"carne": ["gato", "perro"], "zanahoria": ["conejo"]}

#Añadir 4 alimentos más

alimentos.update(pescado=["gato"], croquetas=["perro", "gato"], semillas=["loro", "hamster"], heno=["conejo", "cuy"])

#Existe trigo?
print("existe trigo?")
print("trigo" in alimentos)

#Elimina "zanahoria"
del alimentos["zanahoria"]
print(alimentos)