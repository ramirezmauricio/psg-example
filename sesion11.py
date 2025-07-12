#Diccionario de clave entera y valor entero

print ("Diccionario de clave entera y valor entero")
diccionario = {1: 10, 2: 20, 3: 30}
print(diccionario)
print(type(diccionario))

#Diccionario de clave entero y valor cadena

print ("Diccionario de clave entero y valor cadena")
diccionario = {1: 'uno', 2: 'dos', 3: 'tres'}
print(diccionario)
print(type(diccionario))

#Diccionario de clave cadena y valor entero

print ("Diccionario de clave cadena y valor entero")
diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
print(diccionario)
print(type(diccionario))

#Diccionario de clave cadena y valor cadena

print ("Diccionario de clave cadena y valor cadena")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
print(type(diccionario))

#Diccionario mixto

print ("Diccionario mixto")
diccionario = {1:"ID-XXXXX", "edad": 3, 'animal': '🐶' , ("John","Doe"): 6917222722, "salvaje": False}
print(diccionario)
print(type(diccionario))

'''
Se utiliza la función dict() para crear diccionarios vacíos o a partir de secuencias

Permite convertir secuencias como listas, tuplas, conjuntos en diccionarios las secuencias deben tener pares clave-valor
'''

'''
Diccionario vacío, se declara con llaves {} o con la función dict()

Es la razón por la que no se usa {} para crear un conjunto vacío

Los diccionarios nacieron antes que los conjuntos
'''

'''
Para mantener la consistencia y claridad y coherencia

Se mantuvo la sintaxis de los diccionarios vacíos con {}
'''

print ("Diccionario vacío")
diccionario = {}
print(diccionario)
print(type(diccionario))
diccionario = dict()
print(diccionario)
print(type(diccionario))

'''
Diccionario a partir de una lista anidada

Necesita que la lista tenga elementos pares
'''

print ("Diccionario a partir de una lista")
lista = [['perro', '🐶'] , ['gato','🐱'] , ['ave','🐦']]
print(lista)
diccionario = dict(lista)
print(diccionario)
print(type(diccionario))

'''
Diccionario a partir de una tupla

Necesita que la tupla tenga elementos pares
'''

print ("Diccionario a partir de una tupla de tuplas")
tupla = (('perro', '🐶') , ('gatos','🐱') , ('ave',['🐦','🦅']))
print(tupla)
diccionario = dict(tupla)
print(diccionario)
print(type(diccionario))

#Diccionario mediante comprensión

print ("Diccionario mediante comprensión")
diccionario = {animal:animal*3 for animal in '🐶🐱🐹🐰'}
print(diccionario)
print(type(diccionario))

'''
Indexación y Slicing
Los diccionarios poseen indexación por clave

No se puede acceder a los elementos de un diccionario por posición

Si se puede acceder a los elementos de un diccionario por clave

No se puede realizar slicing en un diccionario
'''

#Un diccionario es una colección de pares clave-valor

#Accedemos a los elementos de un diccionario por clave

print ("Acceder mediante clave")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
print(diccionario['perro'],type(diccionario['perro']))
print(diccionario['gato'],type(diccionario['gato']))
print(diccionario['ave'],type(diccionario['ave']))

'''
El acceso no solo nos permite obtener el valor de la clave

Sino que también nos permite modificar el valor de la clave
'''

#Cambiar el valor de un clave

print ("Cambiar el valor de una clave")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario['perro'] = '🐩'
print(diccionario)

#Si la clave no existe, se crea un nuevo par clave-valor

print ("Crear un nuevo par clave-valor")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario['pez'] = '🐠'
print(diccionario)

#Para eliminar un par clave-valor se utiliza la palabra reservada "del"

print ("Eliminar un par clave-valor")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
del diccionario['ave']
print(diccionario)

'''
No se puede modificar la clave son inmutables y únicas

Se puede reasignar la clave creando un nuevo par clave-valor y eliminando el anterior
'''

print ("Modificar la clave")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario['perrito'] = diccionario['perro']
del diccionario['perro']
print(diccionario)

'''
Concatenación de diccionarios
No se puede concatenar diccionarios con el operador +
'''

'''
print ("Concatenar diccionarios")
diccionario1 = {'perro': '🐶', 'gato': '🐱'}
diccionario2 = {'ave': '🐦', 'pez': '🐠'}
concatenado = diccionario1 + diccionario2 # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

'''

'''
Repetición de diccionarios
No se puede repetir diccionarios con el operador *+*
'''

'''
print ("Repetir diccionarios")
diccionario = {'perro': '🐶', 'gato': '🐱'}
repetido = diccionario * 3 # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
'''
'''
Métodos de los diccionarios
Los diccionarios poseen los siguientes métodos:

Métodos de acceso
Métodos de adición
Métodos de eliminación
Métodos de copia
'''

'''
Se utiliza la notación de punto .

diccionario.metodo()

diccionario.metodo(valor)
'''

'''
Métodos de acceso
Nos permiten obtener información del diccionario

get()
items()
keys()
values()
'''

'''
get(clave): Recibe una clave y retorna el valor del 
par clave-valor, si la clave no existe retorna None
'''

print ("Método get(clave)")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print (diccionario)
perro = diccionario.get('perro')
print(perro, type(perro))
pez = diccionario.get('pez')
print(pez, type(pez))

'''
items(): Retorna una lista de tuplas con los 
pares clave-valor, se puede iterar para obtener los pares clave-valor
'''

print ("Método items()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
items = diccionario.items()
print(items, type(items))
items = list(items) # Convertir a lista
print(items, type(items))
print(items[0], type(items[0]))

'''
keys(): Retorna una lista con las claves 
del diccionario, se puede iterar para obtener las claves
'''

print ("Método keys()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
keys = diccionario.keys()
print(keys, type(keys))
keys = list(keys) # Convertir a lista
print(keys, type(keys))
print(keys[0], type(keys[0]))

'''
values(): Retorna una lista con los valores 
del diccionario, se puede iterar para obtener los valores
'''

print ("Método values()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
values = diccionario.values()
print(values, type(values))
values = list(values) # Convertir a lista
print(values, type(values))
print(values[0], type(values[0]))

'''
Métodos de adición
Nos permiten agregar elementos al diccionario

update()
'''

'''
update(diccionario): Recibe un diccionario y agrega los pares clave-valor
al diccionario, si la clave ya existe reescribe el valor
'''

print ("Método update(diccionario)")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario.update({'pez': '🐠', 'perro': '🐩'})
print(diccionario)

'''
update(clave=valor): Recibe claves y valores, agrega el par clave-valor 
al diccionario, si la clave ya existe reescribe el valor
'''

print ("Método update(clave=valor)")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario.update(pez='🐠', perro='🐩')
print(diccionario)

'''
Métodos de eliminación
Permiten eliminar elementos del diccionario

clear()
pop()
popitem()
'''

#clear(): Elimina todos los elementos del diccionario

print ("Método clear()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
diccionario.clear()
print(diccionario)

'''
pop(clave): Recibe una clave y elimina el par clave-valor 
del diccionario, retorna el valor de la clave
'''

print ("Método pop(clave)")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
gato = diccionario.pop('gato')
print(gato, type(gato))
print(diccionario)

'''
popitem(): Elimina el último par clave-valor del diccionario, 
retorna el par clave-valor, si el diccionario está vacío retorna un error
'''

print ("Método popitem()")
diccionario = {'perro': '🐶', 'gato': '🐱'}
print(diccionario)
par = diccionario.popitem()
print(par, type(par))
print(diccionario)
# par = diccionario.popitem()
# print(par, type(par)) # KeyError: 'popitem(): dictionary is empty'

'''
Métodos de copia
Permiten copiar el diccionario con una nueva referencia de memoria

copy()
'''

'''
Cuando se asigna un diccionario a una nueva variable se asigna por referencia

NO se crea un dict nuevo sino una referencia al original
'''

print ("Asignación por referencia")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
copia = diccionario
print(copia)
copia['ave'] = '🦅'
print(diccionario)
print(copia)

#Para crear una copia del diccionario se utiliza el método copy()

print ("Método copy()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
copia = diccionario.copy()
print(copia)
copia['ave'] = '🦅'
print(diccionario)
print(copia)

'''
Funciones con diccionarios
Los diccionarios interactúan con funciones propias de python

len()
in / not in
iter()
Existen otras funciones pueden encontrarse en la documentación
https://docs.python.org/3/library/stdtypes.html#typesmapping
'''

#len(diccionario): Retorna la cantidad de pares clave-valor del diccionario

print ("Función len()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
longitud = len(diccionario)
print(longitud)

#in / not in: Verifica si una clave existe en el diccionario

print ("Función in  / not in")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
existe = 'perro' in diccionario
print(existe, type(existe))
no_existe = 'pez' not in diccionario
print(no_existe, type(no_existe))

#iter(diccionario.items): Recibe items del diccionario y retorna un iterador

print ("Función iter()")
diccionario = {'perro': '🐶', 'gato': '🐱', 'ave': '🐦'}
print(diccionario)
iterador = iter(diccionario.items())
print(type(iterador))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))
siguiente = next(iterador)
print(siguiente, type(siguiente))

'''
Diccionarios anidados
Los diccionarios pueden contener otros diccionarios
'''

print ("Diccionarios anidados")
diccionario = {'perro': '🐶', 'gato': '🐱',  'ave': {'pajaro': '🐦', 'aguila': '🦅'}}
print(diccionario)
aves = diccionario['ave']
print(aves)
ave = aves['pajaro']
print(ave)
ave = aves['aguila']
print(ave)