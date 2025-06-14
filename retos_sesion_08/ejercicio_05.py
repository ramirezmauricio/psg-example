'''
De la siguiente guía telefónica
- Jhon, 591123456, Villa fátima
- Jane, 591546324, Obrajes
- Dogg, 591222421, Miraflores
- Kity, 591753159, Achumani
Genera una tupla anidada e imprime el resultado

Ejemplo:

((Nombre, Telf, Dir), (Nombre, Telf, Dir), ...)
'''

#Datos
d1 = ("Jhon", "591123456", "Villa fátima")
d2 = ("Jane", "591546324", "Obrajes")
d3 = ("Dogg", "591222421", "Miraflores")
d4 = ("Kity", "591753159", "Achumani")

#Tupla anidada
d = (d1, d2, d3, d4)

#Impresión:
print(f"Los datos de la tupla anidada son: {d}")