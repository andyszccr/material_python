# ⚙️ Funciones vs. métodos (3.4.7)

> Notas de apoyo del curso: **3.4.7 — Funciones vs. métodos**. Un método es un tipo especial de función que **pertenece a los datos** con los que trabaja. Aquí está la diferencia con las funciones, las dos formas de invocación (`function(arg)` vs `data.method(arg)`) y por qué este tema llega justo antes de **añadir elementos a una lista**.

---

## 1. La idea clave: ¿a quién pertenece el código?

| | **Función** | **Método** |
|---|---|---|
| **Propiedad de...** | todo el código (no de ningún dato) | los **datos** para los que trabaja |
| **Recibe** | datos (argumentos) | datos (argumentos) |
| **Puede crear** | nuevos datos | nuevos datos |
| **¿Puede cambiar el estado de algo?** | generalmente **no**: (casi) siempre produce un resultado | **sí**: puede cambiar el estado interno de sus datos |
| **Invocación típica** | `result = function(arg)` | `result = data.method(arg)` |

- Un **método** es un tipo específico de función: *se comporta* como una función y *se parece* a una función, pero **difiere en la forma en que actúa y en su estilo de invocación**.
- Invocar un método requiere especificar **los datos a partir de los cuales** se invoca → por eso su nombre va **precedido por el nombre de los datos** que posee.

> 📌 Lo veremos **en profundidad** cuando estudiemos **Programación Orientada a Objetos** (aquí solo reconocemos la sintaxis).

## 2. Las dos formas de invocación

**Función** — toma un argumento, hace algo y devuelve un resultado:

```python
result = function(arg)
```

**Método** — el nombre del método está precedido por el nombre de los datos que posee el método, luego un **punto** y un par de paréntesis que encierran los argumentos:

```python
result = data.method(arg)
```

El método se comporta como una función, pero puede hacer algo más: **cambiar el estado interno de los datos** desde los que se invocó.

```python
len(numeros)        # función: calcula la longitud; NO cambia la lista
numeros.append(4)   # método: añade al final Y cambia la lista
```

## 3. ¿Por qué ahora? (las listas 📋)

Podrías preguntarte: *¿por qué hablamos de métodos y no de listas?* Porque este tema es esencial ahora: **agregar nuevos elementos a una lista existente** se hace con **métodos propios de las listas**, no con funciones.

De los tipos estudiados hasta ahora, **cadenas (`str`)** y **listas (`list`)** son *clases* → pueden ejecutar métodos.

## 4. Verificación ejecutable

```python
numeros = [111, 7, 2, 1]

# función: no pertenece a ningún dato
print(len(numeros))       # 4

# método: pertenece a la lista y cambia su estado
numeros.append(4)
print(numeros)            # [111, 7, 2, 1, 4]
print(len(numeros))       # 5
```

Salida:

```
4
[111, 7, 2, 1, 4]
5
```

## 5. Resumen

- **Función** → propiedad de todo el código; **método** → propiedad de los datos con los que trabaja.
- `result = function(arg)` vs `result = data.method(arg)` → `dato` + `.` + `método(` + argumentos + `)`.
- El método puede **cambiar el estado** de sus datos; la función (normalmente) solo produce un resultado.
- Las listas se amplían con **métodos** (`append()`, `insert()`, …), no con funciones.

## ✍️ Quiz

1. Completa la línea: para añadir el valor `5` al **final** de la lista `numeros`, usarías `numeros.____(5)` *(adelanto de la próxima sección)*.
2. En `len(numeros)` y `numeros.insert(0, 222)`, ¿cuál es la función y cuál el método? ¿Cuál puede cambiar la lista?
3. **V/F:** un método puede cambiar el estado interno de los datos a partir de los cuales se invocó.

<details>
<summary>✅ Respuestas</summary>

1. `append` → `numeros.append(5)` (es el método de las listas para añadir al final).
2. `len` es la **función**; `insert` es el **método** → solo `insert` puede cambiar la lista.
3. **Verdadero** — esa es justamente la diferencia con una función.

</details>

---

⬅️ **Anterior:** [listas.md](listas.md) (3.4.1 intro) · ➡️ **Siguiente:** *Añadir elementos: métodos `append()` e `insert()`* — notas **por crear** *(pendiente)*.
