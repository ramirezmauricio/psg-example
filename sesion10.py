#Conjunto de enteros

print ("Conjunto de enteros")
conjunto = {1, 2, 3, 4, 5}
print(conjunto) 
print(type(conjunto))

#Conjunto de cadenas

print ("Conjunto de cadenas")
conjunto = {'🍕','🍔','🍟','🌭'}
print(conjunto)
print(type(conjunto))

#Conjunto mixto

print ("Conjunto mixto")
conjunto = {1, True, 3.14, '☕'}
print(conjunto)
print(type(conjunto))

'''
Se utiliza la función set() para crear conjuntos vacíos o a partir de una secuencia

Permite convertir secuencias como listas, tuplas, cadenas en conjuntos
'''

#Conjunto vacío

print ("Conjunto vacío")
conjunto = set()
print(conjunto)
print(type(conjunto))

#Conjunto a partir de la cadena

print ("Conjunto a partir de la cadena")
cadena = 'Hola Mundo'
conjunto = set(cadena)
print(conjunto)
print(type(conjunto))

#Conjunto a partir de una tupla

print ("Conjunto a partir de una tupla")
tupla = (1, 2, 3, 4, 5, 5)
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))

#Conjunto a partir de una lista

print ("Conjunto a partir de una lista")
lista = [True, False, 0, 1]
conjunto = set(lista)
print(conjunto)
print(type(conjunto))

#Conjunto por comprensión

print ("Conjunto por comprensión")
conjunto = {x for x in '🍕🍔🍟🍕🍔🍟🍔🍟'}
print(conjunto)
print(type(conjunto))

'''
Indexación y Slicing
Los conjuntos no soportan indexación ni slicing

Porque no son ordenados ni indexados

conjunto = {1, 2, 3, 4, 5}
print(conjunto[0]) # TypeError: 'set' object is not subscriptable

conjunto = {1, 2, 3, 4, 5}
print(conjunto[0:3]) # TypeError: 'set' object is not subscriptable
'''

'''
Concatenación de conjuntos
Los conjuntos no soportan la concatenación con el operador +

conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
print(conjunto1 + conjunto2)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
Repetición con conjuntos
Los conjuntos no soportan la repetición con el operador *

conjunto = {1, 2, 3}
print(conjunto * 3)
# TypeError: unsupported operand type(s) for *: 'set' and 'int'
'''

'''
Métodos de los conjuntos
Los conjuntos soportan métodos como:

Métodos de adición
Métodos de eliminación
Métodos de operaciones con conjuntos
Métodos de asignación con operaciones
Métodos de búsqueda
Métodos de copia
'''

'''
Se utiliza la notación de punto .

conjunto.metodo()

conjunto.metodo(valor)
'''

'''
Métodos de adición
Los métodos de adición permiten agregar elementos a un conjunto

add()
update()
No retorna ningún valor
'''

#add(valor) recibe un valor y lo agrega al conjunto si no existe

print ("Método add()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.add('🥗')
print(conjunto) 

#update(valores) recibe una secuencia de valores y los agrega al conjunto si no existen

print ("Método update()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.update(['🥤','🍦'])
print(conjunto) 
conjunto.update('🍩🍪')
print(conjunto) 
conjunto.update(('🍫','🍬'))
print(conjunto)
conjunto.update({'🍭','🍮'})
print(conjunto)

'''
Métodos de eliminación
Los métodos de eliminación permiten eliminar elementos de un conjunto

remove()
discard()
pop()
clear()
Solo pop() retorna el elemento eliminado
'''

#remove(valor) recibe un valor y lo elimina del conjunto si existe, si no existe lanza un error
print ("Método remove()")
conjunto = {'🍕','🍔','🍟','🌭'} 
print (conjunto)
conjunto.remove('🍔')
print(conjunto)
# conjunto.remove('🍔')
# print(conjunto)
# Key Error: '🍔'

#discard(valor) recibe un valor y lo elimina del conjunto si existe, si no existe no lanza un error
print ("Método discard()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.discard('🍔')
print(conjunto)
conjunto.discard('🍔')
print(conjunto)

#pop() elimina un elemento aleatorio del conjunto y lo retorna
print ("Método pop()")
conjunto = {'🍕','🍔','🍟','🌭', '🥤','🍦'}
print (conjunto)
print(conjunto.pop())
print(conjunto)
print(conjunto.pop())
print(conjunto)

#clear() elimina todos los elementos del conjunto
print ("Método clear()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
conjunto.clear()
print(conjunto)

'''
Métodos de operaciones con conjuntos
union() : Unión de conjuntos
intersection() : Intersección de conjuntos
difference() : Diferencia de conjuntos
symmetric_difference() : Diferencia simétrica de conjuntos
Retornan un nuevo conjunto con el resultado de la operación
'''

'''
union(conjunto) recibe un conjunto y retorna la unión de ambos

Contiene todos los elementos de ambos sin repetir

A∪B={x∣x∈A∨x∈B}}
'''

print ("Método union()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
union = conjunto1.union(conjunto2)
print(union)

'''
intersection(conjunto) recibe un conjunto y retorna la intersección de ambos

Contiene los elementos que están en ambos conjuntos

A∩B={x∣x∈A∧x∈B}
'''

print ("Método intersection()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)

'''
difference(conjunto) recibe un conjunto y retorna la diferencia de ambos conjuntos

Los que están en el 1er conjunto pero no en el 2do

A−B={x∣x∈A∧x∈/B}
'''

print ("Método difference()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
diferencia = conjunto1.difference(conjunto2)
print("1 y 2:",diferencia)
diferencia = conjunto2.difference(conjunto1)
print("2 y 1:",diferencia)

'''
symmetric_difference(conjunto) recibe un conjunto y retorna la diferencia simétrica de ambos

Contiene los elementos que están en un conjunto o en el otro pero no en ambos

A△B={x∣x∈A∧x∈/B∨x∈B∧x∈/A}
'''

print ("Método symmetric_difference()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diferencia_simetrica)

'''
Métodos de asignación con operaciones
Permiten realizar operaciones con conjuntos y asignar el resultado al conjunto inicial

intersection_update() : Intersección
difference_update() : Diferencia
symmetric_difference_update() : Diferencia simétrica
'''

'''
intersection_update(conjunto) recibe un conjunto 
y asigna al conjunto inicial la intersección de ambos conjuntos
'''

print ("Método intersection_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1.intersection_update(conjunto2)
print(conjunto1)

'''
difference_update(conjunto) recibe un conjunto 
y asigna al conjunto inicial la diferencia de ambos conjuntos
'''

print ("Método difference_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
conjunto1.difference_update(conjunto2)
print ("1:",conjunto1, "2:",conjunto2)

'''
symmetric_difference_update(conjunto) recibe un conjunto 
y asigna al conjunto inicial la diferencia simétrica de ambos conjuntos
'''

print ("Método symmetric_difference_update()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)

'''
Métodos de búsqueda
Los métodos de búsqueda permiten buscar elementos en un conjunto

issubset() : Subconjunto
issuperset() : Superconjunto
isdisjoint() : Disjunto
Retornan un valor booleano
'''

'''
issubset(conjunto) recibe una secuencia 
y retorna True si el conjunto es subconjunto del conjunto recibido
'''

print ("Método issubset()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 es subconjunto del conjunto2?
print(conjunto1.issubset(conjunto2))
# ¿El conjunto3 es subconjunto del conjunto1?
print(conjunto3.issubset(conjunto1))

'''
issuperset(conjunto) recibe una secuencia 
y retorna True si el conjunto es superconjunto del conjunto recibido
'''

print ("Método issuperset()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 es superconjunto del conjunto2?
print(conjunto1.issuperset(conjunto2)) # C1 contiene a C2?
# ¿El conjunto1 es superconjunto del conjunto2?
print(conjunto1.issuperset(conjunto3)) # C1 contiene a C3?

'''
isdisjoint(conjunto) recibe un secuencia 
y retorna True si el conjunto no tiene elementos en común con el conjunto recibido
'''

print ("Método isdisjoint()")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨'}
conjunto3 = {'🍔','🍟'}
print (conjunto1, conjunto2,conjunto3)
# ¿El conjunto1 no tiene elementos en común con el conjunto2?
print(conjunto1.isdisjoint(conjunto2))
# ¿El conjunto1 no tiene elementos en común con el conjunto3?
print(conjunto1.isdisjoint(conjunto3))

'''
Métodos de copia
Los métodos de copia permiten copiar un conjunto

copy()
Retorna un nuevo conjunto con los mismos elementos
'''

'''
Cuando se asigna un conjunto a una variable se asigna por referencia

NO se crea una copia del conjunto sino una referencia al conjunto original
'''

print ("Asignación por referencia")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
copia = conjunto
copia.add('🥗')
print(conjunto)
print(copia)

#Para crear una copia de un conjunto se utiliza el método copy()

print ("Método copy()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
copia = conjunto.copy()
copia.add('🥗')
print(conjunto)
print(copia)

'''
Funciones con conjuntos
Los conjuntos interactúan con funciones propias de python que permiten secuencias

len()
max()
min()
sum()
Existen otras funciones pueden encontrarse en la documentación y funciones incorporadas
'''

#len(conjunto) retorna la cantidad de elementos del conjunto

print ("Función len()")
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
print(len(conjunto))

'''
max(conjunto) retorna el elemento mayor del conjunto

Si el conjunto contiene cadenas retorna el elemento mayor en orden lexicográfico

Si el conjunto contiene números retorna el valor mayor
'''

#max(conjunto)

print ("Función max()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (max(conjunto))
conjunto = {'🍕','🍔','🍟','🌭'}
print (conjunto)
print(max(conjunto))

'''
min(conjunto) retorna el elemento menor del conjunto

Si el conjunto contiene cadenas retorna el elemento menor en orden lexicográfico

Si el conjunto contiene números retorna el valor menor
'''

#min(conjunto)

print ("Función min()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (min(conjunto))
conjunto = {'🍨','🍔','🍟','🍕'}
print (conjunto)
print(min(conjunto))

'''
sum(conjunto) retorna la suma de los elementos del conjunto

Solo si el conjunto contiene números
'''

print ("Función sum()")
conjunto = {1, 2, 3, 4, 5}
print (conjunto)
print (sum(conjunto))

'''
Operadores con conjuntos
Los conjuntos soportan operadores que permiten realizar operaciones

Operadores de adición
Operadores de comparación
Operadores para operaciones con conjuntos
Operadores para asignación con operaciones
'''

'''
Operadores de adición
Los operadores de adición permiten agregar elementos a un conjunto

Similar al método add()

|= : Update
'''

#|= recibe un conjunto y agrega al conjunto inicial los elementos del conjunto recibido
print ("Operador |=")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨'}
print (conjunto1, conjunto2)
conjunto1 |= conjunto2
print(conjunto1)

'''
Operadores de comparación
Los operadores de comparación permiten comparar conjuntos

== : Igualdad
!= : Desigualdad
< : Es subconjunto y no igual
> : Es superconjunto y no igual
<= : Es subconjunto o igual
>= : Es superconjunto o igual
'''

#== compara si dos conjuntos son iguales

print ("Operador ==")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 == conjunto2)
print(conjunto1 == conjunto3)

#!= compara si dos conjuntos son diferentes

print ("Operador !=")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 != conjunto2)
print(conjunto1 != conjunto3)

#< compara si un conjunto es subconjunto y no igual a otro

print ("Operador <")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 < conjunto2)
print(conjunto1 < conjunto3)

#> compara si un conjunto es superconjunto y no igual a otro

print ("Operador >")
conjunto1 = {'🍔','🍟','🥤','🍕'}
conjunto2 = {'🍔','🍟', '🥤'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 > conjunto2)
print(conjunto1 > conjunto3)

#<= compara si un conjunto es subconjunto o igual a otro

print ("Operador <=")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 <= conjunto2)
print(conjunto1 <= conjunto3)

#>= compara si un conjunto es superconjunto o igual a otro

print ("Operador >=")
conjunto1 = {'🍔','🍟'}
conjunto2 = {'🍔','🍟'}
conjunto3 = {'🍕','🍨'}
print (conjunto1, conjunto2, conjunto3)
print(conjunto1 >= conjunto2)
print(conjunto1 >= conjunto3)

'''
Operadores para operaciones con conjuntos
Los operadores para operaciones con conjuntos permiten realizar operaciones con conjuntos

| : Unión
& : Intersección
- : Diferencia
^ : Diferencia simétrica
'''

#| retorna la unión de dos conjuntos

print ("Operador |")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
union = conjunto1 | conjunto2
print(union)

#& retorna la intersección de dos conjuntos

print ("Operador &")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
interseccion = conjunto1 & conjunto2
print(interseccion)

#- retorna la diferencia de dos conjuntos

print ("Operador -")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
diferencia = conjunto1 - conjunto2
print("1 - 2:",diferencia)
diferencia = conjunto2 - conjunto1
print("2 - 1:",diferencia)

#^ retorna la diferencia simétrica de dos conjuntos

print ("Operador ^")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)

'''
Operadores para asignación con operaciones
Los operadores para asignación con operaciones permiten realizar operaciones con conjuntos y asignar el resultado al conjunto inicial

|= : Unión
&= : Intersección
-= : Diferencia
^= : Diferencia simétrica
'''

#|= recibe un conjunto y agrega al conjunto inicial los elementos del conjunto recibido

print ("Operador |= Unión")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 |= conjunto2
print(conjunto1)

#&= recibe un conjunto y asigna al conjunto inicial la intersección de ambos conjuntos

print ("Operador &= Intersección")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 &= conjunto2
print(conjunto1)

#-= recibe un conjunto y asigna al conjunto inicial la diferencia de ambos conjuntos

print ("Operador -= Diferencia")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print ("1:",conjunto1, "2:",conjunto2)
conjunto1 -= conjunto2
print("1 - 2:",conjunto1)
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 -= conjunto1
print("2 - 1:",conjunto2)

#^= recibe un conjunto y asigna al conjunto inicial la diferencia simétrica de ambos conjuntos

print ("Operador ^= Diferencia simétrica")
conjunto1 = {'🍔','🍟', '🥤'}
conjunto2 = {'🍕','🍨','🥤'}
print (conjunto1, conjunto2)
conjunto1 ^= conjunto2
print(conjunto1)

'''
Conjuntos inmutables
Los conjuntos inmutables son conjuntos que no pueden ser modificados después de su creación

En python se declaran utilizando la función frozenset()
'''

conjunto = frozenset({'🍔','🍕','🥗','🍟','🌭'})
print(conjunto)
print(type(conjunto))

'''
Poseen los mismos métodos que los conjuntos mutables pero no poseen los métodos de adición, 
eliminación y asignaciones con operaciones

conjunto = frozenset({1, 2, 3, 4, 5})
print(conjunto)
print(conjunto.add(6)) # AttributeError: 'frozenset' object has no attribute 'add'
print(conjunto.remove(1)) # AttributeError: 'frozenset' object has no attribute 'remove'
print(conjunto |= {6}) # SyntaxError: invalid syntax

'''

'''
Conjuntos anidados
Los conjuntos anidados son conjuntos que 
contienen otros conjuntos pero tienen que ser inmutables para ser anidados

print ("Conjunto de conjuntos")
conjunto = {frozenset({'🍅','🍓','🍎'}), frozenset({'🍈','🍐','🍏'})}
print(conjunto)
print(type(conjunto))

#Si se intenta anidar un conjunto mutable se lanza un error

print ("Conjunto de conjuntos")
conjunto = {{'🍅','🍓','🍎'}, {'🍈','🍐','🍏'}} #TypeError: unhashable type: 'set'
print(conjunto)
print(type(conjunto))

'''