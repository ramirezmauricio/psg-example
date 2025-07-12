'''
Crea un diccionario con la siguiente tupla de especies animales
(('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅']))
Del diccionario obtén y elimina el valor de la clave 'aves'
Modifica el valor de la clave 'felino' por '🐈'
Cambia la clave canino por caninos y su valor por ['🐶','🐕']
'''

#Diccionario

animales = (('canino', '🐶'), ('felino', '🐱'), ('aves', ['🐦', '🦅']))

animales = dict(animales)

#Eliminamos la clave "aves"

aves = animales.pop("aves")

#Modificar el valor de la clave "felino"

animales['felino'] = '🐈'

#Cambia la clave "canino" por "caninos" y su valor por ['🐶','🐕']
animales['caninos'] = ['🐶', '🐕']
del animales['canino']

print(animales)