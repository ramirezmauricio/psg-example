#Agregar 5 Ejemplos con otras funciones no vistas en la sesión
#Utilizar la documentación Métodos de cadenas

print("\n")
cadena = "Esto usaré para todos los ejemplos."
print(f"La cadena original es: \"{cadena}\"")
print("\n")


#Ejemplo 1: Center
print("Ejemplo 1: Center")
print("center coloca a la cadena de caracteres dentro de otros caracteres")
print(cadena.center(50, '*'))
print("\n") 

#Ejemplo 2: isupper

print("Ejemplo 2: isupper")
print("isupper nos ayuda a saber si todos los caracteres están en mayúscula")
print(cadena.isupper())
print("\n") 

#Ejemplo 3: rstrip

print("Ejemplo 3: rstrip")
print("rstrip nrstrip elimina del final de la cadena los caracteres que le indiques")
print("si no se indica nada se eliminan espacios vacíos")
print("rstrip por defecto")
print(cadena.rstrip())
print("rstrip eliminando el caracter \"emplos.\"")
print(cadena.rstrip("emplos."))
print("\n") 

#Ejemplo 4: removeprefix
print("Ejemplo 4: removeprefix")
print("removeprefix elimina un prefijo exacto de la cadena, pero sólo si aparece justo al inicio")
print("si no coincide, devuelve la cadena original")
print("haremos la prueba con \"Esto usar\"")
print(cadena.removeprefix("Esto usar"))
print("\n") 

#Ejemplo 5: isascii
print("Ejemplo 5: isascii")
print("isascii() devuelve True si todos los caracteres de la cadena están en el rango ASCII 0–127")
print(cadena.isascii())
print("\n") 

'''
Funciones incorporadas (built-ins):

str()

len()

input()

Conversión de tipos vía int(), float(), bool()

print()

Métodos de cadenas (cadena.metodo()):

Transformación de mayúsculas/minúsculas:

upper(), lower(), capitalize(), title(), swapcase()

Búsqueda y conteo:

count(), find(), rfind()

Comprobación de contenido:

isdigit(), isalpha(), isalnum()

División y unión:

split(), join()

Limpieza y reemplazo:

strip(), replace()

Formateo:

format() y f-strings (f"…")


'''