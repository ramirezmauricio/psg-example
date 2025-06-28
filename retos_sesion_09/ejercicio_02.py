'''
De la siguiente lista [5,4,3,2,2,2,0,0,1,2] obtener una sub lista inversa utilizando saltos de 3 en 3
'''

#lista
l = [5,4,3,2,2,2,0,0,1,2]

#sub lista inversa usando saltos de 3 en 3
li = l[-1::-3]
print(li)