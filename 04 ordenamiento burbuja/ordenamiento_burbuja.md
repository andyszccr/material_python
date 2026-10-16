# 🫧 Ordenamiento burbuja (sección 11)

> Notas de apoyo del curso **3.5.1–3.5.4**: **Ordenación por el algoritmo burbuja** — orden ascendente/descendente, *comparar adyacentes e intercambiar*, el rastro de `[8, 10, 6, 2, 4]`, **cuántos pases hacen falta** (bandera `swapped`), la **versión interactiva**, los métodos `sort()` / `reverse()` y el **resumen de sección**.

---

## 1. Orden ascendente y descendente

| Orden | Definición (por pares adyacentes) |
|---|---|
| **Ascendente** (no descendente) | el primero de cada par **no es mayor** que el segundo |
| **Descendente** (no ascendente) | el primero de cada par **no es menor** que el segundo |

A partir de aquí, siempre **ascendente**: de menor a mayor.

## 2. La idea: comparar adyacentes e intercambiar

Lista de trabajo: **`[8, 10, 6, 2, 4]`**

Algoritmo por cada par de vecinos: ¿el primero es mayor que el segundo? → si están en el orden incorrecto, **intercambiar**; si no, **no hacer nada**.

### Pasada 1 → se coloca el 10 al final

| Par | ¿Intercambio? | Lista resultante |
|---|---|---|
| 8, 10 | no | `[8, 10, 6, 2, 4]` |
| 10, 6 | sí | `[8, 6, 10, 2, 4]` |
| 10, 2 | sí | `[8, 6, 2, 10, 4]` |
| 10, 4 | sí | `[8, 6, 2, 4, 10]` ✅ |

El elemento mayor **acaba en su sitio**; imaginando la lista "de lado", sube como una **burbuja** desde el fondo hasta la superficie de una copa de champán → de ahí el nombre del algoritmo.

### Pasada 2 → se coloca el 8

`[8, 6, 2, 4, 10]` → `[6, 8, 2, 4, 10]` → `[6, 2, 8, 4, 10]` → **`[6, 2, 4, 8, 10]`**

### Pasada 3 → se coloca el 6

`[6, 2, 4, 8, 10]` → `[2, 6, 4, 8, 10]` → **`[2, 4, 6, 8, 10]`** → ¡lista ordenada! 🎉

> Con **5 elementos** harían falta **como máximo 4 pasadas**; aquí bastaron 3 (cada pasada reduce la zona sin ordenar).

## 3. Un solo paso en Python

```python
my_list = [8, 10, 6, 2, 4]

if my_list[0] > my_list[1]:                    # par 1
    my_list[0], my_list[1] = my_list[1], my_list[0]
if my_list[1] > my_list[2]:                    # par 2
    my_list[1], my_list[2] = my_list[2], my_list[1]
if my_list[2] > my_list[3]:                    # par 3
    my_list[2], my_list[3] = my_list[3], my_list[2]
if my_list[3] > my_list[4]:                    # par 4
    my_list[3], my_list[4] = my_list[4], my_list[3]

print(my_list)   # [8, 6, 2, 4, 10]
```

El intercambio usa **asignación múltiple** `a, b = b, a`: cambia los dos valores de un golpe, sin variable auxiliar.

En lugar de cuatro `if` sueltos, conviene codificar **un solo pase completo** con un bucle: para 5 elementos necesitamos `len(my_list) - 1` comparaciones:

```python
my_list = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # ¡intercambio!
```

## 4. Ordenando una lista: ¿cuántos pases? (bandera `swapped`)

**¿Cuántos pases necesitamos para ordenar la lista completa?** Resolvámoslo con otra variable cuya tarea es observar si se ha realizado algún intercambio durante el pase:

- Se crea con el valor **`False`** → *aún no hay intercambios*.
- Si ocurre algún intercambio → se le asigna **`True`**.
- Si al final del pase sigue en `False` → **la lista ya está ordenada** y no hay que hacer nada más.
- El `while` se repite **mientras `swapped` sea `True`**; para entrar la primera vez arrancamos con `swapped = True`.

```python
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)   # [2, 4, 6, 8, 10]
```

Salida: **`[2, 4, 6, 8, 10]`** ✅

- **Anidamiento de bucles:** un `for` dentro de un `while` → el `while` repite pases y el `for` recorre los pares adyacentes (`range(len(my_list) - 1)` va del `0` al penúltimo, porque `i + 1` no puede pasarse del final).
- El `for` recorre **todos** los pares en cada pase (simplificación del curso), aunque la zona final ya esté ordenada; la bandera es la que **corta** antes de tiempo.

📌 En este repo: [`02ordenamiento.py`](02ordenamiento.py) 🐍 es exactamente este programa (ejecutado: imprime `[2, 4, 6, 8, 10]`); [`01ordenamiento.py`](01ordenamiento.py) está *pendiente*.

**Versión interactiva (3.5.3):** el programa se enriquece con una conversación con el usuario: primero pregunta `¿Cuántos elementos deseas ordenar?` con `int(input(...))`, luego lee cada valor con `float(input(...))` y lo añade con `append()`, y por último ordena e imprime la lista.

## 5. El atajo de Python: el método `sort()`

Python tiene **sus propios mecanismos de clasificación**: nadie necesita escribir sus propios algoritmos, ya que hay suficientes herramientas listas-para-usar. El burbuja se explica para aprender a **procesar el contenido de una lista** y ver cómo puede funcionar la clasificación real.

> `sort()` y `reverse()` **son métodos** (ver [funciones_vs_metodos.md](../03%20bucles%20y%20listas/funciones_vs_metodos.md)) → **cambian la propia lista**.

```python
my_list = [8, 10, 6, 2, 4]
my_list.sort()              # ordena lo más rápido posible, EN EL SITIO
print(my_list)              # [2, 4, 6, 8, 10]

my_list.sort(reverse=True)  # ordena descendente
print(my_list)              # [10, 8, 6, 4, 2]

my_list.reverse()           # NO ordena: invierte el orden actual
print(my_list)              # [2, 4, 6, 8, 10]
```

## 6. Resumen de sección (3.5.4)

**1.** El método **`sort()`** ordena los elementos de una lista:

```python
lst = [5, 3, 1, 2, 4]
print(lst)          # [5, 3, 1, 2, 4]

lst.sort()
print(lst)          # [1, 2, 3, 4, 5]
```

**2.** El método **`reverse()`** **invierte** la lista (no la ordena):

```python
lst = [5, 3, 1, 2, 4]
print(lst)          # [5, 3, 1, 2, 4]

lst.reverse()
print(lst)          # [4, 2, 1, 3, 5]
```

### Ideas clave de la sección

- Orden **ascendente** = ningún par adyacente tiene el primero mayor que el segundo.
- Burbuja: comparar cada par de adyacentes e **intercambiar** si están mal; por cada pase, el mayor de la zona sin ordenar queda **al final**.
- Programa: `while swapped` + `for i in range(len(my_list) - 1)` con la bandera **`swapped`** (si un pase termina con `False`, la lista ya está ordenada).
- Atajos: `sort()`, `sort(reverse=True)`, `reverse()` — **métodos** que modifican la lista.

## ✍️ Quiz (cuestionario oficial)

1. ¿Cuál es la salida? `lst = ["D", "F", "A", "Z"]` → `lst.sort()` → `print(lst)`
2. ¿Cuál es la salida? `a, b, c = 3, 1, 2` → `lst = [a, c, b]` → `lst.sort()` → `print(lst)`
3. ¿Cuál es la salida? `lst = ["A", "B", "C", " "]` → `lst.reverse()` → `print(lst)`

<details>
<summary>✅ Respuestas</summary>

1. `['A', 'D', 'F', 'Z']`
2. `[1, 2, 3]`
3. `[' ', 'C', 'B', 'A']` — `reverse()` invierte, **no** ordena.

</details>

---

⬅️ **Anterior:** [funciones_vs_metodos.md](../03%20bucles%20y%20listas/funciones_vs_metodos.md) · ➡️ **Siguiente:** listas multidimensionales / *compresión de listas* — notas **por crear** *(pendiente)*.
