# Empleando una variable counter para salir del bucle
# Observa el fragmento de código a continuación:

counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)