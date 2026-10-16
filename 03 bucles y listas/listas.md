# 📋 Listas en Python

> Notas de apoyo del curso: **3.4.1 — ¿Por qué necesitamos listas?** (del problema de las variables *escalares* a la primera lista: corchetes, longitud y numeración desde cero).

---

## 😰 3.4.1 ¿Por qué necesitamos listas?

Puede suceder que tengas que **leer, almacenar, procesar y, finalmente, imprimir docenas, quizás cientos, tal vez incluso miles de números**. ¿Entonces qué? ¿Necesitas crear una variable separada para cada valor? ¿Tendrás que pasar largas horas escribiendo sentencias como la que se muestra a continuación?

```python
var1 = int(input())
var2 = int(input())
var3 = int(input())
var4 = int(input())
var5 = int(input())
var6 = int(input())
# ¿y var7, var8, var9, ... hasta var10000?
```

Si no crees que esta sea una tarea complicada, toma un papel y escribe un programa que:

1. lea **cinco números**;
2. los imprima en orden **desde el más pequeño hasta el más grande** (este tipo de procesamiento se denomina **ordenamiento**).

Debes percatarte que ni siquiera tienes suficiente papel para completar la tarea. 😅

### ⚖️ Hasta ahora: variables **escalares**

Hasta ahora has aprendido a declarar variables que pueden almacenar **exactamente un valor dado a la vez**. Tales variables a veces se denominan **escalares**, por analogía con las matemáticas. **Todas las variables que has usado hasta ahora son realmente escalares.**

### 📦 ¿Y una variable "espaciosa"?

Piensa en lo conveniente que sería declarar una variable que pudiera almacenar **más de un valor** — por ejemplo, cien, o mil, o incluso diez mil. Seguiría siendo una y la misma variable, pero muy amplia y espaciosa. ¿Suena atractivo? Quizás, pero **¿cómo manejarías un contenedor así lleno de valores diferentes? ¿Cómo elegirías solo el que necesitas?**

**¿Y si solo pudieras numerarlos?** Y luego decir: *dame el valor número 2; asigna el valor número 15; aumenta el número del valor 10000*.

En Python, ese "contenedor numerado" es un tipo de dato **secuencia**, y el ejemplo que veremos ahora es la **lista** (*list*).

### ✏️ Crear una lista

Creemos una variable llamada `numbers`; no se le asigna solo un número, sino que se **llena con una lista** que consta de cinco valores (la lista comienza con un **corchete abierto** y termina con un **corchete cerrado**; el espacio entre los corchetes se llena con cinco números **separados por comas**):

```python
numbers = [10, 5, 7, 2, 1]
```

Dicho con la terminología adecuada: **`numbers` es una lista que consta de cinco valores**, todos ellos números. También podemos decir que esta sentencia crea una **lista de longitud igual a cinco** (ya que contiene cinco elementos). En Python, `type(numbers)` confirma el tipo: `<class 'list'>`.

### 🔢 Numeración desde cero

Python ha adoptado una convención que indica que **los elementos de una lista están siempre numerados desde cero**. Esto significa que el elemento almacenado al principio de la lista tendrá el número cero. Como hay cinco elementos en nuestra lista, **al último de ellos se le asigna el número cuatro**. *No olvides esto.* Pronto te acostumbrarás, y se convertirá en algo natural.

| Índice | `0` | `1` | `2` | `3` | `4` |
|---|---|---|---|---|---|
| Valor | 10 | 5 | 7 | 2 | 1 |

### 🎭 Elementos de tipos diferentes

Los elementos dentro de una lista **pueden tener diferentes tipos**: algunos pueden ser enteros, otros flotantes, otros cadenas… e incluso **otros elementos pueden ser listas** (las llamaremos *listas multidimensionales* más adelante en el curso):

```python
varios = [1, 2.5, "tres", [4, 5]]
```

### 🧺 Una lista de escalares

Una aclaración antes de continuar: nuestra lista es una **colección de elementos**, pero **cada elemento es un escalar**. Es decir, cada casilla del contenedor guarda un único valor; lo "multivalor" es la lista en su conjunto.

**Verificación ejecutable:**

```python
numbers = [10, 5, 7, 2, 1]
print(type(numbers))    # <class 'list'>
print(numbers)          # [10, 5, 7, 2, 1]

varios = [1, 2.5, "tres", [4, 5]]
print(varios)           # [1, 2.5, 'tres', [4, 5]]
print(varios[3])        # [4, 5] — ¡un elemento puede ser otra lista!
```

### 📌 Resumen de la sección

| Concepto | Idea clave |
|---|---|
| **Escalar** | Variable que guarda **un solo valor** a la vez |
| **Secuencia** | Tipo de datos que guarda **más de un valor** en una variable; en Python, las **listas** son un tipo de secuencia |
| **Lista** | Se crea con corchetes `[]` y valores separados por comas: `[10, 5, 7, 2, 1]` |
| **Longitud** | Número de elementos de la lista (la anterior tiene **5**) |
| **Índice** | Posición numerada **desde 0**: primero `0`, último `longitud - 1` |
| **Tipos mixtos** | Una lista puede combinar enteros, flotantes, cadenas e incluso otras listas |

### ❓ Comprueba lo que has aprendido

1. En `numbers = [10, 5, 7, 2, 1]`, ¿cuántos elementos tiene la lista y con qué índice aparece el último?
2. Verdadero o falso: todos los elementos de una lista deben ser del mismo tipo.
3. ¿Qué imprime `varios[3]` si `varios = [1, 2.5, "tres", [4, 5]]`?

<details>
<summary>✅ Respuestas</summary>

1. Tiene **5** elementos; el último tiene el índice **4** (la numeración empieza en 0).
2. **Falso** — pueden mezclarse enteros, flotantes, cadenas y hasta otras listas.
3. `[4, 5]` — el cuarto elemento es él mismo una lista.

</details>

---

➡️ **Siguiente:** operaciones básicas sobre las listas (modificar elementos por índice, `len()`, `del` para eliminar, etc.) — practica primero con los scripts [`07 listas.py`](07%20listas.py), [`08 listas.py`](08%20listas.py), [`09 listas.py`](09%20listas.py) y [`10 listas.py`](10%20listas.py).