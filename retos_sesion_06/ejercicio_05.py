#Comparar los números 44 y 98 , 111 y 333 , comprobar si tienen la misma paridad ambos pares o ambos impares

a1 = 44
a2 = 98

b1 = 111
b2 = 333

print("Comprobando paridad grupo A")
print("Ambos son pares o ambos son impares?")
paridad_a = (a1 % 2 == 0) == (a2 % 2 == 0)
print("Respuesta:", paridad_a)


print("Comprobando paridad grupo B")
print("Ambos son pares o ambos son impares?")
paridad_b = (b1 % 2 == 0) == (b2 % 2 == 0)
print("Respuesta:", paridad_b)