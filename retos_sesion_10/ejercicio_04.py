'''
Jane y Jhon llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a un candy bar. Quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. A continuación tienes los postres que han ido pidiendo en cada salida:
Jane: Lemon Pie, Brownie, Tarta de Manzana,
      Helado de Chocolate, Flan
Jhon: Carrot Cake, Croissant de Chocolate,
      Lemon Pie, Tarta de Manzana, Pudding
Si la cantidad de postres que tienen en común es mayor al 50% 
entonces son compatibles,
de lo contrario quieren replantear su relación
'''

#conjuntos de comidas
jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
jhon = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

#cantidad de datos
cantidad_jane = len(jane)
cantidad_jhon = len(jhon)

#cantidad de comidas en común 
comun = jane.intersection(jhon)
cantidad_comun = len(comun)

#cálculo del 50% de compatiblidad

print("Es desde el punto de vista de jane una relación compatible?")
compatiblidad_jane = cantidad_comun / cantidad_jane * 100
print("cantidad de comidas de jane:", cantidad_jane)
print("cantidad de comidas en común:", cantidad_comun)
print("porcentaje de comtabilidad:", compatiblidad_jane, "%")
print(compatiblidad_jane > 50)

print("Es desde el punto de vista de jhon una relación compatible?")
compatiblidad_jhon = cantidad_comun / cantidad_jhon * 100
print("cantidad de comidas de jhon:", cantidad_jhon)
print("cantidad de comidas en común:", cantidad_comun)
print("porcentaje de comtabilidad:", compatiblidad_jhon, "%")
print(compatiblidad_jhon > 50)

print("su relación es compatible?:", compatiblidad_jane > 50 and compatiblidad_jhon > 50)

print("deberían replantear su relación?:", not(compatiblidad_jane > 50 and compatiblidad_jhon > 50))
