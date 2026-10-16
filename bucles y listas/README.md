# 🔁 Bucles con `while` y `for`

> Notas de apoyo del curso: **3.2.2 — Un bucle infinito** (qué es un bucle sin fin, `Ctrl-C` y el patrón de **bucle con centinela**), **el bucle `for` con `range()` de tres argumentos** y **LAB 3.2.7 — Fundamentos del bucle `for`: contar *mississippily***.

---

## ♾️ 3.2.2 Un bucle infinito

Un **bucle infinito** (también denominado **bucle sin fin**) es una secuencia de instrucciones en un programa que se repite **indefinidamente**.

Este es un ejemplo de un bucle que **no puede finalizar** su ejecución:

```python
while True:
    print("Estoy atrapado dentro de un bucle.")
```

Este bucle imprimirá infinitamente `Estoy atrapado dentro de un bucle.` en la pantalla.

> 💡 **Para la mejor experiencia de aprendizaje:** inicia IDLE, crea un archivo nuevo, copia y pega el código anterior, guarda tu archivo y ejecuta el programa. Lo que verás es la secuencia interminable de cadenas impresas de `"Estoy atrapado dentro de un bucle."` en la ventana de la consola de Python. Para finalizar tu programa, simplemente presiona **`Ctrl-C`** (o **`Ctrl-Break`** en algunas computadoras). Esto provocará la excepción **`KeyboardInterrupt`** y permitirá que tu programa salga del bucle. Hablaremos de ello más adelante en el curso.

> ⚠️ En un programa real, un bucle infinito casi siempre es un **error**: una condición de salida que nunca se cumple. `while True` solo se usa de forma **intencional**, combinado con una instrucción que rompe el bucle (`break`), tal como veremos más adelante en el curso.

---
## 🔍 Encontrar el número más grande de un gran conjunto de datos

Volviendo al bosquejo del algoritmo, veamos cómo usar este bucle recién aprendido para encontrar el **número más grande** de un gran conjunto de datos ingresados.

Analiza el programa cuidadosamente. Localiza dónde comienza el bucle **(línea 8)** y descubre cómo se sale del cuerpo del bucle:

```python
# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)
```

### 🧩 Anatomía del bucle

| Línea | Qué ocurre |
|---|---|
| **8** | **Aquí comienza el bucle.** `while number != -1` evalúa la condición **antes** de cada vuelta |
| 9–12 | **Cuerpo del bucle:** si `number` supera al valor guardado, se actualiza `largest_number` |
| **14** | Última línea del cuerpo: se ingresa el **siguiente** número — este paso hace que la condición de la línea 8 pueda cambiar |
| **—** | Cuando el usuario escribe `-1`, la condición de la línea 8 es falsa → el bucle termina y se ejecuta la línea 17 (`print`) |

> 💡 El valor inicial `largest_number = -999999999` actúa como el **"peor caso posible"**: cualquier primer número lo superará.
>
> 📌 El `-1` es un **valor centinela**: no es un dato válido, es la señal **de detener** la lectura.

**Salida del programa** (entrada: `5`, `20`, `9`, `7`, `-1`):

```text
El número más grande es: 20
```

> ⚠️ **Caso borde:** si el primer valor ingresado **ya es** `-1`, el bucle nunca se ejecuta e imprime el centinela inicial (`El número más grande es: -999999999`). Más adelante, con la instrucción `break`, se evitará este problema leyendo el primer valor **dentro** del bucle.

---

## 🎯 El bucle `for` y `range()` con tres argumentos

La función `range()` también puede aceptar **tres argumentos**: inicio, parada e incremento (paso). Echa un vistazo al código del editor:

```python
for i in range(2, 8, 3):
    print("El valor de i es", i)
```

**Salida:**

```text
El valor de i es 2
El valor de i es 5
```

**¿Por qué solo dos líneas?** El tercer argumento es un **incremento**: un valor agregado para controlar la variable en cada giro del bucle (como puedes sospechar, el valor predeterminado del incremento es **1**).

- El **primer argumento** nos dice cuál es el número de **inicio** de la secuencia → `2`.
- El **segundo argumento** le dice a la función dónde **detener** la secuencia: genera números hasta el número indicado, pero **no lo incluye**.
- El **tercer argumento** indica el **paso**: la diferencia entre cada número de la secuencia generada.

Secuencia: **2** (número inicial) → **5** (2 incrementado por 3 = 5, está dentro del rango de 2 a 8) → **8** (5 incrementado por 3 = 8, **no** está dentro del rango, porque el parámetro de parada **no se incluye**).

### 📌 Más sobre la función `range()`

- Si el conjunto generado está **vacío**, el bucle **no ejecutará su cuerpo en absoluto** — no habrá salida:

  ```python
  for i in range(1, 1):
      print("El valor de i es", i)   # sin salida
  ```

- El conjunto debe ordenarse en orden **ascendente**: no hay forma de forzar a `range()` a crearlo de otra forma. Con dos argumentos, el segundo debe ser **mayor** que el primero — tampoco habrá salida:

  ```python
  for i in range(2, 1):
      print("El valor de i es", i)   # sin salida
  ```

> 💡 Para un orden **descendente** hay que usar el tercer argumento con un **incremento negativo**: `for i in range(3, 1, -1):` imprime `3` y `2`.

---

## ⚡ Ejemplo: cálculo de la potencia

Echemos un vistazo a un programa corto cuya tarea es escribir algunas de las **primeras potencias de dos**:

```python
power = 1

for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2
```

```text
2 a la potencia de 0 es 1
2 a la potencia de 1 es 2
2 a la potencia de 2 es 4
...
2 a la potencia de 15 es 32768
```

- La variable **`expo`** se usa como **variable de control** del bucle e indica el valor actual del exponente (`range(16)` → del 0 al 15).
- La propia exponenciación se sustituye **multiplicando por dos** en cada vuelta: como `2⁰ = 1`, después `2 × 1 = 2¹`, `2 × 2¹ = 2²`, y así sucesivamente.

> 🤔 **¿Cuál es el máximo exponente para el cual nuestro programa aún imprime el resultado?** Ejecuta el código y comprueba: es **15** (`range(16)` genera 16 valores, del 0 al 15; la salida llega hasta `2 a la potencia de 15 es 32768`).

---

## 🧪 LAB 3.2.7 — Fundamentos del bucle `for`: contando *mississippily*

**Escenario:** ¿Sabes lo que es *Mississippi*? Es el nombre de uno de los estados y de los ríos de los Estados Unidos. El río tiene aproximadamente **2,340 millas** de largo, lo que lo convierte en el **segundo río más largo** del país — ¡tan largo que una sola gota de agua necesita **90 días** para recorrerlo entero!

La palabra también se usa para un propósito diferente: **contar *mississippimente***. Agregar "Mississippi" a un número al contar segundos en voz alta hace que suene más cercano al reloj: *"un Mississippi, dos Mississippi, tres Mississippi"* ≈ **3 segundos** reales. Así cuentan los niños que juegan al escondite para asegurarse de que el buscador haga un conteo honesto.

**Tu tarea:** escribe un programa que use un bucle `for` para **contar de forma *mississippi* hasta cinco**. Habiendo contado hasta cinco, imprime el mensaje final **"¡Listos o no, ahí voy!"**.

**Esqueleto proporcionado en el editor:**

```python
import time

# Escribe un bucle for que cuente hasta cinco.
# Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
# Cuerpo del bucle - usar: time.sleep(1)
# Escribe una función de impresión con el mensaje final.
```

> ℹ️ **Info extra:** el código contiene dos elementos que aún no se han explicado: la instrucción **`import time`** y el método **`sleep()`**. Se ha importado el módulo `time` y se usa `sleep(1)` para **suspender la ejecución** durante un segundo después de cada `print()` dentro del bucle, de modo que la salida se parezca a un conteo real. No te preocupes: pronto aprenderás más sobre **módulos** y **métodos**.

**Solución validada:**

```python
import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("¡Listos o no, ahí voy!")
```

**Salida esperada:**

```text
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
¡Listos o no, ahí voy!
```

---

## 🐍 Scripts de esta carpeta

| Archivo | Tema |
|---|---|
| [`01 while.py`](01%20while.py) 🐍 | Lee números hasta el centinela `0` y cuenta cuántos son **impares** (`% 2 == 1`) y cuántos **pares** — mismo patrón: lectura antes del `while` y al final del cuerpo |

---

## 📝 Comprueba lo que has aprendido

1. ¿Por qué `while True:` nunca termina por sí solo?
2. ¿Qué papel juega el `-1` en el programa del número más grande?
3. ¿En qué línea comienza a evaluarse la condición del bucle?
4. En `for i in range(2, 8, 3):` ¿qué valores toma `i`? ¿Y por qué no se imprime el `8`?
5. ¿Qué imprime `for i in range(1, 1): ...`?

> **Respuestas:** 1) Porque la condición es el literal `True`, que siempre se cumple. 2) Es el **valor centinela**: la señal para salir del bucle. 3) En la **línea 8**; se reevalúa **antes** de cada vuelta, por eso el cuerpo no se ejecuta si el primer valor ya es `-1`. 4) `2` y `5`: el paso es 3, y el `8` no se imprime porque el argumento de **parada no se incluye** en la secuencia. 5) **Nada** — el conjunto generado está vacío, así que el cuerpo no se ejecuta.

---

## 📝 Resumen

| Concepto | Idea clave |
|---|---|
| `while True:` | **Bucle infinito:** se repite indefinidamente; se corta con `Ctrl-C` (`KeyboardInterrupt`) o con `break` |
| Condición del `while` | Se evalúa **antes** de cada vuelta; si es falsa desde el inicio, el cuerpo **nunca** se ejecuta |
| Valor centinela | Valor especial de "parada" (`-1`, `0`, ...) que no es un dato válido |
| Patrón de lectura | Leer **antes** del `while` + leer **al final** del cuerpo = evitar bucles infinitos accidentales |
| `range(inicio, parada, paso)` | **Inicio** incluido, **parada excluida**, **paso** agregado en cada vuelta (por defecto 1) |
| Rango vacío | Si el conjunto está vacío (`range(1, 1)`, `range(2, 1)`), el cuerpo **no se ejecuta** |
| Orden descendente | Usa un **paso negativo**: `range(3, 1, -1)` genera `3, 2` |
