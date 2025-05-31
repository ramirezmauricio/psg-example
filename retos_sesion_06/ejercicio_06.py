#¿El cubo de 300 se encuentra en el siguiente rango? [N > 0 & N < 27_000_000]

n = 300
rango_inicial = 0
rango_final = 27000000

#Cálculo de cubo
cubo = n ** 3


print("¿El cubo de", n, "se encuentra en el siguiente rango? [N > 0 & N < 27_000_000]")
rango_cubo = (cubo < rango_inicial) and (cubo > rango_final)
print("Respuesta:", rango_cubo)