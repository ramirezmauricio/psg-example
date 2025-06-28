'''
Crear una lista de personas con 10 nombres de personas
Obtener una sub lista de 5 a 9 con saltos de 2 en 2
Buscar si existe el nombre "José" en la lista original
Ordenar la sub lista alfabéticamente a-z
Ordenar la lista original alfabéticamente descendente z-a
'''

#lista de personas
l = ["mauricio", "hugo", "manuel", "oscar", "ronaldo", "edgar", "sebastian", "harold", "samuel", "vladimir"]

#sub lista de 5 a 9 con saltos de 2 en 2
l1 = l[4:8:2]
print(l1)

#existencia de "José" en la lista
print("Existe el nombre de José en la lista?")
print("José" in l)

#ordenar la sub lista
l1.sort()
print(l1)

#ordenar la lista original alfabeticamente descendente
l.sort(reverse=True)
print(l)