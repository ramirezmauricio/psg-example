#Programa en Python que convierte las siguientes temperaturas de grados Fahrenheit a grados Celcius

#Variables de entrada
#Valores a convertir en grados Fahrenheit
f1 = 25
f2 = 300
f3 = 76

#Resolución del ejercicio
#Conversión de fahrenheti a grados celsius
c1 = (f1 - 32) * 5 / 9
c2 = (f2 - 32) * 5 / 9
c3 = (f3 - 32) * 5 / 9

#Impresión de resultados
print(f1, "ºF equivalen aproximadamente a: ", round(c1, 2), "ºC", sep="")
print(f2, "ºF equivalen aproximadamente a: ", round(c2, 2), "ºC", sep="")
print(f3, "ºF equivalen aproximadamente a: ", round(c3, 2), "ºC", sep="")