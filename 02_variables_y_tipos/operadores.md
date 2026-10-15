# 🔗 Operadores de Cadena y Conversión de Tipos

> Notas de apoyo del curso (sección 6 — **Entrada y salida básica**): operadores `+` y `*` aplicados a cadenas, la función `str()`, y resumen de la sección.

---

## 📎 2.6.7 Operadores de cadena

Es hora de regresar a los dos operadores aritméticos **`+`** y **`*`**. Ambos tienen una **función secundaria**: son capaces de hacer algo más que sumar y multiplicar — también pueden **manipular cadenas**, aunque de una manera muy específica.

### Concatenación con `+`

Cuando se aplica `+` a **dos cadenas**, se convierte en un **operador de concatenación**:

```
string + string
```

Simplemente **concatena (junta) dos cadenas en una**. Puede usarse más de una vez en la misma expresión, y en ese caso se comporta con **enlazado del lado izquierdo** (asociatividad izquierda):

```python
"Python" + " " + "PCEP"   # 'Python PCEP'
```

> ⚠️ **No es conmutativo:** a diferencia del operador aritmético, `"ab" + "ba"` **no** es lo mismo que `"ba" + "ab"`.
>
> ⚠️ Para que el `+` sea un concatenador (y no un sumador), **ambos argumentos deben ser cadenas**. **No se pueden mezclar tipos** — `"edad: " + 25` lanza un `TypeError`.

**Ejemplo:**

```python
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print(fnam + " " + lnam)
```

> 💡 Usar `+` para concatenar cadenas permite construir la salida de una manera **más precisa** que con un `print()` puro, incluso enriquecido con `end=` y `sep=`.

### Replicación con `*`

Cuando se aplica `*` a una **cadena y un número** (o número y cadena), se convierte en un **operador de replicación**:

```
string * number
number * string
```

**Replica la cadena el número de veces indicado.**

| Expresión | Resultado |
|---|---|
| `"James" * 3` | `"JamesJamesJames"` |
| `3 * "an"` | `"ananan"` |
| `5 * "2"` (o `"2" * 5`) | `"22222"` (**¡no 10!**) |

> 📌 **Recuerda:** un número **menor o igual a cero** produce una **cadena vacía** `""`.

**Ejemplo — dibujar un rectángulo** (el `+` en su nuevo rol de concatenador):

```python
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
```

```
+----------+
|          |
|          |
|          |
|          |
|          |
```

> 📌 Fíjate en el uso de los **paréntesis** en la segunda línea: agrupan la cadena completa antes de replicarla 5 veces.

> 🎨 **¡Intenta practicar para crear otras formas o tu propia obra de arte!**

---

## 🔢 2.6.8 Conversiones de tipos una vez más — `str()`

Ya sabes usar `int()` y `float()` para convertir una **cadena a un número**. Esa conversión **no es de un solo sentido**: también se puede convertir un **número a una cadena**, algo **más fácil y seguro** — esta operación **siempre es posible**.

La función que hace esto es **`str()`**:

```
str(number)
```

> 💡 Sinceramente, `str()` puede hacer **mucho más** que transformar números en cadenas; eso lo veremos después.

### El triángulo rectángulo otra vez

Veamos un programa que calcula la hipotenusa usando `str()`:

```python
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hyp = (leg_a ** 2 + leg_b ** 2) ** 0.5
print("La hipotenusa mide " + str(hyp) + " unidades.")
```

```
Ingresa la longitud del primer cateto: 3
Ingresa la longitud del segundo cateto: 4
La hipotenusa mide 5.0 unidades.
```

> 📌 Gracias a `str()` podemos pasar el resultado a `print()` como **una sola cadena**, **sin usar comas**.

---

## 🧪 Laboratorios de la sección

### LAB 2.6.9 — Entradas y salidas simples

**Escenario:** completar el código para evaluar las cuatro operaciones aritméticas básicas e imprimir los resultados. Todavía no hay que protegerse de la división entre cero.

```python
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)
```

### LAB 2.6.10 — Operadores y expresiones

**Escenario:** evaluar una expresión con fracciones anidadas y asignarla a `y`, cuidando la **prioridad de operadores** y usando cuantos paréntesis sean necesarios:

```
        1
y = ------------
            1
    x + ------------
                1
        x + --------
                1
            x + -
                x
```

**Solución validada** (coincide con los 4 datos de prueba del curso):

```python
x = float(input("Ingresa el valor para x: "))
y = 1 / (x + (1 / (x + (1 / (x + 1 / x)))))
print("y =", y)
```

| Entrada | Salida esperada |
|---|---|
| `1` | `y = 0.6000000000000001` |
| `10` | `y = 0.09901951266867294` |
| `100` | `y = 0.009999000199950014` |
| `-5` | `y = -0.19258202567760344` |

### LAB 2.6.11 — Cálculo de horas (operadores y expresiones – 2)

**Escenario:** dada una hora de inicio (0..23), minutos (0..59) y una duración en minutos, mostrar la **hora final**. Pista: el operador **`%`** es clave.

```python
hour = int(input("Hora inicial (0-23): "))
minute = int(input("Minuto inicial (0-59): "))
duration = int(input("Duración en minutos: "))

total_minutes = hour * 60 + minute + duration
final_hour = (total_minutes // 60) % 24
final_minute = total_minutes % 60
print(str(final_hour) + ":" + str(final_minute))
```

| Entrada | Salida esperada |
|---|---|
| `12`, `17`, `59` | `13:16` |
| `23`, `58`, `642` | `10:40` |
| `0`, `1`, `2939` | `1:0` |

---

## 📝 2.6.12 Resumen de sección

1. **`print()`** envía datos a la consola; **`input()`** obtiene datos de la consola.
2. `input()` tiene un parámetro opcional: la **cadena de mensaje** (prompt):

   ```python
   name = input("Ingresa tu nombre: ")
   print("Hola, " + name + ". ¡Un gusto conocerte!")
   ```

3. Cuando se invoca `input()`, el **flujo del programa se detiene** hasta que el usuario escribe algo y pulsa **Enter**. Esto sirve también para **pausar** el programa:

   ```python
   print("\nPresiona Enter para terminar el programa.")
   input()
   print("FIN.")
   ```

4. El **resultado** de `input()` es **una cadena**. Se pueden unir cadenas con **`+`** (concatenación):

   ```python
   num_1 = input("Ingresa el primer número: ")   # 12
   num_2 = input("Ingresa el segundo número: ")   # 21
   print(num_1 + num_2)                            # 1221
   ```

5. También se pueden **multiplicar** cadenas con **`*`** (replicación):

   ```python
   my_input = input("Ingresa algo: ")   # hola
   print(my_input * 3)                  # holaholahola
   ```

---

## ✅ Tabla resumen

| Concepto | Idea clave |
|---|---|
| `string + string` | **Concatenación**: junta dos cadenas; no conmutativo, sin mezclar tipos |
| `string * number` | **Replicación**: repite la cadena; ≤ 0 produce `""` |
| `str()` | Convierte **cualquier valor** a cadena (siempre posible) |
| `input()` | Lee de la consola, **siempre devuelve `str`**, y detiene el programa |