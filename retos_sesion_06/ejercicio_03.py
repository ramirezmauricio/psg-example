#Imprime una tabla de verdad para la siguiente sentencia: "Un sistema de seguridad controla el acceso a una habitación, la puerta sólo se abre si se introduce una tarjeta válida o la huella dactilar, pero no ambas al mismo tiempo. Si se introduce la tarjeta y la huella dactilar, la puerta no se abre. ¿Qué operador lógico se puede utilizar?"

#Usar xor, osea !=

#Tabla de resultados
tarjeta_valida = True
huella_dactilar = True
print("tarjeta válida = ",tarjeta_valida, ", huella dactilar = ", huella_dactilar, ", se abre la puerta? = ", tarjeta_valida != huella_dactilar)
tarjeta_valida = True
huella_dactilar = False
print("tarjeta válida = ",tarjeta_valida, ", huella dactilar = ", huella_dactilar, ", se abre la puerta? = ", tarjeta_valida != huella_dactilar)
tarjeta_valida = False
huella_dactilar = True
print("tarjeta válida = ",tarjeta_valida, ", huella dactilar = ", huella_dactilar, ", se abre la puerta? = ", tarjeta_valida != huella_dactilar)
tarjeta_valida = False
huella_dactilar = False
print("tarjeta válida = ",tarjeta_valida, ", huella dactilar = ", huella_dactilar, ", se abre la puerta? = ", tarjeta_valida != huella_dactilar)
