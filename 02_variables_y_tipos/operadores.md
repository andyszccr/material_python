# 🔗 Operadores en Python: cadena, comparación y lógicos

> Notas de apoyo del curso: **sección 6 — Entrada y salida básica** (operadores `+` y `*` aplicados a cadenas, la función `str()`, resumen de la sección), **sección 7 — Operadores de comparación**, **3.1.13 — Resumen de sección: operadores relacionales**, **operadores lógicos: `and`, `or`, `not`** (tablas de verdad, prioridades y leyes de De Morgan) y **3.3.4 — Operadores bit a bit** (`&`, `|`, `~`, `^`: tablas de verdad, trucos de memoria y diferencias con los operadores lógicos).

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

---

## 📊 Operadores de comparación

> Notas de la sección **7 — Estructura alternativa**: los seis operadores que comparan valores.

### Igualdad: el operador `==` (igual a)

El operador **`==`** compara los **valores** de dos operandos. Si son iguales, el resultado de la comparación es **`True`**; si no lo son, es **`False`**.

Observa esta comparación — ¿cuál es el resultado?

```python
var == 0
```

> 📌 **No podemos encontrar la respuesta si no sabemos qué valor está almacenado actualmente en `var`.** Si la variable ha cambiado muchas veces durante la ejecución, o si su valor inicial se ingresa desde la consola, Python solo puede responder a esta pregunta **en tiempo de ejecución**.

**Ejemplo — el programador con insomnio:** debe contar ovejas negras y blancas por separado, siempre y cuando haya **exactamente el doble** de ovejas negras que de blancas. La pregunta es:

```python
black_sheep == 2 * white_sheep
```

Debido a la **baja prioridad** del operador `==`, la pregunta se trata como si estuviera escrita así:

```python
black_sheep == (2 * white_sheep)
```

### Desigualdad: el operador `!=` (no es igual a)

El operador **`!=`** también compara los valores de dos operandos. La diferencia con `==`: si los valores **son iguales**, el resultado es **`False`**; si **no son iguales**, es **`True`**.

```python
var = 0  # Asignando 0 a var
print(var != 0)   # False

var = 1  # Asignando 1 a var
print(var != 0)   # True
```

### Mayor que: el operador `>`

También se puede hacer una pregunta de comparación usando el operador **`>` (mayor que)**. Si deseas saber si hay **más ovejas negras que blancas**:

```python
black_sheep > white_sheep   # Mayor que
```

**`True`** lo confirma; **`False`** lo niega.

### Mayor o igual que: el operador `>=`

El operador mayor que tiene una variante especial, **no estricta**, denotada de manera diferente que la notación aritmética clásica: **`>=` (mayor o igual que)**. Hay **dos signos subsecuentes**, no uno.

```python
centigrade_outside >= 0.0   # Mayor o igual que
```

> 📌 **Prioridad y asociatividad:** los operadores de comparación (`>`, `>=`, `<`, `<=`) son **operadores binarios con enlazado del lado izquierdo**, y su prioridad es **mayor** que la de `==` y `!=`. Es decir: `a > b == c` se evalúa como `(a > b) == c`.

### Menor que `<` y menor o igual que `<=`

Como probablemente ya hayas adivinado, los operadores son **`<` (menor que)** y su hermano no estricto **`<=` (menor o igual que)**:

```python
current_velocity_mph < 85   # Menor que
current_velocity_mph <= 85  # Menor o igual que
```

### Tabla resumen de comparación

| Operador | Signo | Resultado `True` cuando... |
|---|---|---|
| igual a | `==` | los valores son **iguales** |
| no igual a | `!=` | los valores son **distintos** |
| mayor que | `>` | el operando izquierdo **>** derecho |
| mayor o igual que | `>=` | izquierdo **≥** derecho |
| menor que | `<` | izquierdo **<** derecho |
| menor o igual que | `<=` | izquierdo **≤** derecho |

> 📌 Todos son **binarios**, con **enlazado del lado izquierdo**. Prioridad: `<`, `<=`, `>`, `>=` son **más altas** que `==` y `!=`.

---

## 🏁 3.1.13 Resumen de sección — operadores relacionales

1. Los operadores de **comparación** (o también denominados operadores **relacionales**) se utilizan para comparar valores. La siguiente tabla ilustra cómo funcionan, asumiendo que **`x = 0`**, **`y = 1`** y **`z = 0`**:

| Operador | Descripción | Ejemplo |
|---|---|---|
| `==` | Devuelve `True` si los valores de los operandos son **iguales**, y `False` de lo contrario. | `x == y` → `False`<br>`x == z` → `True` |
| `!=` | Devuelve `True` si los valores de los operandos **no son iguales**, y `False` de lo contrario. | `x != y` → `True`<br>`x != z` → `False` |
| `>` | Devuelve `True` si el valor del operando izquierdo es **mayor** que el valor del operando derecho, y `False` de lo contrario. | `x > y` → `False`<br>`y > z` → `True` |
| `<` | Devuelve `True` si el valor del operando izquierdo es **menor** que el valor del operando derecho, y `False` de lo contrario. | `x < y` → `True`<br>`y < z` → `False` |
| `>=` | Devuelve `True` si el valor del operando izquierdo es **mayor o igual** que el valor del operando derecho, y `False` de lo contrario. | `x >= y` → `False`<br>`x >= z` → `True`<br>`y >= z` → `True` |
| `<=` | Devuelve `True` si el valor del operando izquierdo es **menor o igual** que el valor del operando derecho, y `False` de lo contrario. | `x <= y` → `True`<br>`x <= z` → `True`<br>`y <= z` → `False` |

**Verificación ejecutable** (todas las salidas coinciden con la tabla):

```python
x, y, z = 0, 1, 0
print(x == y, x == z)   # False True
print(x != y, x != z)   # True False
print(x > y, y > z)     # False True
print(x < y, y < z)     # True False
print(x >= y, x >= z, y >= z)   # False True True
print(x <= y, x <= z, y <= z)   # True True False
```
---

## ⚖️ Operadores lógicos: `and`, `or`, `not`

Cuando queremos combinar **dos o más condiciones** en una sola expresión, entran en juego los **operadores lógicos**.

> 📖 Del curso: si **tú estás en el centro comercial** **y** **yo estoy en el centro comercial**, uno de nosotros le comprará un regalo a mamá — la palabra **`and`** significa que la compra depende de **ambas** condiciones a la vez (en lógica: una **conjunción**). Si en su lugar decimos que estás **o** yo estoy, basta con que se cumpla **una sola** (en lógica: una **disyunción**). Python construye conjunciones y disyunciones con los **operadores lógicos**.

### `and` — conjunción

Es un operador **binario** con una prioridad **inferior a la de los operadores de comparación**. Esto permite codificar condiciones complejas **sin usar paréntesis**:

```python
counter > 0 and value == 100   # se lee como (counter > 0) and (value == 100)
```

El resultado se determina sobre la base de la **tabla de verdad**. Para la conjunción `A and B`:

| Argumento A | Argumento B | `A and B` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |

> 💡 **`and` solo devuelve `True` cuando los dos argumentos son `True`** — basta con un `False` en cualquier argumento para que el resultado sea `False`.

### `or` — disyunción

Es un operador **binario** con una prioridad **más baja que `and`** (del mismo modo que `==` tiene una prioridad más baja que `<` — por eso importa el orden en que se agrupan). Su tabla de verdad:

| Argumento A | Argumento B | `A or B` |
|---|---|---|
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `True` |

> 💡 **`or` solo devuelve `False` cuando los dos argumentos son `False`** — basta con un `True` en cualquier argumento para que el resultado sea `True`.

> 📌 Prioridad entre operadores lógicos (de mayor a menor): **`not` → `and` → `or`**.

### `not` — negación

Además, hay otro operador que se puede aplicar para construir condiciones. Es un operador **unario** que realiza una **negación lógica**. Su funcionamiento es simple: **convierte la verdad en falso y lo falso en verdad**.

Se escribe como la palabra `not`, y el curso señala que su **prioridad es muy alta**: *igual que la de los unarios `+` y `-`*. Su tabla de verdad es simple:

| Argumento | `not Argumento` |
|---|---|
| `False` | `True` |
| `True` | `False` |

> 🔎 **Verificado con Python:** `not 2 == 3` devuelve `True`, es decir Python lee `not (2 == 3)` — las **comparaciones** se agrupan antes que `not`. Por eso el propio curso escribe los paréntesis explícitos: `not (var <= 0)` — **úsalos también** para que la intención sea siempre inequívoca y la legibilidad mejore.

---

## 🧪 Expresiones lógicas — prácticas del curso

### Equivalencias con `not`

Creemos una variable llamada `var` y le demos el valor `1`. Las siguientes condiciones son **equivalentes**:

```python
var = 1

# Ejemplo 1:
print(var > 0)         # True
print(not (var <= 0))  # True — la misma condición, negada

# Ejemplo 2:
print(var != 0)        # True
print(not (var == 0))  # True — la misma condición, negada
```

### Las leyes de De Morgan

Puede que ya estés familiarizado con las **leyes de De Morgan**. Dicen que:

- La **negación de una conjunción** es la **disyunción de las negaciones**.
- La **negación de una disyunción** es la **conjunción de las negaciones**.

En Python:

```python
not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)
```

> 📌 Los paréntesis están allí para **mejorar la legibilidad**; en expresiones largas, además, evitan que tengamos que recordar prioridades de memoria.

### Otras notas importantes

- **No existe la forma abreviada `op=`** para estos operadores: ninguno de los operadores lógicos de dos argumentos se puede usar como `and=` u `or=`.
- Los operadores lógicos toman sus argumentos **como un todo**, independientemente de cuántos bits contengan: **cero** (todos los bits en 0) significa `False`; **distinto de cero** (algún bit en 1) significa `True`, y el resultado siempre es `False` o `True`:

  ```python
  i = 1
  j = not not i   # True si i no es cero; False si i es cero
  ```

**Verificación ejecutable** (todas las salidas coinciden con las tablas y equivalencias):

```python
var = 1

# Tablas de verdad de and y or
for a in (False, True):
    for b in (False, True):
        print(a, b, "and->", a and b, "or->", a or b)

print(not False, not True)            # True False
print(var > 0, not (var <= 0))        # True True
print(var != 0, not (var == 0))       # True True

# De Morgan, comprobadas para las 4 combinaciones posibles de p y q
print(all((not (p and q)) == ((not p) or (not q))
          for p in (False, True) for q in (False, True)))   # True
print(all((not (p or q)) == ((not p) and (not q))
          for p in (False, True) for q in (False, True)))   # True
```

---

## 0️⃣ 3.3.4 Operadores bit a bit

Sin embargo, hay **cuatro operadores** que nos permiten **manipular bits de datos individuales**. Se denominan **operadores bit a bit** (*bitwise*).

Cubren todas las operaciones que mencionamos anteriormente en el contexto lógico, y un operador adicional: **`or` (significa *o exclusivo*)**, que se denota como **`^`** (signo de intercalación). Aquí están todos ellos:

- **`&`** (*ampersand*) — **conjunción** a nivel de bits;
- **`|`** (barra vertical) — **disyunción** a nivel de bits;
- **`~`** (tilde) — **negación** a nivel de bits;
- **`^`** (signo de intercalación / *caret*) — **o exclusivo** a nivel de bits (*xor*).

### Tablas de verdad bit a bit

**Operaciones bit a bit (`&`, `|` y `^`):**

| Argumento A | Argumento B | `A & B` | `A \| B` | `A ^ B` |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

**Operaciones bit a bit (`~`):**

| Argumento | `~ Argumento` |
|---|---|
| 0 | 1 |
| 1 | 0 |

### 🧠 Hagámoslo más fácil

- **`&`** requiere **exactamente dos `1`s** para proporcionar `1` como resultado;
- **`|`** requiere **al menos un `1`** para proporcionar `1` como resultado;
- **`^`** requiere **exactamente un `1`** para proporcionar `1` como resultado (si hay dos unos, el resultado es `0`).

### ⚠️ Dos advertencias importantes

1. **Los argumentos de estos operadores deben ser enteros** — no debemos usar flotantes aquí: Python lanza `TypeError: unsupported operand type(s) for &: 'float' and 'int'`.
2. **La diferencia con los operadores lógicos es importante:** los operadores **lógicos no penetran en el nivel de bits** de su argumento — solo les interesa el **valor entero final** (`0` → `False`, distinto de `0` → `True`). Los operadores **a nivel de bits son más estrictos**: tratan con **cada bit por separado**. Si asumimos que un entero ocupa **64 bits**, puedes imaginar la operación como **64 evaluaciones simultáneas** del operador lógico para cada par de bits de los argumentos — en la vida real, todas se realizan **al mismo tiempo** (simultáneamente).

> 🔎 **Verificado con Python:** la tabla de `~` muestra la negación de **un solo bit**; en Python `~` trabaja en **complemento a dos** sobre todos los bits del entero, por eso `~0` es `-1`, `~1` es `-2` y `~15` es `-16` (lo comprobarás en el ejemplo de la siguiente sección).

---

## 🔍 Diferencias: operadores lógicos vs. a nivel de bits

Supongamos que se han realizado las siguientes asignaciones:

```python
valor1 = 15
valor2 = 22
```

Si asumimos que los enteros se almacenan con 32 bits, los valores binarios de las dos variables serán:

```text
valor1:          00000000000000000000000000001111
valor2:          00000000000000000000000000010110
valor1 & valor2: 00000000000000000000000000000110
```

- **`valor1 and valor2`** — conjunción **lógica**: ambas variables son distintas de cero, por lo que se considera que representan `True`. Al consultar la tabla de verdad de `and`, el resultado es **`True`**.
  > 🔎 En Python, `and` devuelve uno de sus **operandos**, no literalmente `True`: `15 and 22` devuelve `22`, que es *truthy* — por eso conviene comprobarlo con `bool(valor1 and valor2)` → `True`.
- **`valor1 & valor2`** — conjunción **bit a bit**: el operador `&` opera con **cada par de bits correspondiente por separado** → `00000000000000000000000000000110`, es decir **6**.

```python
print(bin(valor1))            # 0b1111
print(bin(valor2))            # 0b10110
print(bin(valor1 & valor2))   # 0b110
print(valor1 & valor2)        # 6
```

### 🔁 Operador de negación

Primero el lógico: con `valor1 = 15` (número distinto de cero → `True`), **`not valor1`** nos devuelve el valor opuesto → **`False`**.

La negación a nivel de bits es así: **`~valor1`** → **`-16`**. Puede parecer un poco sorprendente, pero no lo es en absoluto: los números negativos se representan en **complemento a dos**.

```text
valor1:   00000000000000000000000000001111
~valor1:  11111111111111111111111111110000
```

### ✍️ Formas abreviadas (`op=`)

Cada uno de estos operadores **de dos argumentos** sí se puede usar en forma abreviada (a diferencia de los operadores lógicos, que no la tienen):

| Escritura completa | Forma abreviada |
|---|---|
| `x = x & y` | `x &= y` |
| `x = x \| y` | `x \|= y` |
| `x = x ^ y` | `x ^= y` |

**Verificación ejecutable:**

```python
valor1, valor2 = 15, 22
print(bin(valor1), bin(valor2))     # 0b1111 0b10110
print(valor1 & valor2)              # 6
print(bool(valor1 and valor2))      # True — el lógico solo mira el valor entero
print(not valor1, ~valor1)          # False -16

x = 12
x &= 5
print(x)                            # 4
```