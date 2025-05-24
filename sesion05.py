#Tipo de dato del valor "1"
print(type(1))

#Asignación de una variable
nombre_variable = "valor"

#Ejemplo de un cálculo correcto y variables nombradas incorrectamente
x1q3z9ahd = 35.0
x1q3z9afd = 12.50
x1q3p9afd = x1q3z9ahd * x1q3z9afd
print(x1q3p9afd)

#Ejemplo de un cálculo correto y variables nombradas correctamente
horas = 35.0
tarifa = 12.50
salario = horas * tarifa
print(salario)

#Tipos de datos numéricos
#Int - Intergers o Enteros, números naturales
#Declaración

# Valor 10 Entero
print (10)
print ( type (10) )

# Variable 100 Entero
variable = 100
print (variable)
print ( type (variable) )

# Variable 20 Entero
variable_2 = int (20)
print (variable_2)
print ( type (variable_2) )

#Diferentes tipos de bases
#Declaración

# Valor 10 en base decimal
print ("Base decimal")
print (10)
# Valor 10 en binario
print ("Base binaria")
print (0b1010)
# Valor 10 en octal
print ("Base octal")
print (0o12)
# Valor 10 en hexadecimal
print ("Base hexadecimal")
print (0xa)

#Los números no tienen límites
# Entero con 60 dígitos
variable_3 = 123456789012345678901234567890123456789012345678901234567890
print (variable_3)
print (type (variable_3))

#Float - Floating point o punto flotante, números reales
#Declaración

# Valor 0.5 Flotante
print (0.5)
print ( type (0.5) )

# Variable 0.100546 Flotante
variable_4 = 0.100546
print (variable_4)
print ( type (variable_4) )

# Variable 1 Flotante
variable_7 = float (1)
print(variable_7)
print ( type (variable_7) )

# Valor 2.0e-3 Flotante
variable_6 = 2.0e-3
print(variable_6)
print ( type (variable_6) )

# Precisión de 17 decimales
variable_5 = 0.9999999999999999
print(variable_5)
print ( type (variable_5) )

#Operadores aritméticos
a = 10
b = 3
# Suma
print ("Suma")
print (a + b)
# Resta
print ("Resta")
print (a - b)
# Multiplicación
print ("Multiplicación")
print (a * b)
# División
print ("División")
print (a / b)
# Potencia
print ("Potencia")
print (a ** b)
# Módulo o residuo
print ("Módulo o residuo")
print (a % b)
# División entera
print ("División entera")
print (a // b)


#EJERCICIO 1
m = 300
s = 3600
h = m // 60 + s // 3600
print("horas en total:", h)

#Operadores de comparación
print ("Operadores de comparación")
comparar = 10
print (comparar < 10)
print (comparar > 10)
print (comparar == 10)
print (comparar <= 10)
print (comparar >= 10)
print (comparar != 10)

print ("Operadores de comparación con int - float")
entero = 10
flotante = 10.0
print (entero < flotante)
print (entero > flotante)
print (entero == flotante)
print (entero <= flotante)
print (entero >= flotante)
print (entero != flotante)