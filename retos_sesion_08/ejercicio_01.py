'''
Ingresa por teclado tres coordenadas 'x','y','z',
Convierte los valores a enteros almacena los 3 valores en una tupla e imprime el resultado
'''

#Coordenadas
a = input("Primera coordenada: ")
b = input("Segunda coordenada: ")
c = input("Tercera coordenada: ")

#Conversión
a = int(a)
b = int(b)
c = int(c)

#tupla
t = (a, b, c)

#Impresión
print(f"La tupla es {t}")