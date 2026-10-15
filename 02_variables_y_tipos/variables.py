# variables.py — Variables y tipos de datos
# Este script demuestra los conceptos básicos de variables en Python.

# 1. Crear variables (sin declarar el tipo: lo toma del valor)
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

print()

# 2. Concatenación de cadenas con el operador +
var2 = "3.8.5"
print("Python version: " + var2)

print()

# 3. Asignación de un nuevo valor a una variable existente
print("asignacion nuevo valor a la variable var3")
var3 = 1
print(var3)
var3 = var3 + 1
print(var3)
var3 = 3
print(var3)
var3 = 2 + 2
print(var3)

print()

# 4. Tipos de datos: la función type() muestra el tipo de la variable
mi_entero = 5
mi_flotante = 4.5
mi_cadena = "hola"
mi_booleano = True
print(type(mi_entero))      # <class 'int'>
print(type(mi_flotante))    # <class 'float'>
print(type(mi_cadena))      # <class 'str'>
print(type(mi_booleano))    # <class 'bool'>

print()

# 5. Tipado dinámico: el tipo puede cambiar al cambiar el valor
var = 5
print(type(var))    # <class 'int'>
var = "hola"
print(type(var))    # <class 'str'>

print()

# 6. Asignación múltiple: varias variables reciben el mismo valor
a = b = c = 0
print(a, b, c)

print()

# 7. Operadores abreviados (asignación augmentada)
x = 2
x *= 3      # x = x * 3
print(x)    # 6
y = 10
y += 1      # y = y + 1
y -= 3      # y = y - 3
print(y)    # 8

print()

# 8. Teorema de Pitágoras: la hipotenusa de un triángulo rectángulo
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

print()

# 9. Borrar una variable con del
temp = 99
del temp
# print(temp)  # NameError si se descomenta: la variable ya no existe
print("temp fue borrada con del")
