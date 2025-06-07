#Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome sin importar los espacios, mayúsculas o minúsculas

palabra = input("Escribe tu cadena de texto para saber si es palíndromo o no: ")

#Minimizar todo el texto
min_palabra = palabra.lower()

#Eliminar espacios vacíos
esp_min_palabra = min_palabra.replace(" ", "")

#Caracteres invertidos
inv_esp_min_palabra = esp_min_palabra[-1::-1]

#Comparación
palindromo = (inv_esp_min_palabra == esp_min_palabra)

#Resultados
print(f"Tu cadena de caracteres \"{palabra}\" es un palindromo?: {palindromo}")
print(f"\"{esp_min_palabra}\" fue comparado con \"{inv_esp_min_palabra}\"")