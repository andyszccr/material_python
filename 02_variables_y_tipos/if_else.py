# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number)

# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number)

print()
print()

# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1
 
# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2
 
# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3
 
# Imprime el resultado.
print("El número más grande es:", largest_number)


largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir a la línea 02

# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.
 
largest_number = max(number1, number2, number3)
 
# Imprime el resultado.
print("El número más grande es:", largest_number)


name = input("Introduce el nombre de la flor: ")

if name == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
elif name == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO!, ¡No", name + "!")

name_carro = input("Introduce el nombre del carro: ")

if name_carro == "Audi":
    print("Si, ¡El Ferrari es el mejor carro de todos los tiempos!")
elif name_carro == "ferrari":
    print("No, ¡quiero un gran Ferrari!")
else:
    print("¡Ferrari!, ¡No", name_carro + "!")


income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Escribe tu código aquí.

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
 

year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")


#---------------------------------------------------
x = 10
 
if x > 5: # True
    if x == 6: # False
        print("anidado: x == 6")
    elif x == 10: # True
        print("anidado: x == 10")
    else:
        print("anidado: else")
else:
    print("else")

 
#---------------------------------------------------\
x = 10

if x == 10: # True
    print("x == 10")

if x > 15: # False
    print("x > 15")

elif x > 10: # False
    print("x > 10")

elif x > 5: # True
    print("x > 5")

else:
    print("else no será ejecutado")


x = 10

if x > 5: # primera condición
    print("x es mayor que 5")  # Ejecutado si la primera condición es True.

if x < 10: # segunda condición
    print("x es menor que 10")  # Ejecutado si la segunda condición es True.

if x == 10: # tercera condición
     print("x es igual a 10")  # Ejecutado si la tercera condición es True.



