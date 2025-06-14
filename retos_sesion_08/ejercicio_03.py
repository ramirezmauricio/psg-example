'''
Ingresa una pregunta por teclado y almacena el valor en una tupla
Concatena las tupla
('¿', ) + pregunta + ('?', )
Imprime el resultado concatenado
Repite la tupla concatenada 2 veces e imprime el nuevo resultado
'''

#Consulta
a = input("Ingrese una consulta por teclado: ")

#Tupla
t = (a,)

#Tupla concatenada
t = ('¿', ) + t + ('?', )

#Impresión
print(f"La tupla concatenada es: {t}")

#Repetición de la concatenación
t = ('¿', ) + t + ('?', )

#Repetición de la impresión
print(f"La tupla concatenada es: {t}")
 