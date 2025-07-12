'''
Utiliza un diccionario para almacenar información de un animal marino de un acuario, 
registra información como especie, habitat, dieta, estado de salud, edad y en un set 
los nombre de los responsables de su cuidado
'''

#Introduccion de información

especie_input = input("Introduce la especie del animal: ")
habitat_input= input("Introduce el hábitad del animal: ")
dieta_input = input("Introduce la dieta del animal: ")
salud_input = input("Introduce el estado de salud del animal: ")
edad_input = input("Introduce la edad del animal: ")

#Responsables de su cuidado

cuidado = {"Mauricio", "Mario", "Estefanía"}

#Diccionario de datos

animal_marino = {"Especie":especie_input, "Habitad": habitat_input, "Dieta":dieta_input, "Salud":salud_input, "Edad":edad_input, "Cuidado":cuidado}

print("Diccionario de datos del animal marino")
print(animal_marino)