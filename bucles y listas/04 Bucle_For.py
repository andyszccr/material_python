# Otro tipo de bucle disponible en Python proviene de la observación de que a veces es más importante contar los "giros o vueltas" del bucle que verificar las condiciones.

# Imagina que el cuerpo de un bucle debe ejecutarse exactamente cien veces. Si deseas utilizar el bucle while para hacerlo, puede tener este aspecto:

i = 0
while i < 100:
    # do_something()
    i += 1

print("El bucle se ha ejecutado 100 veces.")
