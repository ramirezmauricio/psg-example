#Programa de Python que transforma X tiempo en segundos en semanas, días, horas, minutos y segundos

#Variables de entrada
#Cantidad de segundos a convertir
s0 = 1000000

#Resolución del ejercicio
#Cálculo de semanas
t1 = s0 // 60 // 60 // 24 // 7
#Cálculo de días
t2 = (s0 - t1 * 60 * 60 * 24 * 7) // 60 // 60 // 24
#Cálculo de horas
t3 = (s0 - t1 * 60 * 60 * 24 * 7 - t2 * 60 * 60 * 24) // 60 // 60
#Cálculo de minutos
t4 = (s0 - t1 * 60 * 60 * 24 * 7 - t2 * 60 * 60 * 24 - t3 * 60 * 60) // 60
#Cálculo de segundos
t5 = s0 - t1 * 60 * 60 * 24 * 7 - t2 * 60 * 60 * 24 - t3 * 60 * 60 - t4 * 60

#Impresión de resultados
print(s0, "segundos = ", t1, "semanas", t2, "días", t3, "horas", t4, "minutos", t5, "segundos")