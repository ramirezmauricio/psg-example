'''
Gestión de hábitats en peligro: Crea un diccionario que asocie especies animales en peligro de extinción con información sobre sus hábitats amenazados, lo que permite priorizar la protección de áreas críticas para la supervivencia de estas especies
{"polo norte" : {
    "especies": {"oso polar", "morsa", "ballena"}
  }, "amazonas" : {
    "especies": {"tigre", "mono", "guacamayo"}
  }
}

Añade al diccionario 2 habitats más usando update() con 2 especies cada uno
Existe en el diccionario el habitat 'amazonas'?
Añade al amazonas la especie 'anaconda'
'''

#Diccionario
habitats = {"polo norte" : {
    "especies": {"oso polar", "morsa", "ballena"}
  }, "amazonas" : {
    "especies": {"tigre", "mono", "guacamayo"}
  }
}

#añadir 2 habitats usando update()

habitats.update(sabana={
        "especies": {"elefante", "jirafa"}
    }, arrecife={
        "especies": {"tortuga marina", "coral"}
    }
)

#exite amazonas?

print("exite amazonas?")
print('amazonas' in habitats)

#añadir al "amazonas" la especie "anaconda"

habitats['amazonas']['especies'].add('anaconda')
print(habitats)