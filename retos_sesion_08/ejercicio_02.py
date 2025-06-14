'''
Crea una tupla con los siguientes elementos:
'a','b','c','d','e','f','g','h','i','j'
Imprime el primer elemento
Imprime el último elemento
Imprime un slice del índice 3 al 5
Imprime un slice del 5 al 9 con pasos de 3
Imprime un slice del 9 al 0 con pasos de -2
'''

#Tupla
t = ('a','b','c','d','e','f','g','h','i','j')

#Impresiones
print(f"La tupla a analizar es: {t}", end="\n\n")
print(f"El primer elemento es: {t[0]}")
print(f"El último elemento es: {t[-1]}")
print(f"Slice del índice 3 al 5 es: {t[3:5]}")
print(f"Slice del 5 al 9 con pasos de 3: {t[5:9:3]}")
print(f"Slice del 9 al 0 con pasos de -2: {t[9:0:-2]}")